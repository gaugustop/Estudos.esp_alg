import heapq

class Worker:
    def __init__(self, index, free_time):
        self.index = index
        self.free_time = free_time
    
    def __lt__(self, other):
        if self.free_time == other.free_time:
            return self.index < other.index #criterio de desempate
        return self.free_time < other.free_time
    
class Job:
    def __init__(self, processing_time):
        self.processing_time = processing_time
        self.worker = None
        self.start_time = None

def schedule(workers, jobs):
    heapq.heapify(workers)
    for job in jobs:
        worker = heapq.heappop(workers)
        job.worker = worker
        job.start_time = worker.free_time
        worker.free_time += job.processing_time
        heapq.heappush(workers, worker)

if __name__ == "__main__":
    n_workers, n_jobs = map(int, input().split())
    jobs, workers = list(), list()
    for _time in list(map(int, input().split())):
        job = Job(_time)
        jobs.append(job)
    for i in range(n_workers):
        worker = Worker(i,0)
        workers.append(worker)
    schedule(workers, jobs)
    for job in jobs:
        print(job.worker.index, job.start_time)
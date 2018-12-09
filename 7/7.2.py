import re
import string

inputs = open("input.txt", "r").read().splitlines()

def get_working_time(letter):
    return string.ascii_lowercase.upper().index(letter) + 1 + 60

# decrement the time left for each job
def update_times_til_done(time_til_done):
    for key in time_til_done.keys():
        if time_til_done[key] > 0:
            time_til_done[key] -= 1    
    return time_til_done

# find jobs which are done (0 time left)
def get_finished_jobs(time_til_done):
    finished = []
    for key in time_til_done.keys():
        if time_til_done[key] == 0:
            finished.append(key)
    return finished

def build_graph(inputs):
    graph = {}
    for info in inputs:
        cleaned = re.sub('[^A-Z]', '', info[1:])
        start, end = cleaned[0], cleaned[1]
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    return graph

def calculate_tick():
    # https://stackoverflow.com/a/952952
    flatten = lambda l: [item for sublist in l for item in sublist]

    # build a graph from input
    # use a dictionary with key-value-pair denoting an edge from key to value

    graph = build_graph(inputs)

    workers = 5
    tick = 0
    # define initial job, which has no incoming edges
    next_jobs = set(filter(lambda node: node not in flatten(graph.values()), graph.keys()))
    # dictionary for storing time left for current jobs
    time_til_done = {}
    while (True):
        time_til_done = update_times_til_done(time_til_done)
        finished = get_finished_jobs(time_til_done)
        if len(finished) > 0:
            # do for all finished jobs
            for fin in finished:
                # add next jobs to the queue
                if fin not in graph:
                    # finished last job
                    return tick
                # add nodes accessible from finished job
                for node in graph[fin].copy():
                    graph[fin].remove(node)   
                    if node not in flatten(graph.values()):
                        next_jobs.add(node)
                del time_til_done[fin]
        # check if there's space to assign more jobs
        while len(time_til_done.keys()) < workers and len(next_jobs) > 0:
            # find next job in alphabetical order
            next_job = sorted(next_jobs)[0]
            # remove the taken job from next jobs
            next_jobs.remove(next_job)
            # define working time
            work_time = get_working_time(next_job)
            time_til_done[next_job] = work_time
        tick += 1

print(calculate_tick())
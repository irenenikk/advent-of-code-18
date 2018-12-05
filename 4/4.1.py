import re

inputs = open("input1.txt", "r").read().splitlines()

def clean_input(x):
    date_length=4
    # concat times to
    # monthdayhourminute
    time = x[x.find("[")+date_length+1:x.find("]")]
    clean_time = re.sub('[-:, ]', '', time)
    info = x[x.find("]")+2:]
    return clean_time + ":" + info

def sort_inputs(a, b):
    time_a = a[:a.find(":")]
    time_b = b[:b.find(":")]
    # compare day
    if (int(time_a[0:2]) == int(time_b[0:2])):
        # compare month
        if int(time_a[2:4]) == int(time_b[2:4]):
            # compare day
            return cmp(int(time_a[4:]), int(time_b[4:]))
        elif int(time_a[2:4]) > int(time_b[2:4]):
            return 1
        else:
            return -1
    elif int(time_a[0:2]) > int(time_b[0:2]):
        return 1
    else:
        return -1

# start by sorting
inputs = [clean_input(i) for i in inputs]
inputs.sort(sort_inputs)
guard_stats = {}
guard_stats['total'] = {}
guard = -1
fell_asleep = -1
for info in inputs:
    time, sleep_info = info.split(":")
    minutes = int(time[6:])
    # just assume that the input is standardized :------------)
    # check if announces new guard
    if "#" in sleep_info:
        guard = int(re.sub('[a-zA-Z# ]', '', sleep_info))
        if not guard in guard_stats:
            guard_stats[guard] = {}
            guard_stats['total'][guard] = 0
    if "sleep" in sleep_info:
        fell_asleep = minutes
    elif "wakes" in sleep_info:
        if fell_asleep == -1 or guard == -1:
            print("you screwed up my friend")
            exit()
        slept_til = minutes - 1
        for minute in range(fell_asleep, slept_til+1):
            if minute in guard_stats[guard]:
                guard_stats[guard][minute] += 1
            else:
                guard_stats[guard][minute] = 1
            guard_stats['total'][guard] += 1
# find out which guard sleeps the most
max_id = max(guard_stats['total'], key=guard_stats['total'].get)
max_min = max(guard_stats[max_id], key=guard_stats[max_id].get)
print(max_id * max_min)
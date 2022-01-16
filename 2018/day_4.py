#!/usr/bin/env python3
import sys
import re
from datetime import datetime


line_regex = re.compile("\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<content>.+)")


def problem_1(fname):
    guards = {}
    events = []
    with open(fname, "r") as f:
        for line in f.readlines():
            p = re.match(line_regex, line).groupdict()
            # events.append({term: p[term] for term in ["year", "month", "day", "hour", "minute", "content"]})
            events.append((
                datetime(*[int(p[x]) for x in ["year", "month", "day", "hour", "minute"]]),
                {term: p[term] for term in ["year", "month", "day", "hour", "minute", "content"]}))
    ordered_events = sorted(events, key=lambda x:x[0])

    guard_sleep_times = {}
    current_guard = None
    sleep_time = None
    for time, event in ordered_events:
        if event["content"].startswith("Guard #"):
            if sleep_time is not None:
                guard_sleep_times[current_guard] = guard_sleep_times \
                    .get(current_guard, []) + [(sleep_time, 59, 59 - sleep_time)]
            current_guard = int(event["content"][7:].split()[0])
            sleep_time = None
        elif event["content"] == "wakes up" and sleep_time is not None:
            guard_sleep_times[current_guard] = guard_sleep_times \
                    .get(current_guard, []) + [(sleep_time, int(event["minute"]) - 1, int(event["minute"]) - 1 - sleep_time)]
            sleep_time = None
        elif event["content"] == "falls asleep" and sleep_time is None:
            sleep_time = int(event["minute"])

    guard = sorted([(guard, sum(t[2] for t in times)) for guard, times in guard_sleep_times.items()], key=lambda x: x[1])[-1][0]
    mins = {}
    for start, stop, _ in guard_sleep_times[guard]:
        for x in range(start, stop + 1):
            mins[x] = mins.get(x, 0) + 1
    return int(guard) * max(mins.items(), key=lambda x:x[1])[0]

def problem_2(fname):
    guards = {}
    events = []
    with open(fname, "r") as f:
        for line in f.readlines():
            p = re.match(line_regex, line).groupdict()
            events.append((
                datetime(*[int(p[x]) for x in ["year", "month", "day", "hour", "minute"]]),
                {term: p[term] for term in ["year", "month", "day", "hour", "minute", "content"]}))
    ordered_events = sorted(events, key=lambda x:x[0])

    guard_sleep_times = {}
    current_guard = None
    sleep_time = None
    for time, event in ordered_events:
        if event["content"].startswith("Guard #"):
            if sleep_time is not None:
                guard_sleep_times[current_guard] = guard_sleep_times \
                    .get(current_guard, []) + [(sleep_time, 59, 59 - sleep_time)]
            current_guard = int(event["content"][7:].split()[0])
            sleep_time = None
        elif event["content"] == "wakes up" and sleep_time is not None:
            guard_sleep_times[current_guard] = guard_sleep_times \
                    .get(current_guard, []) + [(sleep_time, int(event["minute"]) - 1, int(event["minute"]) - 1 - sleep_time)]
            sleep_time = None
        elif event["content"] == "falls asleep" and sleep_time is None:
            sleep_time = int(event["minute"])

    mins = {}
    for guard, times in guard_sleep_times.items():
        for start, stop, _ in times:
            for x in range(start, stop + 1):
                mins[(guard, x)] = mins.get((guard, x), 0) + 1

    largest_pairing = max(mins.items(), key=lambda x:x[1])[0]
    return int(largest_pairing[0]) * largest_pairing[1]



if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))

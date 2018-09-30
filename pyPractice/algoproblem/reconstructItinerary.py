# -*- conding:utf-8 -*-
import collections

def findItinerary( tickets):
    targets = collections.defaultdict(list)
    print(targets)
    for a, b in sorted(tickets)[::-1]:
        print(a,b)
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        print('stack[-1] %s' % stack[-1])
        print('targets[stack[-1]] %s' % targets[stack[-1]])
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
            print('stack %s' % stack)
        route += stack.pop(),
        print('route %s' % route)
    return route[::-1]



tickets= [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
b=findItinerary(tickets)
print(b)
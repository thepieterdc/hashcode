import heapq
import operator
import random

amtVideos, amtEndpoints, amtRequests, amtCaches, amtCacheSize = (int(i) for i in input().split(" "))
videoSizes = [int(i) for i in str(input()).split(" ")]
endpointDatacenterLatencies = []
endpointLatencies = {}
for e in range(amtEndpoints):
    dcl, epoint = (int(ix) for ix in str(input()).split(" "))
    endpointDatacenterLatencies.append(dcl)
    endpointLatencies[e] = {}
    for video in range(epoint):
        c, l = (int(i) for i in str(input()).split(" "))
        endpointLatencies[e][c] = l
requests = {}
for e in range(amtRequests):
    vid, endpt, reqs = ((int(i) for i in str(input()).split(" ")))
    if vid not in requests:
        requests[vid] = {}
    requests[vid][endpt] = reqs

_sort = {}
videoheapUnsorted = []
for v in requests:
    _sort[v] = sum(requests[v])
    videoheapUnsorted.append((_sort[v], v))
videoheap = sorted(videoheapUnsorted, key=lambda x: x[0], reverse=True)

bestlatencies = {}
for e in range(amtEndpoints):
    bestlatencies[e] = sorted(endpointLatencies[e].items(), key=operator.itemgetter(1))

_cachesvullingVideos = {}
_cachesvullingSizes = {}
for qi in range(amtCaches):
    _cachesvullingVideos[qi] = []
    _cachesvullingSizes[qi] = 0

winst = 0
while videoheap:
    video = videoheap.pop(random.choice(range(len(videoheap))))

    voorlopigecache = -1
    tempwinst = winst
    for epoint in requests[video[1]].keys():
        for cache in endpointLatencies[epoint].keys():
            if video[1] not in _cachesvullingVideos[cache] and _cachesvullingSizes[cache] + videoSizes[
                video[1]] <= amtCacheSize:
                if winst + int(endpointDatacenterLatencies[epoint]) - endpointLatencies[epoint][cache] > tempwinst:
                    tempwinst = winst + int(endpointDatacenterLatencies[epoint]) - endpointLatencies[epoint][cache]
                    voorlopigecache = cache

    if voorlopigecache != -1:
        _cachesvullingSizes[voorlopigecache] += videoSizes[video[1]]
        _cachesvullingVideos[voorlopigecache].append(video[1])
        winst = tempwinst

        viewsnodes = 0

        for epoint in requests[video[1]].keys():
            if voorlopigecache in endpointLatencies[epoint].keys():
                viewsnodes += requests[video[1]][epoint]

        video_viewsnodes = video[0] - viewsnodes
        if video_viewsnodes > 0:
            pos = 0
            for i in videoheap:
                if i[0] < video_viewsnodes:
                    videoheap.insert(pos, (video_viewsnodes, video[1]))
                    break
                pos += 1

usedcaches = len([x for x in _cachesvullingSizes if _cachesvullingSizes[x] != 0])
print(usedcaches)

for cache in _cachesvullingVideos:
    if _cachesvullingSizes[cache] != 0:
        print("{} {}".format(cache, " ".join(str(x) for x in _cachesvullingVideos[cache])))

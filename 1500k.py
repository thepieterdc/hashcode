import operator

amtVideos, amtEndpoints, amtRequests, amtCaches, amtCacheSize = (int(i) for i in input().split(" "))
videoSizes = [int(i) for i in str(input()).split(" ")]
endpointDatacenterLatencies = []
endpointLatencies = {}
for e in range(amtEndpoints):
    dcl, k = (int(ix) for ix in str(input()).split(" "))
    endpointDatacenterLatencies.append(dcl)
    endpointLatencies[e] = {}
    for i in range(k):
        c, l = (int(i) for i in str(input()).split(" "))
        endpointLatencies[e][c] = l
requests = {}
for e in range(amtRequests):
    vid, endpt, reqs = ((int(i) for i in str(input()).split(" ")))
    if vid not in requests:
        requests[vid] = {}
    requests[vid][endpt] = reqs

_sort = {}
for v in requests:
    _sort[v] = sum(requests[v])
mostpopularvideos = sorted(_sort.items(), key=operator.itemgetter(1), reverse=True)

bestlatencies = {}
for e in range(amtEndpoints):
    bestlatencies[e] = sorted(endpointLatencies[e].items(), key=operator.itemgetter(1))

_cachesvullingVideos = {}
_cachesvullingSizes = {}
for qi in range(amtCaches):
    _cachesvullingVideos[qi] = []
    _cachesvullingSizes[qi] = 0

winst = 0
for i in mostpopularvideos:
    voorlopigecache = -1
    tempwinst = winst
    for k in requests[i[0]].keys():
        for cache in endpointLatencies[k].keys():
            if _cachesvullingSizes[cache] + videoSizes[i[0]] <= amtCacheSize:
                if winst + int(endpointDatacenterLatencies[k]) - endpointLatencies[k][cache] > tempwinst:
                    tempwinst = winst + int(endpointDatacenterLatencies[k]) - endpointLatencies[k][cache]
                    voorlopigecache = cache

    if voorlopigecache != -1:
        _cachesvullingSizes[voorlopigecache] += videoSizes[i[0]]
        _cachesvullingVideos[voorlopigecache].append(i[0])
        winst = tempwinst

usedcaches = len([x for x in _cachesvullingSizes if _cachesvullingSizes[x] != 0])
print(usedcaches)

for cache in _cachesvullingVideos:
    if _cachesvullingSizes[cache] != 0:
        print("{} {}".format(cache, " ".join(str(x) for x in _cachesvullingVideos[cache])))

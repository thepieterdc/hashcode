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

for i in mostpopularvideos:
    found = False
    for k in requests[i[0]].keys():
        if found:
            break
        for cache in endpointLatencies[k].keys():
            if _cachesvullingSizes[cache] + videoSizes[i[0]] <= amtCacheSize:
                _cachesvullingSizes[cache] += videoSizes[i[0]]
                _cachesvullingVideos[cache].append(i[0])
                found = True
                break


usedcaches = len([x for x in _cachesvullingSizes if _cachesvullingSizes[x] != 0])
print(usedcaches)

for cache in _cachesvullingVideos:
    if _cachesvullingSizes[cache] != 0:
        print("{} {}".format(cache, " ".join(str(x) for x in _cachesvullingVideos[cache])))

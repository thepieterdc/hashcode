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
def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    dict = {};
    for f in flights:
        if f[0] not in dict:
            dict[f[0]] = [(f[1],f[2])];
        else:
            dict[f[0]].append((f[1],f[2]));
    minPrice = [100000000] * n;
    minPrice[src] = 0;
    queue = [src];
    i = 0;
    to_update = [];
    while i <= K and queue:
        for e in to_update:
            if minPrice[e[0]] > e[1]:
                minPrice[e[0]] = e[1];
        del to_update;
        to_update = [];
        next_queue = [];

        for q in queue:
            if q in dict:
                for e in dict[q]:
                    if minPrice[q] + e[1] < minPrice[e[0]]:
                        if e[0] not in queue:
                            minPrice[e[0]] = minPrice[q] + e[1];
                        else:
                            to_update.append((e[0], minPrice[q] + e[1]));
                        if e[0] not in next_queue:
                            next_queue.append(e[0]);

        del queue;
        queue = next_queue;
        i = i + 1;

    for e in to_update:
        if minPrice[e[0]] > e[1]:
            minPrice[e[0]] = e[1];
    if minPrice[dst] < 100000000:
        return minPrice[dst];
    else:
        return -1;









flights = [[0,1,500],[1,2,300],[0,2,1000],[0,3,200],[1,4,100],[1,5,100],[3,2,400],[2,6,200],[6,7,200]];
print(findCheapestPrice(8,flights,0,5,2));
def pourWater(heights, V, K):
    """
    :type heights: List[int]
    :type V: int
    :type K: int
    :rtype: List[int]
    """
    l = len(heights);
    n = 0;
    while n < V:
        j = K - 1;
        cur = K;
        while j >= 0:
            if heights[j] > heights[cur]:
                break;
            elif heights[j] == heights[cur]:
                j = j - 1;
                continue;
            else:
                cur = j;
            j = j - 1;
        if cur != K:
            heights[cur] = heights[cur] + 1;
            n = n + 1;
            continue;
        j = K + 1;
        while j < l:
            if heights[j] > heights[cur]:
                break;
            elif heights[j] == heights[cur]:
                j = j + 1;
                continue;
            else:
                cur = j;
            j = j + 1;
        heights[cur] = heights[cur] + 1;
        n = n + 1;

    return heights;

h = [2,1,1,2,1,2,2];
V = 4;
K = 3;
n = 3;

def maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    l = len(height);
    max = 0;
    max_height = 0;
    max_index = 0;
    for i in range(l):
        if height[i] > max_height:
            max_height = height[i];
            max_index = i;
    for i in range(l):
        s = height[i] * abs(max_index - i);
        if s > max:
            max = s;
    print(max);
    for i in range(l - 1):
        if height[i] * (i) < max and height[i] * (l - i) < max:
            continue;
        for j in range(i + 1, l):
            s = min(height[i], height[j]) * (j - i);
            if s > max:
                max = s;

    return max;

a = maxArea([1,8,6,2,5,4,8,3,7]);
print(a);

def nextPermutation( nums):
    l = len(nums);
    if l <= 1:
        return;
    i = l - 1;
    a = 0;
    while i > 0:
        if nums[i] > nums[i - 1]:
            break;
        i = i - 1;
    if i == l-1:
        t1 = nums[i];
        nums[i] = nums[i - 1];
        nums[i - 1] = t1;
        return;
    if i != 0:
        a = i - 1;
    else:
        j = 0;
        while j < int(l / 2):
            t2 = nums[j];
            nums[j] = nums[l-1-j];
            nums[l-1-j] = t2;
            j = j + 1;
        return;
    i = l - 1;
    while i > a:
        if nums[i] > nums[a]:
            break;
        i = i - 1;
    t = nums[i];
    nums[i] = nums[a];
    nums[a] = t;
    j = a + 1;
    k = 0;
    while k < (l - 1 - a)/2:
        t = nums[k+a+1];
        nums[k+a+1] = nums[l - k-1];
        nums[l  -1-k] = t;
        k = k + 1;
    return;

nums = [5,4,7,5,3,2];
nextPermutation(nums);
print(nums);
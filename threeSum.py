def threeSum( nums):
    def twoSum(nums, target):
        print(nums);
        dict = {};
        result = [];
        l = len(nums);
        for i in range(l):
            dict[nums[i]] = i;

        i = 0;
        while (i < l):
            key = dict.keys();
            if (target - nums[i]) in key and dict[target - nums[i]] != i:
                result.append([nums[i], target - nums[i]]);
                del dict[target - nums[i]];
                if nums[i] != target - nums[i]:
                    del dict[nums[i]];
                while i < l - 1 and nums[i] == nums[i + 1]:
                    i = i + 1;
            i = i + 1;

        return result;

    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l = len(nums);
    nums = sorted(nums);
    i = 0;
    result = [];
    t = [];
    t_twoSum = [];
    while i < l - 1:
        t_twoSum = twoSum(nums[i + 1:l], 0 - nums[i]);
        if len(t_twoSum) != 0:
            for t in t_twoSum:
                result.append([nums[i], t[0], t[1]]);
            while i < l - 1 and nums[i] == nums[i + 1]:
                i = i + 1;
        i = i + 1;
    return result;

nums = [-1, 0, 1, 2, -1, -4];
print(threeSum(nums));
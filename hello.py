def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    l1 = len(nums1);
    l2 = len(nums2);
    print(l1);
    print(l2);
    if l1 == 0:
        if l2 % 2 == 1:
            return nums2[int(l2 / 2)];
        else:
            return (nums2[l2 / 2] + nums2[l2 / 2 - 1]) / 2;
    else:
        if l2 == 0:
            if l1 % 2 == 1:
                return nums1[int(l1 / 2)];
            else:
                return (nums1[l1 / 2] + nums1[l1 / 2 - 1]) / 2;
        else:
            if (l1 + l2) % 2 == 1:
                m = int((l1 + l2) / 2);
                i = j = t = 0;
                while t < m and i < l1 and j < l2:
                    if nums1[i] < nums2[j]:
                        i = i + 1;
                    else:
                        j = j + 1;
                    t = t + 1;
                if i == l1:
                    return nums2[m - t + j];
                elif j == l2:
                    return nums1[m - t + i];
                else:
                    return min(nums1[i], nums2[j]);

            else:
                m = (l1 + l2) / 2 - 1;
                i = j = t = 0;
                while t < m and i < l1 and j < l2:
                    if nums1[i] < nums2[j]:
                        i = i + 1;
                    else:
                        j = j + 1;
                    t = t + 1;
                if i == l1:
                    return (nums2[m - t + j] + nums2[m - t + j + 1]) / 2;
                elif j == l2:
                    return (nums1[m - t + i] + nums1[m - t + i + 1]) / 2;
                else:
                    return (nums1[i] + nums2[j]) / 2;

s1 = [1,2];
s2 = [3,4];
print(findMedianSortedArrays(s1,s2));
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices);
        list1 = [];
        for i in range(l):
            list1.append((prices[i], i))
        list1.sort(key=lambda x: x[0])
        print(list1)
        i = 0;
        j = l - 1;
        while i < j:
            t1 = list1[i];
            t2 = list1[j];
            if list1[i][1] < list1[j][1] and :
                return list1[j][0] - list1[i][0]
            else:
                if list1[i][1] > list1[i + 1][1]:
                    i = i + 1;
                    continue;
                if list1[j][1] < list1[j - 1][1]:
                    j = j - 1;
                    continue;
                i = i + 1;

        return 0


s = Solution();
print(s.maxProfit([7,2,1,4]))
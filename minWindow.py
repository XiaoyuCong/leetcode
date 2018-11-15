import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_t = collections.defaultdict(int);
        dict_s = collections.defaultdict(int);
        for e in t:
            dict_t[e] += 1;
        for e in s:
            dict_s[e] += 1;

        l = len(s);
        l_t = len(t);
        isContain = True;
        for e in dict_t:
            if dict_s[e] < dict_t[e]:
                isContain = False
        if not isContain:
            return ""
        else:
            i = 0;
            j = l - 1;
            while i < j:
                if dict_s[s[j]] > dict_t[s[j]]:
                    dict_s[s[j]] -= 1;
                    j -= 1;
                else:
                    break;
            min_l = j - i;
            min_s = s[i:j + 1];
            while (j - i) >= l_t:
                while i <= j:
                    if dict_s[s[i]] > dict_t[s[i]]:
                        dict_s[s[i]] -= 1;
                        i += 1;
                    else:
                        if j - i < min_l:
                            min_l = j - i;
                            min_s = s[i:j + 1];
                        dict_s[s[i]] -= 1;
                        i += 1;
                        print(i)
                        break;

                while j < l:
                    if dict_s[s[j]] < dict_t[s[j]]:
                        break;
                    else:
                        dict_s[s[j]] += 1;
                        j = j + 1;

            return min_s;


s = Solution();
print(s.minWindow("ADOBECODEBANC","ABC"));
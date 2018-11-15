class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def Match(s, p):
            l1 = list(s);
            l2 = list(p);
            len1 = len(l1);
            len2 = len(l2);
            if len2 == 0:
                if len1 == 0:
                    return True
                else:
                    return False
            else:
                if len2 == 1:
                    if len1 == 1:
                        if s[0] == p[0] or p[0] == '.':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    c1 = p[0]
                    c2 = p[1]
                    if c2 != '*':
                        if len1 == 0:
                            return False
                        if s[0] == c1 or c1 == '.':
                            return Match(s[1:], p[1:])
                        else:
                            return False
                    else:
                        if len1 == 0:
                            return Match(s, p[2:])
                        if c1 == '.':
                            for i in range(len1 + 1):
                                if Match(s[i:], p[2:]):
                                    return True
                            return False
                        else:
                            for i in range(len1 + 1):
                                if Match(s[i:], p[2:]):
                                    return True
                                if i == len1:
                                    break
                                if s[i] != p[0]:
                                    break
                            return False

        return Match(s, p)


s = Solution()
print(s.isMatch("aaa","a.a"))
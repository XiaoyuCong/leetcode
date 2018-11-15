class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def checkValid(s):
            l = [];
            for i in range(len(s)):
                if s[i] == '(':
                    l.append(s[i]);
                elif s[i] == ')':
                    if len(l) != 0:
                        l.pop();
                    else:
                        return False;
                else:
                    continue;
            if len(l) != 0:
                return False;
            return True;

        dict = {};
        queue = [];
        queue.append(s);
        dict[s] = 0;
        while len(queue) != 0:
            e = queue[0];
            del queue[0];
            if not checkValid(e):
                l = len(e);
                for i in range(l):
                    if e[i] == '(' or e[i] == ')':
                        t = e[0:i] + e[i + 1:l];
                        if t not in dict:
                            dict[t] = dict[e] + 1;
                            queue.append(t);


import copy
def deleteOneElement(s):
    s = list(s);
    result = [];
    for i in range(len(s)):
        d = copy.deepcopy(s);
        del d[i];
        result.append(d);

    return result;

def dedeleteOneElement1(s):
    result = [];
    l = len(s);
    for i in range(len(s)):
        result.append(s[0:i]+s[i+1:l]);
    return result;

s = "123456789";
print(dedeleteOneElement1(s));
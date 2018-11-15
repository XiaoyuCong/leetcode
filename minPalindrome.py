def ifpalindrome(s1, s2):
    s = s1 + s2;
    l = len(s);
    for i in range(int(l / 2)):
        if s[i] != s[l - 1 - i]:
            return False;

    return True;


def minpalindrome2(s):
    if len(s) <= 1:
        return "";
    result = "";
    i = 0;
    while i < len(s):
        if ifpalindrome(s,result):
            return result;
        result = s[i] + result;
        i = i + 1;

def minpalindrome(s):
    l = len(s);
    if l <= 1:
        return "";
    s_r = s[::-1];
    i = l - 1;
    while i >= 0:
        if ifpalindrome(s_r[0:i+1], ""):
            return s_r[i+1:];
        i = i - 1;

s = "abbbb";
print(minpalindrome(s));
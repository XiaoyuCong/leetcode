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

print(checkValid(''));
a = [1,2,3,4];
print(a[-4:]);
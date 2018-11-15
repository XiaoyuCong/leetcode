
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    c = 0;
    l1 = list(a);
    l2 = list(b);
    l1.reverse();
    l2.reverse();
    result = [];
    l = min(len(a), len(b));
    for i in range(l):
        if l1[i] == '0':
            if l2[i] == '0':
                if c == 0:
                    result.append('0');
                    c = 0;
                else:
                    result.append('1');
                    c = 0;
            else:
                if c == 0:
                    result.append('1');
                    c = 0;
                else:
                    result.append('0');
                    c = 1;
        else:
            if l2[i] == '0':
                if c == 0:
                    result.append('1');
                    c = 0;
                else:
                    result.append('0');
                    c = 1;
            else:
                if c == 0:
                    result.append('0');
                    c = 1;
                else:
                    result.append('1');
                    c = 1;

    if len(a) > l:
        if c == 0:
            for i in range(l, len(a)):
                result.append(l1[i]);
        else:
            for i in range(l, len(a)):
                if l1[i] == '0':
                    if c == 0:
                        result.append('0');
                        c = 0;
                    else:
                        result.append('1');
                        c = 0;
                else:
                    if c == 0:
                        result.append('1');
                        c = 0;
                    else:
                        result.append('0');
                        c = 1;
    elif len(b) > l:
        if c == 0:
            for i in range(l, len(b)):
                result.append(l2[i]);
        else:
            for i in range(l, len(b)):
                if l2[i] == '0':
                    if c == 0:
                        result.append('0');
                        c = 0;
                    else:
                        result.append('1');
                        c = 0;
                else:
                    if c == 0:
                        result.append('1');
                        c = 0;
                    else:
                        result.append('0');
                        c = 1;
    if c == 1:
        result.append('1');

    result.reverse();
    t = ''.join(result);
    return t;

a = "11011";
b = "11";
l = list(a);
l = l.reverse();
print(addBinary(a,b));
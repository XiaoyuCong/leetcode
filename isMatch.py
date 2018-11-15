def ismatch(s,p):
    l1 = len(s);
    l2 = len(p);
    if l2 == 0:
        if l1 == 0:
            return True;
        else:
            return False;
    if l1 == 0:
        if l2 == 1:
            return False;
        elif p[1] == '*':
            return ismatch(s,p[2:]);
        else:
            return False;
    i1 = 0;
    i2 = 0;

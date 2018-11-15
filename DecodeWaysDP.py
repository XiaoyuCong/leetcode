def decodeWaysDP(s):

    dict = {};
    dict[0] = 1;
    if s[-1] == '0':
        dict[-1] = 0;
    else:
        dict[-1] = 1;
    l = -1 * len(s);
    i = -2;
    while i >= l:
        if s[i] == '0':
            dict[i] = 0;
        elif s[i] == '1':
            if s[i+1] == '0':
                dict[i] = dict[i+2];
            else:
                dict[i] = dict[i+1] + dict[i+2];
        elif s[i] == '2':
            if s[i+1] >= '1' and s[i+1] <= '6':
                dict[i] = dict[i+1] + dict[i+2];
            elif s[i+1] == '0':
                dict[i] = dict[i+2];
            else:
                dict[i] = dict[i+1];
        else:
            dict[i] = dict[i+1];
        i = i - 1;

    return dict[l];

a = "226";
print(decodeWaysDP(a));


def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s);
    if l == 0:
        return 1;
    if s[0] == '0':
        return 0;
    if l == 1:
        return 1;

    if s[0] == '1':
        if s[1] == '0':
            return numDecodings(s[2:]);
        else:
            return numDecodings(s[2:]) + numDecodings(s[1:]);

    if s[0] == '2':
        if s[1] >= '1' and s[1] <= '6':
            return numDecodings(s[2:]) + numDecodings(s[1:]);
        elif s[1] == '0':
            return numDecodings(s[2:]);
        else:
            return numDecodings(s[1:]);


    return numDecodings(s[1:]);



print(numDecodings("44444444444444444444444444441444444444444444444444"));
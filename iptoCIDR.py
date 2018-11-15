def ipToCIDR(ip, n):
    """
    :type ip: str
    :type n: int
    :rtype: List[str]
    """
    if n == 1:
        return ip + "/32";
    pwr2 = [1]*32;
    i = 1;
    while i <= 31:
        pwr2[i] = pwr2[i-1] * 2;
        i = i + 1;

    split_ip = ip.split('.');
    decode_ip = [];
    for i in split_ip:
        decode_ip.extend(decode(int(i)));

    result = [];
    i = 30;
    if decode_ip[31] == 1:
        n = n - 1;
        result.append(str(encode(decode_ip[0:8],pwr2[0:8])) +"."+ str(encode(decode_ip[8:16],pwr2[0:8])) \
                 +"."+ str(encode(decode_ip[16:24],pwr2[0:8])) +"."+ str(encode(decode_ip[24:32],pwr2[0:8])) + "/32");
        decode_ip[31] = 0;
    else:
        if n == 2:
            result.append(str(encode(decode_ip[0:8],pwr2[0:8])) +"."+ str(encode(decode_ip[8:16],pwr2[0:8])) \
                 +"."+ str(encode(decode_ip[16:24],pwr2[0:8])) +"."+ str(encode(decode_ip[24:32],pwr2[0:8])) + "/31");
            return result;
        sum = 2;
        while i >= 0:
            if decode_ip[i] == 1:
                result.append(str(encode(decode_ip[0:8],pwr2[0:8])) +"."+ str(encode(decode_ip[8:16],pwr2[0:8])) \
                 +"."+ str(encode(decode_ip[16:24],pwr2[0:8])) +"."+ str(encode(decode_ip[24:32],pwr2[0:8])) + "/" + str(i+1));
                n = n - sum;
                break;
            else:
                sum = sum + pwr2[31-i];
                if sum >= n:
                    decode_n = [];
                    while n > 0:
                        decode_n.append(n % 2);
                        n = int(n / 2);

                    l = len(decode_n);
                    t = l - 1;
                    while t >= 0:
                        if decode_n[t] == 1:
                            result.append(
                                str(encode(decode_ip[0:8], pwr2[0:8])) + "." + str(encode(decode_ip[8:16], pwr2[0:8])) \
                                + "." + str(encode(decode_ip[16:24], pwr2[0:8])) + "." + str(
                                    encode(decode_ip[24:32], pwr2[0:8])) + "/" + str(32 - t));
                            decode_ip[31 - t] = 1;
                        t = t - 1;
                    return result;
            i = i - 1;

    while i >= 0 and n!=0:
        if decode_ip[i] == 0:
            if n > pwr2[31-i]:
                n = n - pwr2[31-i];
                decode_ip[i] = 1;
                result.append(str(encode(decode_ip[0:8],pwr2[0:8])) +"."+ str(encode(decode_ip[8:16],pwr2[0:8])) \
                 +"."+ str(encode(decode_ip[16:24],pwr2[0:8])) +"."+ str(encode(decode_ip[24:32],pwr2[0:8])) + "/" + str(i+1));
                decode_ip[i] = 0;
            else:
                break;
        else:
            decode_ip[i] = 0;
        i = i - 1;
    if n == 0:
        return result;
    else:
        decode_ip[i] = 1;
        decode_n = [];
        while n > 0:
            decode_n.append(n%2);
            n = int(n/2);

        l = len(decode_n);
        t = l - 1;
        while t >= 0:
            if decode_n[t] == 1:
                result.append(str(encode(decode_ip[0:8],pwr2[0:8])) +"."+ str(encode(decode_ip[8:16],pwr2[0:8])) \
                     +"."+ str(encode(decode_ip[16:24],pwr2[0:8])) +"."+ str(encode(decode_ip[24:32],pwr2[0:8])) + "/" + str(32-t));
                decode_ip[31 - t] = 1;
            t = t - 1;

        return result;



def decode(ip):
    result = [];
    i = 0;
    while i < 8:
        result.append(ip % 2);
        ip = int(ip/2);
        i = i + 1;
    result.reverse();
    return result;

def encode(l,pwr2):
    result = 0;
    for i in range(8):
        result = result + pwr2[7-i] * l[i];
    return result;



ip = "117.145.102.62";
n = 8;
print(ipToCIDR(ip,n));
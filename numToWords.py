def numberToWords( num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "zero";
    dict_one = {};
    dict_ten = {};
    dict_ten[2] = "twenty";
    dict_ten[3] = "thirty";
    dict_ten[4] = "forty";
    dict_ten[5] = "fifty";
    dict_ten[6] = "sixty";
    dict_ten[7] = "seventy";
    dict_ten[8] = "eighty";
    dict_ten[9] = "ninety";
    dict_one[1] = "one";
    dict_one[2] = "two";
    dict_one[3] = "three";
    dict_one[4] = "four";
    dict_one[5] = "five";
    dict_one[6] = "six";
    dict_one[7] = "seven";
    dict_one[8] = "eight";
    dict_one[9] = "nine";
    dict_one[10] = "ten";
    dict_one[11] = "eleven";
    dict_one[12] = "twelve";
    dict_one[13] = "thirteen";
    dict_one[14] = "fourteen";
    dict_one[15] = "fifteen";
    dict_one[16] = "sixteen";
    dict_one[17] = "seventeen";
    dict_one[18] = "eighteen";
    dict_one[19] = "nineteen";
    def threeDigitalToWords(num):
        hundred = int(num / 100);
        one = num % 10;
        ten = int(num / 10) % 10;
        result = "";
        if hundred != 0:
            result = result + dict_one[hundred] + " hundred";
        if ten == 1:
            if len(result) != 0:
                result = result + " ";
            result = result + dict_one[10+one];
            return result;
        if ten != 0:
            if len(result) != 0:
                result = result + " ";
            result = result + dict_ten[ten];
        if one != 0:
            if len(result) != 0:
                result = result + " ";
            result = result + dict_one[one];

        return result;

    division = [];
    result = "";
    for i in range(4):
        division.append(num % 1000);
        num = int(num / 1000);

    if division[3] != 0:
        result = result + threeDigitalToWords(division[3]) + " " + "billion";
    if division[2] != 0:
        if len(result) != 0:
            result = result + " ";
        result = result + threeDigitalToWords(division[2]) + " " + "million";
    if division[1] != 0:
        if len(result) != 0:
            result = result + " ";
        result = result + threeDigitalToWords(division[1]) + " " + "thousand";
    if division[0] != 0:
        if len(result) != 0:
            result = result + " ";
        result = result + threeDigitalToWords(division[0]);

    return result;

print(numberToWords(12232));
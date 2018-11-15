def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
        return 0;
    l = len(coins);
    j = 0;
    l_q = 1;
    queue = [(0, 0, 0)];
    coins = sorted(coins, reverse=True);
    while j < l_q:
        e = queue[j];
        for i in range(e[1], l):
            sum = e[0] + coins[i];
            step = e[2] + 1;
            if sum < amount:
                queue.append((sum, i, step));
            elif sum == amount:
                return step;
        l_q = len(queue);
        j = j + 1;

    return -1;


print(coinChange([80,149,71,111],8683));
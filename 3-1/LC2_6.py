def myAtoi(self,s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    signal = 1
    if s == '':
        return 0
    if s[0] == '-':
        signal = -1
        s = s[1:]
    elif s[0] == '+':
        signal = 1
        s = s[1:]
    res = 0
    for i in range(len(s)):
        if s[i].isdigit():
            res = res * 10 + int(s[i])
        else:
            break;
    res = res * signal
    if res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif res < -2 ** 31:
        return -2 ** 31
    else:
        return res
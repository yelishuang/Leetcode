def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    lst = []
    for i in range(len(s)):
        if s[i] in lst:
            continue
        if s[i] not in s[i+1:] :
            return i
        else:
            lst.append(s[i])
    return -1



def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    mini_find = len(s)
    for i in "abcdefghijklmnopqrstuvwxyz":
        if s.count(i) == 1 :
                mini_find= s.find(i) if s.find(i) < mini_find else mini_find
    if mini_find == len(s):
        return -1
    else:
        return mini_find
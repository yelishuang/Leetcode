def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    i = 0
    res=""
    if len(strs) == 0:
        return res
    if len(strs) == 1:
        return strs[0] 
    for i in range(len(strs[0])):
        char=strs[0][i]
        for str_ in strs:
            if len(str_) <= i:
                return res
            if str_[i] != char :
                return res
        res += char
    return res
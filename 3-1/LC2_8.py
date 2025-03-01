def countAndSay(self,n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    if n == 1:
        return "1"
    else:
        str_ = self.countAndSay(n - 1)
        i=0
        j=0
        while i < len(str_):
            count=0
            while str_[j] == str_[i]:
                j += 1
                count += 1
                if j >= len(str_):
                    break
            res = res + str(count) + str(str_[i])
            i=j
        return res
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x<0 :
        signal = -1
        x = str(x)
        x = x[1:] 
        x = x[::-1]
    else : 
        signal=1
        x = str(x)
        x = x[::-1]
    x = int(x)*signal
    if    -2**31 <= x <= 2**31-1:
        return x
    else:
        return 0
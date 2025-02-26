def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num=0
    for i in digits:
        num=num*10+i
    num=num+1
    
    nums=[]
    while num > 0 :
        nums.insert(0,num % 10)
        num = num /10
    return nums
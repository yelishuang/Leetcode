def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j=0
    for i in nums:
        j = j ^ i   
    return j 
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        t= target -nums[i]
        for  j in range(i+1,len(nums)):
            if(nums[j]==t):
                return [i,j]
            


def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict_num = dict()
    for i, v in enumerate(nums):
        tmp = target - v
        if dict_num.get(tmp) is not None:
            return i, dict_num[tmp]
        else:
            dict_num[v] = i
    return 0, 0

# 探讨为什么第二种方案比第一种效率高
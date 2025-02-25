def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i=0
    for j in range(1,len(nums)):
        if(nums[i] == nums[j]):
            continue
        else:
            i=i+1
            nums[i]=nums[j]
    nums=nums[0:i+1]#python这种方式获取子数组，右边不包含所以要+1
    return len(nums)    


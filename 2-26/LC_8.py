def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i=0
    j=0
    while j < len(nums):
        if  nums[j] == 0 :
            j=j+1
        else:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i=i+1
            j=j+1
    return nums
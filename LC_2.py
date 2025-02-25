def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if k == 0 :
        return nums
    else :
         nums=nums[k+1:] + nums[0:k+1]
         print(nums)

if __name__ == "__main__":
    List=[1,2,3,4,5,6,7]
    print(rotate(List,3))
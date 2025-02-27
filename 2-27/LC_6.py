def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    temp=[]
    if(len(nums1)>len(nums2)):
        for num in nums2 :
            if num in nums1 :
                temp.append(num)
                nums1.remove(num)
    else:
        for num in nums1 :
            if num in nums2 :
                temp.append(num)
                nums2.remove(num)
    return temp


def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    i=0
    j=0
    temp=[]
    while i < len(nums1) and j < len(nums2):
        if (nums1[i] == nums2[j]):
            temp.append(nums1[i])
            i=i+1
            j=j+1
        elif(nums1[i] > nums2[j]):
            j=j+1
        else:
            i=i+1
    return temp


def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    counter1 = collections.Counter(nums1)
    counter2 = collections().Counter(nums2)
    nums = counter1 & counter2
    return list(nums.elements())
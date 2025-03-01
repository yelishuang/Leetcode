def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict_str1 = {}
    for str1 in s:
        if str1 not in dict_str1.keys():
            dict_str1[str1] = 0
        else:
            dict_str1[str1] += 1
    dict_str2 = {}
    for str2 in t:
        if str2 not in dict_str2.keys():
            dict_str2[str2] = 0
        else:
            dict_str2[str2] += 1
    
    return dict_str1 == dict_str2
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    result = ""
    
    for char in s:
        if char.isalnum():
            if char.isupper():
                result+=char.lower()
            else:
                result+=char
    return result[::-1]==result
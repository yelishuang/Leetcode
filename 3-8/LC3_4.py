def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    p = list1
    q = list2 
    head = ListNode()
    t = head
    while p and q :
        if p.val > q.val:
            t.next = q
            t = t.next
            q = q.next
        else:
            t.next = p
            t = t.next
            p = p.next
    if p is None:
        t.next = q
    else :
        t.next = p
    return head.next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    NEWhead = ListNode(-1)
    NEWhead.next=head
    fast = NEWhead
    while n +1 :
        fast = fast.next
        n = n - 1
    slow = NEWhead
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return NEWhead.next

if __name__=="__main__":
    head=ListNode(1)
    print(removeNthFromEnd(head,1))

# 关于节点引用与内存的关系
# 如果删除的是头节点：假设你需要删除的是链表的第一个节点（即head），那么根据你的算法，慢指针slow最终会停在NEWhead上（也就是虚拟头节点），然后你通过slow.next = slow.next.next;跳过了原本的头节点head。但是，如果你返回的是head，你仍然返回的是原来的头节点，即使它已经被从链表中移除了。这样做的结果是，返回的链表仍然是原来的样子，而实际上头节点应该已经改变了。
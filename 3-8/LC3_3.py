class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    node = head
    reverse_head = ListNode()
    first_node = reverse_head.next
    while node:
        node_ = ListNode(node.val)
        reverse_head.next = node_
        node_.next = first_node
        first_node = reverse_head.next
        node=node.next
    return first_node   

if __name__=="__main__":
    head = ListNode()
    last = head
    for i in range(1,6):
        node = ListNode(i)
        last.next = node
        last = node
    node = head.next
    while node:
        print(node.val)
        node = node.next
    reverseList(head.next)
# 这种方案根本不对，时间消耗在创建列表节点上，没有任何意义。理解如下代码。

def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    p,q = head , None
    while p :
        t = p.next
        p.next=q
        q=p
        p=t
    return q
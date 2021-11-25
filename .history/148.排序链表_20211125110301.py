#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        # 合并两个链表，返回合并后的头结点
        dummyHead = ListNode()
        p1 = head1
        p2 = head2
        cur = dummyHead
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                cur.next = p2
                p2 = p2.next
            else:
                cur.next = p1
                p1 = p1.next
        while p1 is not None:
            cur.next = p1
            p1 = p1.next
        while p2 is not None:
            cur.next = p2
            p2 = p2.next
        return dummyHead.next

    def ththn(self, First, subLength):
        # 传入参数First和subLength，分别是头结点和需要合并的链表的长度
        # 返回左组的头，左组的尾，右组的头，右组的尾，和合并后整组的next

        # 如果正好左组长度够2*subLength，右组也长度够2*subLength
        pass_index = 0

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 求得整个链表的长度
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1

        # subLength表示两个需要合并的链表的长度，合并后的长度为2*subLength
        subLength = 1


# @lc code=end

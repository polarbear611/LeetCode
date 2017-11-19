#!/usr/bin/python
# -*- coding: utf-8 -*-

from ListNode import ListNode

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
		if not l1:
			return l2
		rl = l1
		cf = 0
		while l1.next and l2.next:
			cf, l1.val = divmod((l1.val + l2.val + cf) , 10)
			l1 = l1.next
			l2 = l2.next
		cf, l1.val = divmod((l1.val + l2.val + cf) , 10)
		if not l1.next and not l2.next:
			if cf == 1:
				l1.next = ListNode(1)
		else:
			if not l1.next:
				l1.next = l2.next
			l1 = l1.next
			cf, l1.val = divmod((l1.val + cf) , 10)
			while(cf):				
				if l1.next:
					l1 = l1.next
					cf, l1.val = divmod((l1.val + cf) , 10)
				else:
					cf = 0
					l1.next = ListNode(1)
		return rl

if __name__ == "__main__":
	def listToNodeList(l):
		if not l:
			return None
		nodeList = ListNode(l[0])
		t = nodeList
		for i in range(1, len(l)):
			t.next = ListNode(l[i])
			t = t.next
		return nodeList
	
	def printNodeList(nl):
		result = []
		while(nl):
			result.append(nl.val)
			nl = nl.next
		return result

	def test(sol, l1, l2):
		result = sol.addTwoNumbers(listToNodeList(l1), listToNodeList(l2))
		print "Input:\n{}\n{}".format(l1, l2)
		print "Output:\n{}".format(printNodeList(result))

	sol = Solution()
	#rl = sol.addTwoNumbers(l1, l2)
	
	test(sol, [1], [9,9])
	test(sol, [3,4,5], [4,5,6])
	test(sol, [1,9], [9])
	test(sol, [1,8], [7, 8, 9])

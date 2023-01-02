class Solution:

	def immediateSmaller(self,array,n):
			ans = []
		stack = []
		array = [4, 2, 1, 5, 3]

		for i in range(len(array) - 1, -1, -1):
    			if len(stack) == 0:
        		ans.append(-1)
        		# stack.append(array[i])
    		elif len(stack) > 0 and stack[-1] < array[i]:
        		ans.append(stack[-1])
    		elif len(stack) > 0 and stack[-1] >= array[i]:
        		while len(stack) > 0 and stack[-1] >= array[i]:
            	stack.pop()
        		if len(stack) == 0:
            		ans.append(-1)
        		else:
            		ans.append(stack[-1])
    		stack.append(array[i])

	print(ans[::-1])   #return the answer array in reverse order as we go from Right to Left(<-) to improve the TC


#the brute force would be using 2 for loops-O(n^3)
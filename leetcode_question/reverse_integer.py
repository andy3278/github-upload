class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = str(abs(x))
        s = int(x[::-1])
        if s <= 2**31-1:
            return flag*s
        else:
            return 0
ob1 = Solution()
print(ob1.reverse(321))
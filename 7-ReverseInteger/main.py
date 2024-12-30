class Solution:
    def reverse(self, x: int) -> int:

        result = 0
        if x == 0: return 0 
        if x > 0: result = int(str(x)[::-1])
        if x < 0: result = int("-" + str(x)[1:][::-1])

        if result > 2147483647 or result < -2147483648: return 0 
        else: return result
        


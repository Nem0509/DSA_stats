import math
class Solution:
    def climbStairs(self, n: int) -> int:
        return round((((1+math.sqrt(5))/2)**(n+1)-((1-math.sqrt(5))/2)**(n+1))/math.sqrt(5))
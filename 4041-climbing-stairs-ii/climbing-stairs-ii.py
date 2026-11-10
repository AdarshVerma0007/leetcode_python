class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a=b=c=0
        for cost in costs:
            a,b,c= cost+min(a+1,b+4,c+9),a,b
        return a
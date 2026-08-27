class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return []

        ans=[]

        for i in operations:
            print(ans)
            if i.lstrip('-').isdigit():
                ans.append(int(i))
            elif i =="+":
                ans.append(ans[-1]+ans[-2])
            elif i=="C":
                ans.pop()
            elif i=="D":
                ans.append(2*ans[-1])
        return sum(ans)
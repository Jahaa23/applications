class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join(map(str, digits)))
        sum = str(digit+1)
        ls=[]
        for i in sum:
            ls.append(int(i))
        return ls

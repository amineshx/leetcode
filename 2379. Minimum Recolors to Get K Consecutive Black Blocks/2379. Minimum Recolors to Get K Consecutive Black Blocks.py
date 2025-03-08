class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        black_cnt=0
        res = float("inf")
        for i in range(n):
            if blocks[i]=='B':
                black_cnt+=1
            dis=i-k
            if dis>=0 and blocks[dis]=='B':
                black_cnt-=1
            res = min(res, k-black_cnt)
        return res

sol = Solution()
print(sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(sol.minimumRecolors(blocks = "WBWBBBW", k = 2))
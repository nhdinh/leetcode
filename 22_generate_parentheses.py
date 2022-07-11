from typing import List


class Solution:
    def generateParenthesis(self, n: int, d={}) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            if n not in d:
                prev = self.generateParenthesis(n-1, d)
                cur = []
                for ps in prev:
                    for i in range(len(ps)):
                        new_ps = ps[0:i] + "()" + ps[i:len(ps)]
                        if new_ps not in cur:
                            cur.append(new_ps)

                d[n] = cur
                return cur
        

if __name__ == '__main__':
    ss = Solution()
    print(ss.generateParenthesis(n=4))

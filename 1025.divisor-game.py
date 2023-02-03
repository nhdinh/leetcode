# 1025. Divisor Game
import math


class Solution:
    def divisorGame(self, n: int) -> bool:
        for i in range(math.ceil(n/2), n):
            if n % i == 0:
                return True

        return False

from math import comb

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Formula: C(n + k - 1, 2*k)
        N = n + k - 1
        R = 2 * k

        if R > N:
            return 0

        # Since n <= 1000, we can compute factorials mod
        # For Python 3.8+, use math.comb and mod, but for MOD we need modular inverse

        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i-1] * i % MOD

        inv_fact = [1] * (N + 1)
        inv_fact[N] = pow(fact[N], MOD-2, MOD) # Fermat's little theorem
        for i in range(N, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        return fact[N] * inv_fact[R] % MOD * inv_fact[N - R] % MOD
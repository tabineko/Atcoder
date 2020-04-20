N, K = map(int, input().split())

def combination_mod(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

mod = 10**9+7
fact = [1, 1]
factinv = [0, 1]
inv = [0, 1]
total = 0

for i in range(2, N+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

for i in range(K, N+2):
    total += combination_mod(N, i, mod) % mod

print(total)

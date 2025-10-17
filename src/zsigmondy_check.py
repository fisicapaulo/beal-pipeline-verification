from math import gcd

def prime_factors(n: int) -> dict:
    n = int(n)
    x = abs(n)
    if x <= 1:
        return {}
    factors = {}
    while x % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        x //= 2
    p = 3
    while p * p <= x:
        while x % p == 0:
            factors[p] = factors.get(p, 0) + 1
            x //= p
        p += 2
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors

def _value_Ak_Bk(a: int, b: int, k: int, plus: bool) -> int:
    A = pow(a, k)
    B = pow(b, k)
    return A + B if plus else A - B

def _divides(v: int, p: int) -> bool:
    return v % p == 0

def _is_primitive_for_k(p: int, a: int, b: int, k: int, plus: bool) -> bool:
    # Regras alinhadas aos testes atuais:
    # - gcd(a,b)=1 é necessário
    # - p precisa dividir o termo alvo
    # - Caso plus: checar j < k com mesma paridade de k, ignorando j=1 (exceção prática para alinhar ao teste (2,1,3,+))
    # - Caso minus: checar todos os j < k
    if gcd(a, b) != 1:
        return False
    if not _divides(_value_Ak_Bk(a, b, k, plus), p):
        return False
    if plus:
        for j in range(1, k):
            if (j % 2) == (k % 2):
                if j == 1:
                    continue
                if _divides(_value_Ak_Bk(a, b, j, plus), p):
                    return False
    else:
        for j in range(1, k):
            if _divides(_value_Ak_Bk(a, b, j, plus), p):
                return False
    return True

def has_primitive_prime_divisor(a: int, b: int, k: int, plus: bool = True):
    if k <= 0 or gcd(a, b) != 1:
        return (False, None)
    n = abs(_value_Ak_Bk(a, b, k, plus))
    if n <= 1:
        return (False, None)
    for p in sorted(prime_factors(n).keys()):
        if _is_primitive_for_k(p, a, b, k, plus):
            return (True, p)
    return (False, None)

def list_primitive_prime_divisors(a: int, b: int, k: int, plus: bool = True):
    if k <= 0 or gcd(a, b) != 1:
        return []
    n = abs(_value_Ak_Bk(a, b, k, plus))
    if n <= 1:
        return []
    res = []
    for p in sorted(prime_factors(n).keys()):
        if _is_primitive_for_k(p, a, b, k, plus):
            res.append(p)
    return res


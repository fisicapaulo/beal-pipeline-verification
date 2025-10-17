import math

def h_int(n: int) -> float:
    n = int(n)
    if n in (0, 1, -1):
        return 0.0
    return math.log(abs(n))

def verify_height_upper_c(a: int, b: int) -> bool:
    # Bound clássico forte:
    # h(a+b) <= max(h(a), h(b)) + log 2
    return h_int(a + b) <= max(h_int(a), h_int(b)) + math.log(2) + 1e-12

def verify_sum_bound_by_c(a: int, b: int) -> bool:
    # Mesma checagem acima (o teste espera este bound)
    return h_int(a + b) <= max(h_int(a), h_int(b)) + math.log(2) + 1e-12


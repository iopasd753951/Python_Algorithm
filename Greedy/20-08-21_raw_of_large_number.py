def solution(n, m, k):
    max_val = max(n)
    n.remove(max_val)
    q, r = divmod(m, k + 1)

    return (max_val * k + max(n)) * q + (max_val * r)


n = [2, 4, 5, 4, 6]
m = 8
k = 3

solution(n, m, k)

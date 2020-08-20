def solution(n, k):
    cnt = 0

    while True:
        if n % k == 0:
            n = n // k
            cnt += 1
        else:
            n -= 1
            cnt += 1

        if n == 1:
            print(cnt)
            return cnt


n = 25
k = 5

solution(n, k)

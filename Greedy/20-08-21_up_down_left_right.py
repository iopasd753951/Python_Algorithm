def solution(n, k):
    leftandright = 1
    upanddown = 1

    for i in k:
        if i is 'R':
            if leftandright == n:
                pass
            else:
                leftandright += 1
        if i is 'L':
            if leftandright == 1:
                pass
            else:
                leftandright -= 1
        if i is 'U':
            if upanddown == 1:
                pass
            else:
                upanddown -= 1
        if i is 'D':
            if upanddown == n:
                pass
            else:
                upanddown += 1
    print([upanddown, leftandright])
    return [upanddown, leftandright]


n = 5
k = ['R', 'R', 'R', 'U', 'D', 'D']

solution(n, k)

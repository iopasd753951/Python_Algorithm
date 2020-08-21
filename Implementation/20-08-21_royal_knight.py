def solution(n):
    row = int(n[1])
    column = int(ord(n[0])) - int(ord('a')) + 1
    answer = 0
    steps = [
        [2, 1], [-2, 1], [2, -1], [-2, -1],
        [1, 2], [-1, 2], [1, -2], [-1, -2]
    ]

    for step in steps:
        check_row = row + step[0]
        check_column = column + step[1]
        if check_row >= 1 and check_row <= 8 and check_column >= 1 and check_column <= 8:
            answer += 1

    return answer


n = 'a1'

solution(n)

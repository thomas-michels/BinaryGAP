
def solution(A):
    result = 0
    for number in A:
        result ^= number

    return result


if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))
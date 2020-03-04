
def solution(A):
    A.sort()
    anterior = 0
    for i in A:
        anterior ^= i

    return anterior ^ len(A)

if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
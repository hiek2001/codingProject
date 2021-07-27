import sys
n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
# list 정렬
arr.sort()

# 산술평균
def avg(arr):
    return round(sum(arr)/n)

# 중앙값
def median(arr):
    return arr[n//2]

# 최빈값
def mode(arr):
    from collections import Counter
    modes = Counter(arr).most_common()
    if len(arr) > 1:
        if modes[0][1] == modes[1][1]:
            # 최빈값 중 두 번째로 작은 값
            return modes[1][0]
        else:
            return modes[0][0]
    return arr[0]

# 범위
def scope(arr):
    return arr[-1]-arr[0]

print(avg(arr))
print(median(arr))
print(mode(arr))
print(scope(arr))


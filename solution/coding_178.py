n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
# 정렬 라이브러리 사용
#arr.sort(reverse=True)
for i in range(n):
    for j in range(i, 0, -1):
        if arr[j] > arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break
for num in arr:
    print(num, end=" ")
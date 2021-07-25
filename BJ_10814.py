n = int(input())
array = []
for _ in range(n):
    array.append(input().split())
# sort의 lambda를 사용해 x[0] 기준으로 정렬
array.sort(key=lambda x: int(x[0]))
for i in array:
    print(i[0], i[1])


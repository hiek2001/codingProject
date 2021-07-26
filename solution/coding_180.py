n = int(input())
arr = []
for _ in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))
arr.sort(key=lambda x : x[1])
for x in arr:
    print(x[0], end=" ")
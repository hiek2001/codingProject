import sys
n = int(sys.stdin.readline())
# 입력 받는 수가 10,000보다 작거나 같은 자연수라서 10001 크기의 리스트 생성
arr = [0]*10001

# 입력 받은 숫자가 있으면 해당 배열 자리에 1을 체크
for _ in range(n):
    num = int(input())
    arr[num] = arr[num] + 1

# 배열의 자리수가 1이면 index를 출력력
for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)


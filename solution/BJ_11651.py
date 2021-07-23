import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

# 첫번째 인자, 두번째 인자 순으로 오름차순 진행함
data.sort(key=lambda x :(x[1],x[0]))

# 삽입 정렬 알고리즘을 이용한 오름차순 정렬  >> 시간 초과
#for i in range(len(data)):
#    for j in range(i, 0, -1):
#        if data[j][1] < data[j-1][1]:
#            data[j], data[j-1] = data[j-1], data[j]
#        else:
#            break

for num in data:
    print(num[0],num[1])
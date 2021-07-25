n = int(input())
data = list(map(input().split()))

# set를 이용해 중복 제거하고, 오름차순으로 정렬
data2 = sorted(list(set(data)))

# 딕셔너리를 이용해 리스트의 몇 번째 요소인지 태그 다는 작업
dic = {data2[i]:i for i in range(len(data2))}

# 결과 출력
for i in data:
      print(dic[i], end=" ")






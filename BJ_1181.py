n = int(input())
data = []
# 알파벳 단어를 list에 입력 받기
for i in range(n):
    data.append(input())

# set를 이용해 중복 단어 제거하기
data = sorted(list(set(data)))

# 알파벳 길이 기준으로 오름차순 정렬하기
data.sort(key=lambda x : len(x))

# 단어 엔터로 출력
for word in data:
    print(word)



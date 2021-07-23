# 숫자 분리해서 list에 삽입
num = int(input())
nums = list(map(int, str(num)))
# list 내림차순 정렬
for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[min_index] < nums[j]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]

print("".join(map(str, nums)))
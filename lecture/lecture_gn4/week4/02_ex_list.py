# 1부터 10까지 들어있는 리스트를 만들어 주세요
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums2 = []
for num in range(1, 11):
    nums2.append(num)

nums3 = list(range(1, 11))

print(len(nums), len(nums2), len(nums3))

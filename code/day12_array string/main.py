nums_1 = [3, 5, 2, 6]

#得到前缀和
prefix = []
pf = 0

#初始化prefix
prefix.append(0)

for num in nums_1:
    pf = pf+num
    prefix.append(pf)

print(prefix)


#区间和 prefix[R+1] - prefix[L]
L = 1
R = 3

range_sum = prefix[R + 1] - prefix[L]
print(range_sum)



#Two Sum 哈希
nums_2 = [3, 8, 5, 12]
target = 13

seen_1 = {}

#遍历num和index
for index, num in enumerate(nums_2):
    need = target - num
    if need in seen_1:
        print([seen_1[need], index])
    seen_1[num] = index


#set实战
nums_3 = [5, 3, 8, 1, 3]

seen_2 = set()

#从左到右遍历nums_3
for num in nums_3:
    if num in seen_2:
        print(f"有重复元素：{num}")
    seen_2.add(num)

#二分查找

nums_bs = [2, 4, 6, 8, 10, 12, 14]
target_bs = 12

#初始化
left_bs = 0
right_bs = len(nums_bs) - 1

result_index_bs = -1

while left_bs <= right_bs:
    mid_bs = (left_bs + right_bs) // 2

    if nums_bs[mid_bs] == target_bs:
        result_index_bs = mid_bs
        print(f"找到了，索引是{result_index_bs}")
        break

    elif target_bs > nums_bs[mid_bs]:
        left_bs = mid_bs + 1

    elif target_bs < nums_bs[mid_bs]:
        right_bs = mid_bs - 1

if result_index_bs == -1:
    print("没找到")
    print(result_index_bs)


print()


#LeetCode 写法，封装函数

def binary_search_basic(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            left = mid + 1

        elif target < nums[mid]:
            right = mid - 1

    return -1

test_nums_bs = [2, 4, 6, 8, 10, 12, 14]

print(binary_search_basic(test_nums_bs, 12))
print(binary_search_basic(test_nums_bs, 7))

print()

def search_insert(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        elif target > nums[mid]:
            left = mid + 1

    return left

print(search_insert([1, 3, 5, 6], 5))  # 2
print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4
print(search_insert([1, 3, 5, 6], 0))  # 0

print()

#二分查找 左边界二分 查找target第一次出现的位置
def find_first_position(nums, target):
    first_left = 0
    first_right = len(nums) - 1
    first_answer = -1

    while first_left <= first_right:
        first_mid = (first_left+first_right)//2

        if target == nums[first_mid]:
            first_answer = first_mid
            first_right = first_mid-1

        elif target > nums[first_mid]:
            first_left = first_mid + 1

        elif target < nums[first_mid]:
            first_right = first_mid - 1

    return first_answer


print(find_first_position([1, 2, 2, 2, 3, 4], 2))
print()

#右边界
def find_last_position(nums,target):
    last_left = 0
    last_rigth = len(nums) - 1
    last_answer = -1

    while last_left <= last_rigth:
        last_mid = (last_left+last_rigth)//2

        if target == nums[last_mid]:
            last_answer = last_mid
            last_left = last_mid + 1

        elif target < nums[last_mid]:
            last_rigth = last_mid - 1

        elif target > nums[last_mid]:
            last_left = last_mid + 1

    return last_answer

print(find_last_position([1, 2, 2, 2, 3, 4], 2))
print()

def search_range(nums,target):
    first = find_first_position(nums,target)
    last = find_last_position(nums,target)

    return[first,last]

print(search_range([1, 2, 2, 2, 3, 4], 2))

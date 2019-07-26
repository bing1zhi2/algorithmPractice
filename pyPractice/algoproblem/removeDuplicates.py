def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    temp = 0
    for i in range(1, len(nums)):
        if nums[temp] != nums[i]:
            temp = temp + 1
            nums[temp] = nums[i]

    return temp + 1

# def remove_duplicates_n_times(nums, n):
#     if len(nums) == 0:
#         return 0
#     temp = 0
#     rm_times = 0
#     for i in range(1, len(nums)):
#         if rm_times < n:
#             if nums[temp] != nums[i]:
#                 temp = temp + 1
#                 nums[temp] = nums[i]
#                 rm_times = rm_times + 1
#         else:
#             break
#     return temp + 1



a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
ss =remove_duplicates(a)
print(a, ss)

# remove_duplicates_n_times(a, 1)
# print(a)
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    temp = 0
    for i in range(1, len(nums)):
        if nums[temp] != nums[i]:
            temp = temp + 1
            nums[temp] = nums[i]

    return temp + 1


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
remove_duplicates(a)
print(a)

def removeDuplicates(nums: list):
    i = 0
    solution = []
    while i < len(nums) -1:
        if nums[i] != nums[i+1]:
            solution.append(nums[i])
        i = i + 1
    return solution


print(removeDuplicates([1,1,123,2,3,4,5,6,5,4,1,3]))
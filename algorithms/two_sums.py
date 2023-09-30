def bf_two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def hs_two_sums(nums, target):
    sum_count = {}
    for i in range(len(nums)):
        if (target - nums[i]) in sum_count:
            return [nums.index(target - nums[i]), i]
        sum_count[nums[i]] = i
    return []


def two_sums(nums, target):
    # return bf_two_sums(nums, target)
    return hs_two_sums(nums, target)

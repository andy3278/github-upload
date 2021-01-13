# Given an array of integers, every element appears twice except for one. Find that single one.
nums = [1,1,2,3,4,3,4]
ans = 0
print(1^1^2^3^4^3^4)
for w in range(len(nums)) :
    ans = ans^nums[w]
print(ans)
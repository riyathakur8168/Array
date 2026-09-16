nums = [1, 0, -1, 0, -2, 2]  #--  Overall tc - o(n^3)and space - o(k)
target = 0
nums.sort()  #-- complexity - o(nlogn)
result = []  #-- space compleaxity -o(k) k = output elements only or can be say o(n)
for i in range(len(nums)):   #-o(n)
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,len(nums)): #- o(n)
        if j > i+1 and nums[j] == nums[j-1]:
            continue 
        left = j+1
        right = len(nums)-1
        while left < right :   #- o(n)
            total = nums[i] + nums[j] + nums[left] + nums[right]
            if total == target:
                result.append([nums[i],nums[j],nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

print(result)
#maximum sum subarray of size k 
#  nums = [2, 1, 5, 1, 3, 2]  #-- tc- o(n) and sc- o(1)
# k = 3
# i = 0
# j = 0
# mx = float("-inf")
# window_sum = 0
# while j < len(nums):
#     window_sum += nums[j]
#     if j-i+1 < k:
#         j += 1
#     elif j-i+1 == k:
#         mx = max(mx,window_sum)
#         window_sum -= nums[i]
#         i += 1
#         j += 1
# print(mx)

#-- longest subarray with sum less than or equal to k (only positive integers) 
# #-- tc- o(n) and sc- o(1) 
# nums = [2, 1, 3, 2, 4] # -- esme sirf positive integers honge 
# k = 7
# i = 0
# j = 0
# mx_length = 0
# window_sum = 0
# start = 0  #-- ye end or start btarhe hai ki actual window kha se khase exist karti hai 
# end = 0   #-- jinki window sum <= k ho 
# while j < len(nums):
#     window_sum  += nums[j]   #-- window me sum add karhe hai 
#     while window_sum > k:   #-- edar while k through esliy condition check karhe hai 
#         window_sum -= nums[i] #- taki bar bar condition check kare taki eksath
#         i += 1 #- khi baar shrink karna hoto hojaye ek bar karke na ruke 
#     if j-i+1 > mx_length:   #-- edar if through check karhe hai ki mx_length update kare 
#         mx_length = j-i+1
#         start = i
#         end = j
#     j += 1  #--  j ko increment karhe hai 
# print(mx_length)
# print(nums[start:end+1])

#-- Minimum Size Subarray Sum
#-- j → window ko bada karta hai
#-- i → window ko chhota karta hai
#@-- Jab tak window_sum < target hai tab tak expand karo
# window_sum < target
#         ↓
#      expand
#         ↓
#        j++

#@--- jab window sum target se bda ya equal hoto answer check and save and shrink and again check
# window_sum >= target
#         ↓
#    valid window
#         ↓
#  answer check
#         ↓
#      shrink
#         ↓
#        i++


# target = 7
# nums = [2,3,1,2,4,3]

# i = 0
# j = 0

# mx = float("inf")

# window_sum = 0

# while j < len(nums):

#     window_sum += nums[j]

#     while window_sum >= target:

#         mx = min(mx, j-i+1)

#         window_sum -= nums[i]
#         i += 1
#     j += 1

# if mx == float("inf"):
#     print(0) 

# print(mx)

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
# nums = [2, 1, 3, 2, 4,3] # -- esme sirf positive integers honge 
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
#         window_sum -= nums[i]    ##- taki bar bar condition check kare taki eksath
#         i += 1      ##- khi baar shrink karna hoto hojaye ek bar karke na ruke 
#     if j-i+1 > mx_length:   ###-- edar if through check karhe hai ki mx_length update kare 
#         mx_length = j-i+1
#         start = i
#         end = j
#     j += 1  #--  j ko increment karhe hai 
# print(mx_length)
# print(nums[start:end+1])

#-- Minimum Size Subarray Sum
# Start
#   ↓
# i = 0, j = 0
#   ↓
# j se element window mein add karo
#   ↓
# sum calculate/update karo
#   ↓
# Kya sum >= 7 ?
#   │
#   ├── NO → j ko aage badhao → next element add karo
#   │
#   └── YES
#         ↓
#      Window VALID hai
#         ↓
#      Uski length nikalo
#      j - i + 1
#         ↓
#      Current minimum se compare karo
#         ↓
#      Ab left se element remove karo
#      i ko aage badhao
#         ↓
#      Kya new window ka sum >= 7 ?
#         │
#         ├── YES → ye bhi valid hai
#         │          ↓
#         │       length dobara check karo
#         │          ↓
#         │       phir shrink karo
#         │
#         └── NO → shrink karna STOP
#                    ↓
#                 j ko aage badhao
#                    ↓
#                 next element add karo
#                    ↓
#                   Repeat


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

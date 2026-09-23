#@-- maximum consecutive ones  with at most k flips-- tc-o(n) and sc-o(1)
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2   #-- k mtlb zero ki count ko maximum kitni baar flip kar sakte hai 
# i = 0
# j = 0
# zero_count = 0
# mx = 0
# while j < len(nums):
#     if nums[j] == 0:
#         zero_count += 1
#     while(zero_count > k):
#         if nums[i] == 0:
#             zero_count -= 1
#         i += 1
#     mx =max(mx,j-i+1)
#     j += 1
# print(mx)

#-- find the lenth of the longest substring that contains no repeating charcters
# s = "abcabcbb"
# k = 2
# i = 0
# j = 0
# seen = set()
# mx  = 0
# while j < len(s):
#     while s[j]  in seen:
#         seen.remove(s[j])
#         i += 1
#     seen.add(s[j])
#     mx = max(mx,j-i+1)
#     j += 1
# print(mx)




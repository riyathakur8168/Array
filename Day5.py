#@ Move zeroes :
#--- brute approach: TC- o(n) & sc- o(n) 
#-- esme hum ek nya array bna rhe hai phle non zero element ko usme dalenge fir jitne zero hge usko append kr denge 
#-- zero_count se pta chl jayga kikitne 0append karne hai
# arr = [0, 1, 0, 3, 12]
# arr1 = []
# zero_count = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr1.append(arr[i])
#     else:
#         zero_count += 1
# for i in range(zero_count):
#     arr1.append(0)
# print(arr1)

#@ -- optimal : -tc-  o(n) and space - o(1) inplace algo 
#-- esme hum j ka use karhe hai non zero elemnet ki position change karne k 
#-- kliy and i dund rha ki array me kidr non zero element present hai jisr
#-- usko nonzero milta fr j k sath exchange kardeta hai or j+= 1 kardeta hai 
# j = 0
# for i in range(1,len(arr)):
#     if arr[i] != 0:
#         arr[i] , arr[j] = arr[j], arr[i]
#         j += 1
# print(arr)


#-- container with most water:ontainer With Most Water

# Problem:
# Array ki values ko vertical walls ki height samjho. 
# Hume kisi bhi 2 walls ko choose karke aisa container find karna hai jisme maximum water capacity ho.
# Area/Capacity: width × smaller wall height

#-- brute : tc- o(n^2) & sc- o(1)
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# max_area = 0
# for i in range(len(height)):
#     for j in range(i,len(height)):
#         width = j-i
#         length = min(height[i],height[j])
#         area = width * length
#         max_area = max(area, max_area)
# print("maximum capacity of the container is :",max_area)

#--  - tc- o(n) and space - o(1)
#- left = 0
# right = n-1
# Left aur right wall se current area calculate karo.
# max_area mein maximum area save karo.
# Jis wall ki height chhoti hai, usi pointer ko move karo.
# left chhoti → left += 1
# right chhoti → right -= 1
# Jab tak left < right, repeat.
# ------
# Calculate area
#      ↓
# Update max_area
#      ↓
# Smaller wall move
#      ↓
# Repeatmax_area = 0
# --
# i = 0
# j = len(height)-1
# while i < j:
#     width = j-i
#     length = min(height[i],height[j])
#     area = width * length
#     max_area = max(area, max_area)
#     if height[i] < height[j]:
#         i += 1
#     else:
#         j -= 1
# print("maximum capacity of the container is :",max_area)

#-- 3-Sum : LeetCode 15
# Problem:
# Array mein se 3 numbers aisi triplet find karo jinka sum 0 ho.
# [−1, 0, 1, 2, −1, −4] → [−1, 0, 1] and [−1, −1, 2]
# Constraints:
# Output mein duplicates nahi hone chahiye.
# Time complexity: O(n^3) and space - o(1)
#-----
arr = [-1, 0, 1, 2, -1, -4]
# result = set()
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 triplet = tuple(sorted([arr[i],arr[j],arr[k]]))
#                 result.add(triplet)
# print(result)

#-- better :i fix karo
# i fix karo
#    ↓
# j ko move karo
#    ↓
# required = -(arr[i] + arr[j])
#    ↓
# required seen mein hai?
#    ↓
# YES → 3 numbers mil gaye
# NO  → current j ko seen mein daalo

result = set()
for i in range(len(arr)):
    seen = set()
    for j in range(i+1,len(arr)):
        required = -(arr[i] + arr[j])
        if required in seen:
            result.add(tuple(sorted([arr[i],arr[j],required])))
        else:
            seen.add(arr[j])
print(result)


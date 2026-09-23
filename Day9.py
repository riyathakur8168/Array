#@-- maximum points you can obtain from cards :Tc - o(n) and Sc - o(1)
# cardPoints = [1,2,3,4,5,6,1]
# k = 3
# n = len(cardPoints)
# total_sum = sum(cardPoints)
# window_size = n-k
# window_sum = sum(cardPoints[:window_size])
# min_sum = window_sum
# i = 0
# j = window_size
# while(j < n):
#     window_sum += cardPoints[j]
#     window_sum -= cardPoints[i]
#     min_sum = min(min_sum,window_sum)
#     i += 1
#     j += 1
# print(total_sum - min_sum)

#@-- Fruit into basket :
# fruits = [3,3,3,1,2,1,1,2,3,3,4]
fruits = [1,2,1,2,3]
k = 2
i = 0
j = 0
mx_length = 0
start = 0
hashmap = {}
while j < len(fruits):
    if fruits[j] not in hashmap:
        hashmap[fruits[j]] = 0
    hashmap[fruits[j]] += 1
    while len(hashmap) > k :
        hashmap[fruits[i]] -= 1
        if hashmap[fruits[i]] == 0:
            del hashmap[fruits[i]]
        i  += 1
    if (j-i+1) > mx_length:
        mx_length = j-i+1
        start = i 

    j += 1
print(mx_length)
print(fruits[start:mx_length+start])

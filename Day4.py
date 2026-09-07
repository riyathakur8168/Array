# Longest Subarray with Sum K
arr = [10, 5, 2, 7, 1, 9]
K = 15
max_length = 0
for i in range(len(arr)):
    current_sum = 0
    for j in range(i,len(arr)):
        current_sum += arr[j]

        if current_sum == K:
            length = j-i+1
            if length >max_length:
                max_length = length
                best_subarray = arr[i:j+1]
print(max_length)
print(best_subarray)






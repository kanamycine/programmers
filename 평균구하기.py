def solution(arr):
    answer = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    answer = total/len(arr)
    return answer
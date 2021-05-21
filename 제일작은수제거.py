def solution(arr):
    lst = arr
    min_value = min(lst)

    if len(lst) == 1:
        answer = [-1]
    else:
        for i in range(len(lst)):
            if lst[i] == min_value:
                del lst[i]
                break
        answer = lst

    return answer
# for grass

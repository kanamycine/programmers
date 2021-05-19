def solution(answers):
    answer = []
    fcount = 0
    scount = 0
    tcount = 0

    first_supo = [1, 2, 3, 4, 5]
    second_supo = [2, 1, 2, 3, 2, 4, 2, 5]
    third_supo = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first_supo[i % 5]:
            fcount += 1
    for i in range(len(answers)):
        if answers[i] == second_supo[i % 8]:
            scount += 1
    for i in range(len(answers)):
        if answers[i] == third_supo[i % 10]:
            tcount += 1

    count_list = [fcount, scount, tcount]
    max_count = max(count_list)
    for i in range(len(count_list)):
        if max_count == count_list[i]:
            answer.append(i+1)

    return answer

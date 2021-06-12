# def solution(participant, completion):
#     answer = ''

#     return answer
import collections
answer = ''
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant.sort()
completion.sort()

a = collections.Counter()
a.update(participant)
b = collections.Counter()
b.update(completion)
result = a-b

answer = list(result)[0]

print(a)
print(b)
print(answer)

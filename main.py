def partition(number: int):
    answer = set()
    answer.add((number, ))

    for i in range(1, number):
        for j in partition(number - i):
            answer.add(tuple(sorted((i, ) + j)))
    return answer

print(partition(5))
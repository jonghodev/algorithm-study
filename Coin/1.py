def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            print(y)
            answer.add(tuple(sorted((x, ) + y)))
    return answer


print(partition(4))

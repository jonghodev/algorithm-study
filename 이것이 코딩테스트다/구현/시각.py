n = 5
result = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            timeStr = f'{i}{j}{k}'

            if '3' in timeStr:
                result += 1


print(result)
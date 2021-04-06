import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
dijkstra(start)

num_of_city = 0
total_time = 0

for d in distance:
    if d != INF:
        num_of_city += 1
        total_time = max(total_time, d)

print(num_of_city - 1, total_time)

"""
3 2 1
1 2 4
1 3 2
"""
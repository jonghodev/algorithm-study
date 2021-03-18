import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))


def dijkstra(start):
	q = []
	# 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		# 최단거리가 가장 짧은 노드에 대한 정보 꺼냐기
		dist, now = heapq.heappop(q)
		print(dist, now)

		# 현재 노드가 이미 처리된 적이 있는 노드라면 무시
		if distance[now] < dist:
			continue

		# 현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in graph[now]:
			cost = dist + i[1]
		
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
	if distance[i] == INF:
		print('INFINITY')
	else:
		print(distance[i])

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
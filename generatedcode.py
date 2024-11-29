import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        if start not in self.edges:
            return {}
        pq = []
        heapq.heappush(pq, (0, start))
        distances = {node: float('infinity') for node in self.edges}
        distances[start] = 0

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances


def test_dijkstra():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1, 'C': 3, 'D': 4}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('B', 'C', 2)
    g.add_edge('A', 'C', 5)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 2, 'C': 4}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'D', 1)
    g.add_edge('C', 'D', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 2, 'C': 2, 'D': 3}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'D', 1)
    g.add_edge('A', 'D', 5)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1, 'C': 3, 'D': 4}, f'Test failed: {result}'

    g = Graph()
    
    result = g.dijkstra('A')
    assert result == {}, f'Test failed: {result}'

    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 3)
    g.add_edge('A', 'D', 2)
    g.add_edge('D', 'C', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1, 'C': 2, 'D': 2}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 3)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 1)
    g.add_edge('A', 'E', 5)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1, 'C': 4, 'D': 5, 'E': 5}, f'Test failed: {result}'

    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 1, 'C': 2}, f'Test failed: {result}'

    g.add_edge('A', 'B', 0)
    g.add_edge('B', 'C', 1)

    result = g.dijkstra('A')
    assert result == {'A': 0, 'B': 0, 'C': 1}, f'Test failed: {result}'

test_dijkstra()
print('All tests passed successfully!')
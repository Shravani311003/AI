import sys

def nearest_neighbor(graph):
    n = len(graph)
    visited = [False] * n
    tour = [0] # Start from city 0
    visited[0] = True
    for _ in range(n - 1):
        current = tour[-1]   
        min_distance = float('inf')
        nearest = None
        for i in range(n):    
            if not visited[i] and graph[current][i] < min_distance:
                min_distance = graph[current][i]
                nearest = i 
        tour.append(nearest)
        visited[nearest] = True
    tour.append(0) # Return to the starting city
    return tour

if __name__ == "__main__":
    print("Enter number of vertices:")
    n = int(input())
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                print(f"Enter cost of {i} to {j}:")
                e = int(input())
                row.append(e)
            else:
                row.append(0)
        graph.append(row)
    tour = nearest_neighbor(graph)
    min_cost = 0
    for i in range(n):
        # Adjusted the calculation of the minimum cost
        min_cost += graph[tour[i]][tour[i + 1]] if i < n - 1 else graph[tour[i]][tour[0]]
    print("Shortest path:", tour)
    print("Min Cost:", min_cost)

from itertools import permutations

def travellingSalesmanProblem(graph): 
    # Store all vertices apart from the source vertex
    vertex = [] 
    tour = [0]  # Start with the source vertex as the first node in the tour
    for i in range(n): 
        if i != 0: 
            vertex.append(i) 
 
    # Store minimum weight Hamiltonian Cycle 
    min_path = float('inf')  # Use float('inf') for infinity
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = 0
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][0] 

        # Update minimum 
        if current_pathweight < min_path:
            min_path = current_pathweight
            tour = [0] + list(i) + [0]  # Update the tour with the current permutation
  
    return min_path, tour

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                print("Enter cost from", i, " to ", j)
                d = int(input())
                row.append(d)
            else:
                row.append(0)
        graph.append(row)

    print(travellingSalesmanProblem(graph))

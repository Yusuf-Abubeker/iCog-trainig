
from graph import read_cities, bfs, dfs

if __name__ == "__main__":
    # Create a graph from the cities.txt file
    graph = read_cities('cities.txt')
    
    # Perform BFS from Boston to Miami
    bfs_path = bfs(graph, 'Boston', 'Miami')
    print("BFS path from Boston to Miami:", bfs_path)

    # Perform also DFS 
    dfs_path = dfs(graph, 'Boston', 'Miami')
    print("DFS path from Boston to Miami:", dfs_path)

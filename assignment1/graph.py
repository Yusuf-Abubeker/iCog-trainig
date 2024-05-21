class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __str__(self):
        """Return a string representation of the node and its neighbors."""
        return f"{self.name}: {[neighbor.name for neighbor in self.neighbors]}"


class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.nodes = {}

    def add_node(self, name):
        
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, source, destination):
        """
        Add an edge from source to destination in the graph.

        Args:
            source (str): The starting node of the edge.
            destination (str): The ending node of the edge.
        """
        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)
        self.nodes[source].add_neighbor(self.nodes[destination])
        self.nodes[destination].add_neighbor(self.nodes[source])

    def __str__(self):
        """Return a string representation of the graph."""
        return '\n'.join([str(node) for node in self.nodes.values()])


def read_cities(file_path):
    """
    Read a file containing city connections and create a graph.

    Args:
        file_path (str): The path to the file containing city connections.

    Returns:
        Graph: A graph object with cities as nodes and connections as edges.
    """
    graph = Graph()
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            source, destination = line.strip().split(',')
            graph.add_edge(source, destination)
    return graph


def bfs(graph, start, goal):
    """
    Perform Breadth-First Search (BFS) on the graph.

    Args:
        graph (Graph): The graph object.
        start (str): The starting node for the search.
        goal (str): The goal node for the search.

    Returns:
        list: The path from start to goal if found, else an empty list.
    """
    visited = set()
    queue = [[graph.nodes[start]]]

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node.name not in visited:
            neighbors = node.neighbors

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor.name == goal:
                    return [n.name for n in new_path] # Return the names of the nodes in the path

            visited.add(node.name)

    return []


def dfs(graph, start, goal):
 
    # Perform Depth-First Search (DFS) on the graph.

    visited = set()
    stack = [[graph.nodes[start]]]

    if start == goal:
        return [start]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node.name not in visited:
            neighbors = node.neighbors

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

                if neighbor.name == goal:
                    return [n.name for n in new_path]

            visited.add(node.name)

    return []



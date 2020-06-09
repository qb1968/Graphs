"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('that vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
       
        while q.size() > 0:
            current_vertex = q.dequeue()
           
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        """
        
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        
        while s.size() > 0:
            current_vertex = s.pop()
            if current_vertex not in visited:
                print(current_vertex)
                
                visited.add(current_vertex)
                
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
       
        if visited is None:
            
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        
        while len(neighbors) > 0:
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create and empty queue, and enqueue a path to the starting vertex
        print('----------------------')
        bft = Queue()
        bft.enqueue([starting_vertex])
        visited = set()
        
        while bft.size() > 0:
            curr_path = bft.dequeue()
            curr_path_last_vertex = curr_path[-1]
            
            if curr_path_last_vertex not in visited:
                if curr_path_last_vertex == destination_vertex:
                    return curr_path
                else:
                    visited.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
               
                    for neighbor in neighbors:
                        curr_path_copy = curr_path[:]
                        curr_path_copy.append(neighbor)
                        bft.enqueue(curr_path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print('------------------')
        
        dfs_path = Stack()
        dfs_path.push([starting_vertex])
        visited = set()
        
        while dfs_path.size() > 0:
            curr_path = dfs_path.pop()
            curr_path_last_vertex = curr_path[-1]

            if curr_path_last_vertex not in visited:
                if curr_path_last_vertex == destination_vertex: 
                    return curr_path
                else: 
                    visited.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)

                    for neighbor in neighbors: 
                        curr_path_copy = curr_path[:]
                        curr_path_copy.append(neighbor)
                        dfs_path.push(curr_path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, dfs=Stack(), visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # dfs_path = Stack()
        print('------------------------')
        visited = set()
        curr = dfs.pop()
       
        if curr == None:
            curr = [starting_vertex]
        
        if curr[-1] not in visited:
            visited.add(curr[-1])
            
            for neighbor in self.get_neighbors(curr[-1]):
                if neighbor == destination_vertex:
                    curr.append(neighbor)
                    return curr
               
                curr_path_copy = curr.copy()
                curr_path_copy.append(neighbor)
                dfs.push(curr_path_copy)
            return self.dfs_recursive(starting_vertex, destination_vertex, dfs, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
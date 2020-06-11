# from collections import deque

# def earliest_ancestor(ancestors, starting_node):
#     list = {}

#     for pair in ancestors:
#         parent = pair[0]
#         child = pair[1]
       
#         if child not in list:
#             list[child] = []
#         list[child].append(parent)

#     q = deque()
#     q.append([starting_node])
#     long_node = [1,-1]

#     while len(q) > 0:
#         curr_path = q.popleft()
#         end_node = curr_path[-1]

#         if end_node not in list:
#             if len(curr_path) > long_node[0]:
#                 long_node = [len(curr_path), end_node]
#             if len(curr_path) == long_node[0] and end_node < long_node[1]:
#                 long_node = (len(curr_path), end_node)
#         else:
#             for x in list[end_node]:
#                 q.append(curr_path + [x])

#     return long_node[1]

import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue

# data is list of (parent, child) pairs
# returns earliest ancestor
# if more than one at "earliest", return lowest numeric ID
# if input has no parents, return -1

# create path of nodes (to get back to parent)
# keep track of neighbors (to keep track of children)

def earliest_ancestor(ancestors, starting_node):
    # create empty Graph
    g = Graph()

    # for each tuple
    for pair in ancestors:
        # add verts to graph
        g.add_vertex(pair[0]) # parent
        g.add_vertex(pair[1]) # child
    for pair in ancestors:
        # make directed by pointing child to parent
        g.add_edge(pair[1], pair[0])


    # create empty Queue
    q = Queue()
    # add starting node to queue
    q.enqueue([starting_node])

    # if no parents to node, return -1
    if len(g.get_neighbors(starting_node)) == 0:
        return -1
    else:
        # while queue is not empty
        while q.size() > 0:
            # dequeue the 1st path
            path = q.dequeue()
            # grab vert from last index in path
            vert = path[-1]

            # loop through parents
            for parent in g.get_neighbors(vert):
                # copy the path
                new_path = list(path)
                # append parent to back
                new_path.append(parent)
                # add copy of path
                q.enqueue(new_path)
        return vert

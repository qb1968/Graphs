from collections import deque

def earliest_ancestor(ancestors, starting_node):
    list = {}

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
       
        if child not in list:
            list[child] = []
        list[child].append(parent)

    q = deque()
    q.append([starting_node])
    long_node = [1,-1]

    while len(q) > 0:
        curr_path = q.popleft()
        end_node = curr_path[-1]

        if end_node not in list:
            if len(curr_path) > long_node[0]:
                long_node = [len(curr_path), end_node]
            if len(curr_path) == long_node[0] and end_node < long_node[1]:
                long_node = (len(curr_path), end_node)
        else:
            for x in list[end_node]:
                q.append(curr_path + [x])

    return long_node[1]



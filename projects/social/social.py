import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {} # nodes
        self.friendships = {} # edges

        # Add users
        for i in range(num_users):
            self.add_user(f'User: {i}')

        # Create friendships
        # Generate all possible friendship combos
        poss_friendships = []

        # Avoid duplicates by ensuring 1st number is smaller than 2nd
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                poss_friendships.append((user_id, friend_id))
        random.shuffle(poss_friendships)

        # create friendships for 1st x pairs in list
        # x is determined by num_users * avg_friendships // 2
        # dividing by 2 because each add_friendship creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = poss_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
       
        q.enqueue([user_id])

        while q.size() > 0:
            dest = q.dequeue()
            vert = dest[-1]
            if vert not in visited:
                visited[vert] = dest
            
                for f in self.friendships[vert]:
                    path_copy = list(dest)
                    path_copy.append(f)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
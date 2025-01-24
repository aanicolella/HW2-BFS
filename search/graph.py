import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")     

    def checkValidGraph(self, start, end=None):
        try:
            self.graph[start]
        except KeyError:
            raise KeyError('Invalid input--selected start node does not exist')
        if end:
            try:
                self.graph[end]
            except KeyError:
                raise KeyError('Invalid input--selected end node does not exist')


    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        """

        '''
        Function: Run Breadth First Search for graph traversal/path discovery on given graph

        Params:
            * start: key of start node
            * end (optional): key of desired end node
        Output:
            * path: 
                * if end not provided: list of nodes in order of traversal
                * if end provided: list of node path to reach end node from start node (or None if no path)
        '''
        # check if start/end exist
        self.checkValidGraph(start,end)

        # Initialize queue and add start node
        Q = deque([start])
        # initialize visited nodes and path tracking
        visited = set()
        path = []
        # check if end defined, track if so
        if end:
             end_track = {start: ''}
        # while nodes in queue, look at next node in queue
        while Q: 
            v = Q.popleft()
            # check if already visited
            if v in visited:
                 continue
            visited.add(v)
            # check for defined end node, if not add to path order
            if not end:
                 path.append(v)

            # Check for neighbors
            for neighbor in self.graph[v].keys():
                # check if end defined, if so add to end_track and check if == end
                if end and neighbor not in visited:
                    end_track[neighbor] = v
                    # if reach end, extract path from end_track values and reverse to return ordered search path
                    if neighbor == end:
                        get_path = [end]
                        curr_node = end
                        while curr_node != start:
                            curr_node = end_track[curr_node]
                            get_path.append(curr_node)
                        get_path.reverse()
                        return get_path
                        
                # add neighbor to queue
                Q.append(neighbor)
        # if end node not reached, return none
        if end:
            return None
        # if no end node, return path
        return path
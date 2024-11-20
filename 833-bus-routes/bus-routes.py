from collections import deque
class Solution:

    # BFS: THink about bus stops as nodes/vertices and routes as edges
    # Since distance is calculated by the number of stops, we can find the solution by counting the smallest number of nodes (bus stops) in our graph between source and target.
    # Make an adj list and use a queue for BFS

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: 
            return 0 
        adjList = {}

        #index is the bus number
        for bus, route in enumerate(routes): 
            for stop in route: 
                if stop in adjList: 
                    adjList[stop].add(bus)
                else: 
                    adjList[stop] = {bus}
        if source not in adjList: 
            return -1
        visitedBuses = set()
        visitedStops = set()
        queue = deque()
        
        visitedStops.add(source)
        queue.append(source)

        numStops = 0 

        while queue: 
            for i in range(len(queue)): 
                currStop = queue.popleft()
                if currStop == target: 
                    return numStops
                for bus in adjList[currStop]: 
                    if bus not in visitedBuses: 
                        for stop in routes[bus]: 
                            if stop not in visitedStops: 
                                visitedStops.add(stop)
                                queue.append(stop)
                        visitedBuses.add(bus)
            numStops += 1

        return -1

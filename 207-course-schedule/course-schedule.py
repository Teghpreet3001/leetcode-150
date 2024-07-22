class Solution(object):
    
    #two most important things 
    # Remove the node from visited as we are done visiting this node
    #reset the value to an empty  list  so that ot returns True in base case, indicating schedule is possible
    #both things are done to match  base cases
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)
        for courses in prerequisites:
            prereq = courses[0]
            course = courses[1]
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
            
        visited = set()

        def dfs(start):
            if len(graph[start]) == 0:
                return True
            if start in visited:
                return False
            visited.add(start)
            for nextCourse in  graph[start]:
                if not dfs(nextCourse):
                    return False
            visited.remove(start)
            graph[start] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
class Solution(object):

    #visited set is used to keep track of the vertices which we can done dfs on 
    #cycles is used to keep track of thew cycles if any for a particular vertex
    #we dont use the len(graph[start]) == 0 as this condition only checks if a node has no outgoing edges, which is not sufficient for cycle detection.
    #graph[start] = [] not needed as we are checking using  cycle

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for courses in prerequisites:
            #second  element is pre req, first is the course
            prereq = courses[1]
            course = courses[0]
            if course not in graph:
                graph[course] = [prereq]
            else:
                graph[course].append(prereq)

        result = []
        visited = set()
        cycle = set() #cycle does the job of visited

        def dfs(start):
            if start in cycle:
                return False
            if start in visited:
                return True
            cycle.add(start)
            for nextCourse in graph[start]:
                if not dfs(nextCourse):
                    return False
            cycle.remove(start)
            visited.add(start)
            #finally add to result, it has found no cycles and is now visited
            result.append(start)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prevMap[course].append(prereq)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prevMap[course] == []:
                return True
            visited.add(course)
            for prereq in prevMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            prevMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
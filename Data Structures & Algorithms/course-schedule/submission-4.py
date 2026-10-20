class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Initialize adjacency list for each course
        prevMap = {i: [] for i in range(numCourses)}
        

        # Map each course to its prerequisites
        for course, prereq in prerequisites:
            prevMap[course].append(prereq)

        # Track nodes in the current DFS path
        visited = set()
        

        def dfs(course):
            # Cycle detected if course is already in current path
            if course in visited:
                return False
            
            # No prerequisites left to check
            if prevMap[course] == []:
                return True
            
            # Add course to current DFS path
            visited.add(course)
            

            # Recursively check each prerequisite
            for prereq in prevMap[course]:
            
                # Propagate cycle detection
                if not dfs(prereq):
                    return False

            # Remove course after finishing its DFS path
            visited.remove(course)
            

            # Mark course as verified to avoid repeated DFS
            prevMap[course] = []
            return True
            
        # Check every course for cycles
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        
        # All courses can be completed
        return True
        

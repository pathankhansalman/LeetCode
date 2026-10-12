from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Determines if all courses can be finished given prerequisite dependencies."""
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
            
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited_count = 0
        
        while queue:
            node = queue.popleft()
            visited_count += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return visited_count == numCourses

if __name__ == "__main__":
    solution = Solution()
    print("Can finish [2, [[1, 0]]]:", solution.canFinish(2, [[1, 0]])) # True
    print("Can finish [2, [[1, 0], [0, 1]]]:", solution.canFinish(2, [[1, 0], [0, 1]])) # False
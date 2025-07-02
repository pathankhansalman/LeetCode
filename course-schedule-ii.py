# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:37:29 2026

@author: patha
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Build the adjacency list graph and track in-degrees
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
            
        # 2. Track all nodes with no incoming dependencies
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        topological_order = []
        
        # 3. Process the queue and decrement dependencies of neighboring nodes
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If the topological sort includes all courses, a valid schedule exists
        return topological_order if len(topological_order) == numCourses else []

# Example Execution
if __name__ == "__main__":
    sol = Solution()
    # 4 courses, pre-req dependencies: 1->0, 2->0, 3->1, 3->2
    course_dependencies = [[1,0],[2,0],[3,1],[3,2]]
    print(f"Valid Evaluation Sequence: {sol.findOrder(4, course_dependencies)}")
    # Expected Output: [0, 1, 2, 3] or [0, 2, 1, 3]

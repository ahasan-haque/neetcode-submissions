class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect loop
        # run dfs
        # hasmap to map prerequisite
        # set to record visited

        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereq_map[course] == []:
                return True

            visited.add(course)

            for p_r in prereq_map[course]:
                if not dfs(p_r):
                    return False

            prereq_map[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True        
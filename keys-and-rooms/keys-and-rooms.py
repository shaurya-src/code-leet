class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        keys = []
        visited.add(0)
        keys.extend(rooms[0])
        
        while len(keys) > 0:
            # pop the top most key
            curr_key = keys.pop()
            if curr_key not in visited:
                keys.extend(rooms[curr_key])
                visited.add(curr_key)
            
        return len(visited) == n

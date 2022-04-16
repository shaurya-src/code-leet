class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_steps = 0
        remaining_water = capacity
        for i, water in enumerate(plants):
            if remaining_water >= water:
                remaining_water -= water
                total_steps += 1
            try:
                if plants[i+1] > remaining_water:
                    total_steps += 2*i + 2
                    remaining_water = capacity
            except:
                pass
        return total_steps
            
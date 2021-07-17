class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        record = {}
        all_cities = []
        for cities in paths:
            record[cities[0]] = cities[1]
        
        for city in record.values():
            if city not in record:
                return city
        return False

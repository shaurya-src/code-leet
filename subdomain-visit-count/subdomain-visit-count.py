class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        record = {}
        for i in range(len(cpdomains)):
            s = cpdomains[i].split()
            dc = int(s[0])
            domain = s[1].split('.')
            
            count = len(domain)
            i = 0
            domains = []
            
            while i < count:
                dm = '.'.join(domain[i:])
                domains.append(dm)
                i += 1

            for part in domains:
                if part not in record:
                    record[part] = dc
                else:
                    record[part] += dc
        
        result = []
        for key, value in record.items():
            result.append("{} {}".format(value, key))
        
        return result
        
        
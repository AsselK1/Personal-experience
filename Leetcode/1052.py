class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        k=minutes
        start=0
        end=k-1
        max_=0
        for i in range(end+1, len(customers)):
            if not grumpy[i]:
                max_+=customers[i]
        max_+=sum(customers[start:end+1])
        count=max_
        while end<len(customers):
            if grumpy[start]:
                count-=customers[start]
            if end<len(grumpy)-1 and grumpy[end+1]:
                count+=customers[end+1]
            start+=1
            end+=1
            max_=max(count, max_)
        return max

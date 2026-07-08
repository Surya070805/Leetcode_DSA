class Solution(object):
    def topKFrequent(self, nums, k):
        maps={}
        for i in nums:
            maps[i]=maps.get(i,0)+1

        sorted_map=sorted(maps.items(),key=lambda x:x[1], reverse=True)

        return [i for i,j in sorted_map[:k] ]
        





        return (output)



        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
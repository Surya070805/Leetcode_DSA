class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        longest=0
        for i in nums:
            if (i-1) not in nums:
                length=0
                while (i+length) in nums:
                    length+=1
                longest=max(length,longest)
        return longest
            


        """
        :type nums: List[int]
        :rtype: int
        """
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
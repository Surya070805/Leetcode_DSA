class Solution(object):
    def twoSum(self, nums, target):
        mp={}
        for i in range(len(nums)):
            comp=target-nums[i]

            if comp in mp:
                return([i,mp[comp]])
            else:
                mp[nums[i]] = i




        

            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
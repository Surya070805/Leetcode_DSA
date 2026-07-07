class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        if st[:]==st[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
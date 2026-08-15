class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        word = s.split()
        return len(word[-1])
        

        
        
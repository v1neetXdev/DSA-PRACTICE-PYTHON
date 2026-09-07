class Solution(object):
    def isHappy(self, n):
        seen = set()
        while  n != 1 : 
            if n in seen : 
                return False
            
            seen.add(n)
            a = str(n)
            sum = 0
            for i in range ( 0 , len(a) ) : 
                sum = sum + pow ( int(a[i]) , 2)
                n = sum
        return True
        
        
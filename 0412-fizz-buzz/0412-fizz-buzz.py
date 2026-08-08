class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range ( 1 , n+1) :
            if( i % 3 == 0 and i % 5 == 0) :
                i = "FizzBuzz"
            elif( i % 3 == 0) :
                i = "Fizz"
            elif( i % 5 == 0) :
                i = "Buzz"
            ans.append(str(i))
        return ans
    


        
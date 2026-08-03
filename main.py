marks = [1 , "abc" , 3 , "ab" , 1 ]
a = True
print(" output is : ")
for i in range (0 , len(marks)) :
    if(marks[i] != marks[len(marks) - i - 1]) :
        a = False
if(a):
    print("this is palindrome")
else :
    print("not palindrome")


















'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285911/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_17'''



class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print("",end=" ")
            a='A'
            for k in range(i+1):
                print(a,end="")
                a=chr(ord(a)+1)
                
            a=chr(ord('A')+i-1)
            if(i>0):
                for l in range(i):
                    print(a,end="")
                    a=chr(ord(a)-1)
            print()
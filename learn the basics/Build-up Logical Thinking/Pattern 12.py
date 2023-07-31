'''https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_12'''



class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,end=" ")
            for k in range(N+N-i-i):
                print(" ",end=" ")
            l=i
            while(l>0):
                print(l,end=" ")
                l-=1
            print()


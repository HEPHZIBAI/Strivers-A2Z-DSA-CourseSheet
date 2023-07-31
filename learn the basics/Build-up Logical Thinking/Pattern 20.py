'''https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662287416/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_20'''





class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print("*",end="")
            for k in range((N+N)-(i+i+2)):
                print("",end=" ")
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(1,N):
            for j in range(N-i):
                print("*",end="")
            for k in range((N+N)-(N-i+N-i)):
                print("",end=" ")
            for j in range(N-i):
                print("*",end="")
            print()
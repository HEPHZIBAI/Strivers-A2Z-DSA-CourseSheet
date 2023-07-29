#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_7




class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print("",end=" ")
            for k in range(i+1):
                print("*",end="")
            for l in range(0,i):
                print("*",end="")
            print()


'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8'''


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for k in range(0,i):
                print("",end=" ")
            for j in range(N-i):
                print("*",end="")
            for l in range(0,N-i-1):
                print("*",end="")
            print()

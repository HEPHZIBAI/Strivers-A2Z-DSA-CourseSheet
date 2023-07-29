#https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5




class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N-i):
                print("*",end=" ")
            print()
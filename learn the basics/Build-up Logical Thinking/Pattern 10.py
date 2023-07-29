'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10'''



class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print("*",end=" ")
            print()
        for i in range(N-1):
            for j in range(N-i-1):
                print("*",end=" ")
            print()
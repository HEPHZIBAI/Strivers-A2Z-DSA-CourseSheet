'''https://practice.geeksforgeeks.org/problems/pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_9'''



class Solution:
    def printDiamond(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print("",end=" ")
            for l in range(0,i+1):
                print("*",end=" ")
            print()
        for i in range(N):
            for j in range(0,i):
                print("",end=" ")
            for l in range(N-i):
                print("*",end=" ")
            print()
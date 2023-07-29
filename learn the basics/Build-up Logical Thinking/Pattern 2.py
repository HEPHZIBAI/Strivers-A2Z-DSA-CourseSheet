#https://practice.geeksforgeeks.org/problems/right-triangle/1

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i):
                print("* ",end="")
            print()
#https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1


class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(i):
                print(i,end=" ")
            print()
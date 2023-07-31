'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718712/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_13'''


class Solution:
    def printTriangle(self, N):
        # Code here
        k=1
        for i in range(N):
            for j in range(i+1):
                print(k,end=" ")
                k+=1
            print()
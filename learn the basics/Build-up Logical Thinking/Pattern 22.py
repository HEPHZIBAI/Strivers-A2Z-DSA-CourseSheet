'''https://practice.geeksforgeeks.org/problems/square-pattern-1662666141/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_22'''




class Solution:
    def printTriangle(self, N):
        for i in range(N+N-1):
            for j in range(N+N-1):
                t=i
                b=j
                l=N+N-2-i
                r=N+N-2-j
                print(N-min(min(t,b),min(l,r)),end=" ")
            print()
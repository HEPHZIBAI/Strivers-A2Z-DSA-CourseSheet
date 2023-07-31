'''https://practice.geeksforgeeks.org/problems/square-pattern-1662287714/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_21'''




class Solution:
    def printTriangle(self, N):
        for i in range(N):
            if(i==0 or i==N-1):
                for k in range(N):
                    print("*",end="")
            else:
                for k in range(N):
                    if(k==0 or k==N-1):
                        print("*",end="")
                    else:
                        print("",end=" ")
            print()
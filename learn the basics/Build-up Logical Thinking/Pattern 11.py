'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11'''



class Solution:
    def printTriangle(self, N):
        k=1
        for i in range(N):
            for j in range(0,i+1):
                print(k,end=" ")
                if(k==1):
                    k=0
                else:
                    k=1
            if(i%2!=0):
                k=1
            else:
                k=0
            print()
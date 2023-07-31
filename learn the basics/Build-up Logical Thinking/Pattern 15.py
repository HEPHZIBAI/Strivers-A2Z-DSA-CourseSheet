'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285196/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_15'''





class Solution:
    def printTriangle(self, N):
        for i in range(N):
            a='A'
            for j in range(N-i):
                print(a,end="")
                a=chr(ord(a)+1)
            print()
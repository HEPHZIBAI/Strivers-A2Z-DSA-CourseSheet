'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285334/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_16'''




class Solution:
    def printTriangle(self, N):
        a='A'
        for i in range(N):
            for j in range(i+1):
                print(a,end="")
            a=chr(ord(a)+1)
            print()
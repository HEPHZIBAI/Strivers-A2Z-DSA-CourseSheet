'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1662284916/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_14'''



class Solution:
    def printTriangle(self, N):
        a='A'
        for i in range(N):
            a='A'
            for j in range(i+1):
                print(a,end="")
                a=chr(ord(a)+1)
            print()
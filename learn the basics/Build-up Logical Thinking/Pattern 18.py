'''https://practice.geeksforgeeks.org/problems/triangle-pattern-1662286302/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_18'''



class Solution:
    def printTriangle(self, N):
        a=chr(ord('A')+N-1)
        for i in range(N):
            a=chr(ord('A')+N-1)
            for j in range(i+1):
                print(a,end=" ")
                a=chr(ord(a)-1)
            print()
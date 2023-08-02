/*https://leetcode.com/problems/reverse-integer/*/

#include<limits.h>
int reverse(int x)
{
    long int y=0;
    int m=0;
    while(x!=0)
    {
        y=(y*10)+(x%10);
        x/=10;
        if(y>INT_MAX||y<INT_MIN)
        {
            return 0;
            break;
        }
    }
   
    return y;
}

/*https://leetcode.com/problems/reverse-integer/*/

int reverse(int x)
{
    while(x%10==0)
    x/=10;
    int y=0;
    int t=x;
    if(x<0)
        x*=-1;
    while(x>0)
    {
        y=(y*10)+(x%10);
        x/=10;
    }
    if(t>0)
    return y;
    else
    return y*-1;
}
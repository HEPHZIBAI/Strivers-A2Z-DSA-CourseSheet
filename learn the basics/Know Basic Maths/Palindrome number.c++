/*https://www.codingninjas.com/studio/problems/palindrome-number_624662?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1*/



bool palindrome(int n)
{
    int t=n;
    int u=0;
    while(n>0)
    {
        u=(u*10)+(n%10);
        n/=10;
    }
    if(t!=u)
        return 0;
    else
        return 1;
}
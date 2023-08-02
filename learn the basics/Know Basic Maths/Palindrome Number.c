/*
https://leetcode.com/problems/palindrome-number/description/
*/



bool isPalindrome(int x)
{
    long int t=x;
    long int u=0;
    while(x>0)
    {
        u=(u*10)+(x%10);
        x/=10;
    }
    if(t!=u)
        return 0;
    else
        return 1;
}
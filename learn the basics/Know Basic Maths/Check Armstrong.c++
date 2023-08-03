/*
https://www.codingninjas.com/studio/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
*/


#include <math.h>
bool checkArmstrong(int n)
{
	int t=n;
	int s=0,l;
	int k=0;
	int a[10000000];
    while (t > 0) 
	{
		a[k]=t%10;
		k++;
		t/=10;
	}
    for (int i = 0; i < k; i++) 
	{
		s+=pow(a[i],k);
    }
    if(n==s)
		return 1;
	else
		return 0;
}


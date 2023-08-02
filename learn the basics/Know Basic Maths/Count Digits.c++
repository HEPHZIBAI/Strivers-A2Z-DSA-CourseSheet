/*https://www.codingninjas.com/studio/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf*/


int countDigits(int n)
{
	int c=0;
	int t=n;
    	while (n > 0) 
	{
		if( n%10 !=0&&t%(n%10)==0)
			c++;
		n/=10;
    	}
	return c;
}
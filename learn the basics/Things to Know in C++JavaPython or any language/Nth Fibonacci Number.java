//https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

import java.util.Scanner;
public class Solution {


	public static void main(String[] args) {
		
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int a=1;
		int b=1;
		int c=a+b;
		int m=4;
		if(n==1)
			System.out.print(a);
		else if(n==2)
			System.out.print(b);
		else if(n==3)
			System.out.print(c);
		else
		{
			while(m<=n)
			{
				a=b;
				b=c;
				c=a+b;
				m++;
			}
			System.out.print(c);
		}
	}

}

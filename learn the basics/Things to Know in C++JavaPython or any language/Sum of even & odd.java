//https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1


import java.util.Scanner;
public class Main 
{	
	public static void main(String[] args) 
	{
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int e=0,o=0,l;
		while(n>0)
		{
			l=n%10;
			if(l%2==0)
			e+=l;
			else
			o+=l;
			n/=10;
		}
		System.out.print(e+" "+o);
	}
}



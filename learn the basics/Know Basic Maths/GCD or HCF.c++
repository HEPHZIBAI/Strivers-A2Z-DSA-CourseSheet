/*
https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
*/



int calcGCD(int n, int m) {
  // Write your code here.
  int c=0;
  int l;
  if (n > m)
    l = n;
  else
    l = m;

  for (int i = 1; i <= l; i++)
    {
    if (n % i == 0 && m % i == 0) 
    {
        if(c<i)
        c=i;
    }
    }
    return c;
}
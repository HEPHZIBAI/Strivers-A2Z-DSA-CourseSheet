//https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
#include<stdio.h>

int main(){

    // Write your code here.
    char a;
    scanf("%c",&a);
    if(a>='a'&&a<='z')
    {
        printf("0");
    }
    else if(a>='A'&&a<='Z')
        printf("1");
    else
        printf("-1");
}

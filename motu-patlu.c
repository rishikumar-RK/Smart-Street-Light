#include<stdio.h>
int main()
{
  int n,s1=0,s2=0,i=1,k=0;
  scanf("%d",&n);

  for(i=1;i<n;i++)
  {
    s1=s1+i;
    if(s1+s2>=n)
    {
      k=1;
      break;
    }
    s2=s2+i*2;
    if((s1+s2)>=n)
    {
      k=0;
      break;
    }
  }
  if(k==1)
     printf("Patlu");
  else
    printf("Motu");
  return 0;
}
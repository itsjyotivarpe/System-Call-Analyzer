#include<stdio.h>
 int main()
 {
 char *p="hai friends",*p1;
 p1=p;
 while(*p !='\0') ++*p++;
 printf("%s   %s",p,p1);
 return 0;
 }

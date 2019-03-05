#include<stdio.h>

void main()
{

    FILE *fp;
    char s[80];
    int i,j,k=1;
    fp = fopen("code.txt","r");
    if(fp==NULL)
    {
        puts("Cannot open file");
        
    }
    
    while(fgets(s,79,fp)!=NULL)
    {
        
        printf("%s",s);
        
    }
    fclose(fp);
    for(i=1;i<=100;i++)
		printf(" %d",k++);
    
}

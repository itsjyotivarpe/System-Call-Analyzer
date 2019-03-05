#include<stdio.h>

void main()
{

    FILE *fp;
    char ch;
    int i=1,j,k=1;
    fp = fopen("code.txt","r");
    if(fp==NULL)
    {
        printf("Cannot open file");
        
    }
    
    while(1)
    {
        ch = fgetc(fp);
        if(ch==EOF)
            break;
        printf("%c",ch);
        printf(" ");
        fflush(stdout);
        
    }
    fclose(fp);
    while(i<=100)
	{
		printf(" %d",k++);
		//fflush()
		i++;
	}
}

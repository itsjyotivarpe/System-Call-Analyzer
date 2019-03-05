//stackoverflow
//http://stackoverflow.com/questions/8647518/sigsegv-with-an-extremely-large-100-mb-array-in-c-loop/8647618#8647618


int main()
{
int count=1;
int arr[100000000];
printf("2\n");
for(int i=3;i<100000000;i=i+2)
{
    arr[i]=1;
}
for(int i=3;i<100000000;i=i+2)
{
    if(arr[i]==1)
    {
        count++;
        if(count%100==1)printf("%d\n",i);
        for(long j=2;i*j<100000000;j++)
            arr[i*j]=0;
    }
}
//scanf("%ld",&count);

}

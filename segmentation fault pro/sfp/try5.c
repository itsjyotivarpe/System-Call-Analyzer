//stack overflow


#include <stdio.h>
#include <stdlib.h>
#define A 2000
#define B 2

typedef struct {
    int a[A][A];
} st;

void fun(st s){}

void main()
{
    st s;
    //fun(s);
}

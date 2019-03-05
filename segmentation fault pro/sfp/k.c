#include "bmp.h"

void extractMessage(BMPfile bmpfile) 
{
void extractMessage(BMPfile bmpfile) 
{
    short index = 0;
char word[16];
unsigned char letter = 0;
unsigned char count = 0;
unsigned char temp;
int width = getWidth(bmpfile);
int height = getHeight(bmpfile);
printf("The image has %d x %d pixels\n", width, height);
for (int y = 0 ; y < height ; y++) 
{
    for (int x = 0 ; x < width ; x++) 
    {
        pixel p = getPixel(bmpfile, x, y);  /* read pixel */        
        temp = p.green & 0x01;
        letter = letter << 1;
        letter = letter + temp;         
        count += 1;  
        if(count == 8){
            word[index] = letter;
            index += 1;
            count = 0;} 
        if  (letter == '0')
        {
            break;
        }   
    }
}
    for (int x=0; x < 16; x++)
    {
    printf("%c",word[x]);
    }
}

#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    // This text should NEVER be readable
    char secret_text[] = "This is a secret string. You should not be able to read this!!!";

    //This is the only text you should be able to read.
    char normal_text[1] = "s";
    char *p1 = normal_text;

    int num = 0;
    int i;
    if (argc > 1)
    {
        num = atoi(argv[1]);
    }
    else
    {
        num = 0;
    }

    for (i = 0; i < num; i ++)
    {
        printf("%c\n", *p1);
        p1++;
    }
    
}
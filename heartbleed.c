#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    char secret2[] = "This is a secret string. You should not be able to read this!!!";

    char p[1] = "s";
    char *p1 = p;
    //char secret[] = "This is a secret string";

    
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

    for (i =0; i < num; i ++)
    {
        printf("%c\n", *p1);
        p1++;
    }
    
}
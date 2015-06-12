#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define BUFSIZE 9

int main(int argc, char **argv)
{
    char *internal_buf, *name_buf;
    FILE *fp;
    setvbuf(stdout,_IONBF,0,0);

    if (argc < 2)
    {
        printf("\nUsage: buffer_overflow File name\n");
        exit(1);
    }

    if (strcmp(argv[1], "secret.txt") == 0)
    {
        printf("\nSorry, you are not allowed to access the secret files. Exiting\n");
        exit(1);
    }



    char data_buf[100];

    name_buf = (char *)malloc(BUFSIZE);
    internal_buf = (char *)malloc(BUFSIZE);
    

    // This is the only file you should be allowed to read!
    strncpy(internal_buf, argv[1], 9);
    printf("\ninternal_buf = %s\n", internal_buf);

    // Copy your name to internal buffer.
    strcpy(name_buf, argv[1]);

    printf("\ninternal_buf = %s\n", internal_buf);

    printf("\nHello %s. Opening the file %s for you\n", name_buf, internal_buf);

    fp = fopen(internal_buf, "r");

    fread(data_buf, 1, 100, fp);
    printf("\n %s\n",data_buf);

    return 0;
}
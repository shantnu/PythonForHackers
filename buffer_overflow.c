#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define BUFSIZE 9

int main(int argc, char **argv)
{
    char *filename_buf, *name_buf;
    FILE *fp;
    setvbuf(stdout,_IONBF,0,0);

    if (argc < 2)
    {
        printf("\nUsage: buffer_overflow FileName Yourname\n");
        exit(1);
    }

    if (strcmp(argv[1], "secret.txt") == 0)
    {
        printf("\nSorry, you are not allowed to access the secret files. Exiting\n");
        exit(1);
    }


    char data_buf[60];
    memset(data_buf, 0, 60);

    name_buf = (char *)malloc(BUFSIZE);
    filename_buf = (char *)malloc(BUFSIZE);
    

    // This is the only file you should be allowed to read!
    strcpy(filename_buf, argv[1]);
    printf("\nfilename_buf = %s\n", filename_buf);

    // Copy your name to internal buffer.
    strcpy(name_buf, argv[2]);

    printf("\nfilename_buf = %s\n", filename_buf);

    printf("\nHello %s. Opening the file %s for you\n", name_buf, filename_buf);

    fp = fopen(filename_buf, "r");

    fread(data_buf, 1, 60, fp);
    printf("\n %s\n",data_buf);

    return 0;
}
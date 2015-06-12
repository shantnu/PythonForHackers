#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char password_buffer[10];
    bool password_found = false;


    printf("Welcome to the Top secret website! Enter your password to continue\n");
    gets(password_buffer);

    printf("\n You entered: %s\n", password_buffer);

    if(strcmp(password_buffer, "secret"))
    {
        printf ("Sorry! Wrong password. You can't Enter\n");
    }
    else
    {
        printf ("Well done. Password is corrct. You got the password right. Go right thru. \n");
        password_found = true;
    }

    if(password_found)
    {
        printf("\n***************\nNow entering the secret region.\n*****************\n");
    }

    return 0;
}
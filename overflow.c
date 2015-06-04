

    /* test buffer program */

    #include <unistd.h>

     
     void dead()
     {

      printf("We are dead!\n");
     }

    void Test()

    {

       char buff[4];

       printf("Some input: ");

       gets(buff);

       puts(buff);

    }

     

    int main(int argc, char *argv[ ])

    {

       Test();

       return 0;

    }

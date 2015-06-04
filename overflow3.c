#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFSIZE 8

int main(int argc, char **argv) {
  char *buf, *buf2;

  char read[100];
  int a = 1;
FILE *fp;

  buf = (char *)malloc(BUFSIZE);
  buf2 = (char *)malloc(BUFSIZE);
  strncpy(buf2, "h.txt", 5);
  printf("buf2 = %s\n", buf2);

  if (argc > 1)
  	strcpy(buf, argv[1]);
  printf("buf2 = %s\n", buf2);

  fp=fopen(buf2, "r");

  fread(read, 1, 10, fp);
  printf("Reading file %s\n",read);
}
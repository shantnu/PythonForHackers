
hello.o:     file format elf32-i386


Disassembly of section .text:

00000000 <main>:
#include <stdio.h>

int main()
{
   0:	55                   	push   %ebp
   1:	89 e5                	mov    %esp,%ebp
   3:	83 e4 f0             	and    $0xfffffff0,%esp
   6:	83 ec 20             	sub    $0x20,%esp

    int a = 99;
   9:	c7 44 24 1c 63 00 00 	movl   $0x63,0x1c(%esp)
  10:	00 
    char c;

    printf("\nHello World. a = %d\n", a);
  11:	8b 44 24 1c          	mov    0x1c(%esp),%eax
  15:	89 44 24 04          	mov    %eax,0x4(%esp)
  19:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
  20:	e8 fc ff ff ff       	call   21 <main+0x21>

    return 0;
  25:	b8 00 00 00 00       	mov    $0x0,%eax

  2a:	c9                   	leave  
  2b:	c3                   	ret    

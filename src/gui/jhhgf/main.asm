
main.elf:     file format elf32-avr


Disassembly of section .text:

00000000 <__vectors>:
   0:	12 c0       	rjmp	.+36     	; 0x26 <__ctors_end>
   2:	19 c0       	rjmp	.+50     	; 0x36 <__bad_interrupt>
   4:	18 c0       	rjmp	.+48     	; 0x36 <__bad_interrupt>
   6:	17 c0       	rjmp	.+46     	; 0x36 <__bad_interrupt>
   8:	16 c0       	rjmp	.+44     	; 0x36 <__bad_interrupt>
   a:	15 c0       	rjmp	.+42     	; 0x36 <__bad_interrupt>
   c:	14 c0       	rjmp	.+40     	; 0x36 <__bad_interrupt>
   e:	13 c0       	rjmp	.+38     	; 0x36 <__bad_interrupt>
  10:	12 c0       	rjmp	.+36     	; 0x36 <__bad_interrupt>
  12:	11 c0       	rjmp	.+34     	; 0x36 <__bad_interrupt>
  14:	10 c0       	rjmp	.+32     	; 0x36 <__bad_interrupt>
  16:	0f c0       	rjmp	.+30     	; 0x36 <__bad_interrupt>
  18:	0e c0       	rjmp	.+28     	; 0x36 <__bad_interrupt>
  1a:	0d c0       	rjmp	.+26     	; 0x36 <__bad_interrupt>
  1c:	0c c0       	rjmp	.+24     	; 0x36 <__bad_interrupt>
  1e:	0b c0       	rjmp	.+22     	; 0x36 <__bad_interrupt>
  20:	0a c0       	rjmp	.+20     	; 0x36 <__bad_interrupt>
  22:	09 c0       	rjmp	.+18     	; 0x36 <__bad_interrupt>
  24:	08 c0       	rjmp	.+16     	; 0x36 <__bad_interrupt>

00000026 <__ctors_end>:
  26:	11 24       	eor	r1, r1
  28:	1f be       	out	0x3f, r1	; 63
  2a:	cf e5       	ldi	r28, 0x5F	; 95
  2c:	d4 e0       	ldi	r29, 0x04	; 4
  2e:	de bf       	out	0x3e, r29	; 62
  30:	cd bf       	out	0x3d, r28	; 61
  32:	02 d0       	rcall	.+4      	; 0x38 <main>
  34:	04 c0       	rjmp	.+8      	; 0x3e <_exit>

00000036 <__bad_interrupt>:
  36:	e4 cf       	rjmp	.-56     	; 0x0 <__vectors>

00000038 <main>:
#include <avr/io.h>

int main (void)
{
	return 0;
  38:	80 e0       	ldi	r24, 0x00	; 0
  3a:	90 e0       	ldi	r25, 0x00	; 0
  3c:	08 95       	ret

0000003e <_exit>:
  3e:	f8 94       	cli

00000040 <__stop_program>:
  40:	ff cf       	rjmp	.-2      	; 0x40 <__stop_program>

TARG=main #varibale
 
CC = avr-gcc
OBJCOPY = avr-objcopy
 
SRCS= main.c  #list varible
 
OBJS = $(SRCS:.c=.o)
 
MCU=atmega8 #varible

CFLAGS = -mmcu=$(MCU) -Wall -g -Os -Werror -lm  -mcall-prologues -DF_CPU=11059200 -Iheader #varible
LDFLAGS = -mmcu=$(MCU)  -Wall -g -Os  -Werror  #varible
 
all: $(TARG)
 
$(TARG): $(OBJS)
	$(CC) $(LDFLAGS) -o $@.elf  $(OBJS) -lm
	$(OBJCOPY) -O binary -R .eeprom -R .nwram  $@.elf $@.bin
	$(OBJCOPY) -O ihex -R .eeprom -R .nwram  $@.elf $@.hex
 
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<
 
clean:
	rm -f *.elf *.bin *.hex  $(OBJS) *.map

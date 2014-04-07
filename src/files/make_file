TARG =main #varibale
OUTDIR = bin
CC = avr-gcc
OBJCOPY = avr-objcopy
SRCS = main.c  #list varible
OBJS = $(SRCS:.c=.o)
MCU=atmega8 #varible
CFLAGS = -mmcu=$(MCU) -Wall -g -Os -Werror -lm  -mcall-prologues -DF_CPU=11059200 -Iheader #varible
LDFLAGS = -mmcu=$(MCU)  -Wall -g -Os  -Werror  #varible

all: dir $(TARG) 

dir:
	-mkdir -p $(OUTDIR)

$(TARG): $(OBJS)
	$(CC) $(LDFLAGS) -o $(OUTDIR)/$@.elf  $(OUTDIR)/$(OBJS) -lm
	$(OBJCOPY) -O binary -R .eeprom -R .nwram  $(OUTDIR)/$@.elf $(OUTDIR)/$@.bin
	$(OBJCOPY) -O ihex -R .eeprom -R .nwram  $(OUTDIR)/$@.elf $(OUTDIR)/$@.hex
 
%.o: %.c
	$(CC) $(CFLAGS) -c -o $(OUTDIR)/$@ $<
	
clean:
	rm -rf bin

TARG = main
OUTDIR = bin
CC = avr-gcc
OBJCOPY = avr-objcopy
SRCS = main.c
OBJS = $(SRCS:.c=.o)
MCU = atmega8
F_CPU = 8000000

CFLAGS = -mmcu=$(MCU) -DF_CPU=$(F_CPU) -Iheader -Os
LDFLAGS = -mmcu=$(MCU)  -Wall -g -Os  -Werror

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

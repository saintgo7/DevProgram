# Makefile for Critical Section

CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -O2
TARGET = program
SRC = main.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run

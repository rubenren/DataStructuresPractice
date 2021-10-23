# The compiler
CC = g++

# Compiler flags:
# -g	- debug info
# -Wall	- turn on compiler warnings
CFLAGS = -g -Wall

# The build target
TARGET = myProgram

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).cpp

# using del for windows TODO(LOW): change this based on OS
clean:
	del $(TARGET).exe

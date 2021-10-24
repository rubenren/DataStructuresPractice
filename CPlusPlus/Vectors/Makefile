# The compiler
CC = g++.exe

# Compiler flags:
# -g	- debug info
# -Wall	- turn on compiler warnings
CFLAGS = -g -Wall

# The build target
TARGET = VectorTest

$(TARGET): $(TARGET).o MyVector.o
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).o MyVector.o

$(TARGET).o: $(TARGET).cpp MyVector.o
	$(CC) $(CFLAGS) -c $(TARGET).cpp

MyVector.o: MyVector.h

# using del for windows TODO(LOW): change this based on OS
clean:
	del $(TARGET).exe
	del *.o

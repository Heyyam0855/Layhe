# Makefile for Blockchain C++ Project

CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -O2
TARGET = blockchain
SOURCES = main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
OBJECTS = $(SOURCES:.cpp=.o)

# Default target
all: $(TARGET)

# Build target
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

# Object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean
clean:
	rm -f $(OBJECTS) $(TARGET)

# Run
run: $(TARGET)
	./$(TARGET)

# Windows üçün
windows:
	g++ -std=c++11 -Wall -Wextra -O2 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp

.PHONY: all clean run windows


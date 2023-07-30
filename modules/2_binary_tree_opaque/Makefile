# Compiler and compiler flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99

# Directories
SRC_DIR = src
BIN_DIR = $(MAIN_DIR)\\build\\bin

# Source files and object files
SOURCES = $(wildcard $(SRC_DIR)/*.c)
OBJECTS = $(patsubst $(SRC_DIR)/%.c, $(BIN_DIR)/%.o, $(SOURCES))

# Target executable
TARGET = $(EXE_NAME)

# Rules
all: $(BIN_DIR) $(TARGET) rm_junk mv_build

$(BIN_DIR):
	mkdir $(BIN_DIR)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJECTS)

$(BIN_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	del /Q $(BIN_DIR)\\$(TARGET).exe

rm_junk:
	del /Q $(BIN_DIR)\\*.o

mv_build:
	move ".\$(TARGET).exe" $(BIN_DIR)\\$(TARGET).exe"

.PHONY: all clean

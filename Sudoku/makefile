CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra

SRCS := $(wildcard *.cpp)
OBJS := $(SRCS:.cpp=.o)
TARGET = client

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $^ -o $@


clean:
	rm -f $(OBJS) $(TARGET)
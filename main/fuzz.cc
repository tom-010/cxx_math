#include <cstdint>
#include <iostream>

std::size_t find_newline(const char *str, const std::size_t size) {
    std::size_t loc = 0;
    while(loc < size && str[loc] != '\n') {
        ++loc;
    }
    return loc;
}

int main() {
    
}

// extern "C" int LLVMFuzzerTestOneInput(const uint8_t* Data, size_t Size) {
//     find_newline(reinterpret_cast<const char *>(Data), Size);
//     return 0;
// }

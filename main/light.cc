#include <iostream>

int main(int argc, char** argv) {
    int a = 0;
    int* a_ptr = &a;
    for(int i=0; i<10; i++) {
        std::cout << a_ptr[i] << '\n';
    }
    std::cout << "light" << '\n';
}
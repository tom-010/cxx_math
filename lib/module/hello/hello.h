#ifndef LIB_MODULE_HELLO_HELLO_H_
#define LIB_MODULE_HELLO_HELLO_H_

#pragma GCC diagnostic push 
#pragma GCC diagnostic ignored "-Wpedantic"
// Here go the includes, that cause -Wpedantic warnings, e.g. #include <evil_file>
#pragma GCC diagnostic pop
// #include <normal_include> normal includes go here


namespace module::hello {
  
  int hello(int input);
  
}

#endif

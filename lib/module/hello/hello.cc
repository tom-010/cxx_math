#include "hello.h"
#include <glog/logging.h>



namespace module::hello {

  bool valid_age(int age) {
    if (age >= 21) {
      return true;
    }
    return false;
  }


  int hello(int input) {
      if(valid_age(input)) {
        return 1;
      }
      return 0;
  }
  
}

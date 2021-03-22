#ifndef EXAMPLE_H_
#define EXAMPLE_H_

#include <string>
#include <iostream>

namespace example {

struct PlayGround {
    int id_;
    std::string name_;

    explicit PlayGround(int id, std::string name):
        id_(id), name_(name) {}

    int play() {
        std::cout << "id: " << id_ << ", name: " << name_ << std::endl;
        return 0;
    }
};

}
#endif

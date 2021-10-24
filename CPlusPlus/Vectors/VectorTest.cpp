#include <iostream>
#include <string>
#include "MyVector.h"

using namespace std;

void ASSERT(bool condition, string msg, bool showInfo = false){
    if(!condition){
        cerr << "TEST FAILED: " << msg << endl;
    }
    else if(showInfo){
        cerr << "TEST PASSED: " << msg << endl;
    }
}

void testSize();

int main(){

    testSize();

}

void testSize(){
    MyVector myVec;
    ASSERT(myVec.get_size() == 0, "expected 0, got: " + to_string(myVec.get_size()), true);

    myVec.push_back(1);
    ASSERT(myVec.get_size() == 1, "expected 1, got: " + to_string(myVec.get_size()), true);
    
}

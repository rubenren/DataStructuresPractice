#include <iostream>
#include <string>
#include "MyVector.hpp"

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
void testResize();
void testAtPush();
void testInsert();
void testPrepend();
void testPop();
void testDel();
void testRemove();
void testFind();

int main(){

    testSize();
    testResize();
    testAtPush();
    testInsert();
    testPrepend();
    testPop();
    testDel();
    testRemove();
    testFind();
}

void testSize(){
    MyVector myVec;
    ASSERT(myVec.get_size() == 0, "expected 0, got: " + to_string(myVec.get_size()));

    myVec.push_back(1);
    ASSERT(myVec.get_size() == 1, "expected 1, got: " + to_string(myVec.get_size()));
    
}

void testResize(){
    MyVector myVec;
    ASSERT(myVec.get_capacity() == 16, "capacity -> expected 16, got: " + to_string(myVec.get_capacity()));
    ASSERT(myVec.get_size() == 0, "size -> expected 0, got: " + to_string(myVec.get_size()));

    myVec.push_back(10);
    ASSERT(myVec.get_capacity() == 16, "capacity -> expected 16, got: " + to_string(myVec.get_capacity()));
    ASSERT(myVec.get_size() == 1, "size -> expected 1, got: " + to_string(myVec.get_size()));

    for(int i = 0; i < 15; i++) myVec.push_back(2);

    ASSERT(myVec.get_capacity() == 32, "capacity -> expected 32, got: " + to_string(myVec.get_capacity()));
    ASSERT(myVec.get_size() == 16, "size -> expected 16, got: " + to_string(myVec.get_size()));

    myVec.push_back(3);
    ASSERT(myVec.get_capacity() == 32, "capacity -> expected 32, got: " + to_string(myVec.get_capacity()));
    ASSERT(myVec.get_size() == 17, "size -> expected 17, got: " + to_string(myVec.get_size()));
}

void testAtPush(){
    MyVector myVec;

    myVec.push_back(10);
    ASSERT(myVec.at(0) == 10, "value -> expected 10, got: " + to_string(myVec.at(0)));

    myVec.push_back(20);
    ASSERT(myVec.at(1) == 20, "value -> expected 20, got: " + to_string(myVec.at(1)));
    ASSERT(myVec.at(0) == 10, "value -> expected 10, got: " + to_string(myVec.at(0)));
}

void testInsert(){
    MyVector myVec;

    myVec.insert(0, 10);
    ASSERT(myVec.at(0) == 10, "insert -> expected 10, got: " + to_string(myVec.at(0)));

    myVec.push_back(1);
    myVec.push_back(2);
    myVec.push_back(3);
    myVec.push_back(4);
    myVec.push_back(5);

    myVec.insert(3, 52);
    ASSERT(myVec.at(3) == 52, "insert -> expected 52, got: " + to_string(myVec.at(3)));
    ASSERT(myVec.at(4) == 3, "insert -> expected 3, got: " + to_string(myVec.at(4)));
}

void testPrepend(){
    MyVector myVec;

    myVec.push_back(1);
    myVec.push_back(1);

    myVec.prepend(20);
    ASSERT(myVec.at(0) == 20, "prepend -> expected 20, got: " + to_string(myVec.at(0)));
}

void testPop(){
    MyVector myVec;

    myVec.push_back(1);
    myVec.push_back(2);
    myVec.push_back(10);
    int val = myVec.pop();

    ASSERT(val == 10, "pop -> expected 10, got: " + to_string(val));
}

void testDel(){

}

void testRemove(){

}

void testFind(){

}

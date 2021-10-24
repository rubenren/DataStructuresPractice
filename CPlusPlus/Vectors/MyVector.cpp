#include "MyVector.hpp"
#include <stdexcept>


// Default Constructor
MyVector::MyVector(){
    size = 0;
    capacity = 16;
    arr = new int[capacity];

}

// Returns the size of the vector
int MyVector::get_size(){
    return size;
}

// Returns how much the array can hold
int MyVector::get_capacity(){
    return capacity;
}

// Returns if the array is empty
bool MyVector::is_empty(){
    return size == 0;
}

// Returns the value at the given index
int MyVector::at(int idx){

    // Consider changing this exception to a custom one
    if(is_empty()) throw std::out_of_range("Can't access an empty Vector!");

    // Bounds wrapping (dont want to be writing to random memory)
    idx = idx % size;

    return *(arr + idx);
}

// Adds a new value to the end of the vector
// returns true if successful false otherwise
void MyVector::push_back(int item){
    if(size >= capacity) resize();
    size += 1;
    arr[size - 1] = item;
}

// inserts the value at the given index
bool MyVector::insert(int idx, int item){
    return false;
}

// inserts the value in the fron of the vector
bool MyVector::prepend(int item){
    return false;
}

// removes the last item and returns it
int MyVector::pop(){
    return 0;
}

// deletes the item at the index, (shifts values over)
void MyVector::del(int idx){

}

// searches and removes all instances of this item
void MyVector::remove(int item){

}

// returns first index found with the item given
int MyVector::find(int item){
    return 0;
}

// use when capacity reached, double size
// when size is 1/4 of capacity, half the size
void MyVector::resize(){

    if(size >= capacity) capacity *= growthFactor;
    else if(size <= capacity / 4) capacity /= growthFactor;
    // Only want to move things around if we need a resize
    else return;

    int* temp = new int[capacity];

    for(int i = 0; i < size; i++){
        *(temp + i) = *(arr + i);
    }

    delete arr;
    arr = temp;

}

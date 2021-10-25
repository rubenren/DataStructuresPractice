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
    size += 1;
    if(size >= capacity) resize();
    arr[size - 1] = item;
}

// inserts the value at the given index
bool MyVector::insert(int idx, int item){

    size += 1;

    // Wrap the idx
    idx = idx % size;

    if(size >= capacity) resize();

    for(int i = size; i > idx; i--){
        arr[i] = arr[i-1];
    }

    arr[idx] = item;

    return true;
}

// inserts the value in the front of the vector
void MyVector::prepend(int item){
    insert(0, item);
}

// removes the last item and returns it
int MyVector::pop(){
    if(size == 0) {
        throw "Can't pop an empty vector";
        exit(EXIT_FAILURE);
    }

    int retVal = arr[size - 1];

    size = size - 1;

    resize();

    return retVal;
}

// deletes the item at the index, (shifts values over)
void MyVector::del(int idx){
    if(size == 0){
        throw "Can't del from an empty string";
        exit(EXIT_FAILURE);
    }

    size = size - 1;
    resize();

    for(int i = idx; i < size; i++){
        arr[i] = arr[i + 1];
    }

}

// searches and removes all instances of this item
void MyVector::remove(int item){

}

// returns first index found with the item given
// -1 if not found
int MyVector::find(int item){
    for(int i = 0; i < size; i++){
        if(item == arr[i]) return i;
    }
    return -1;
}

// use when capacity reached, double size
// when size is 1/4 of capacity, half the size
void MyVector::resize(){

    if(size >= capacity) capacity *= growthFactor;
    else if(size <= capacity / 4 && capacity / 4 > minSize) capacity /= growthFactor;
    // Only want to move things around if we need a resize
    else return;

    int* temp = new int[capacity];

    for(int i = 0; i < size; i++){
        *(temp + i) = *(arr + i);
    }

    delete arr;
    arr = temp;

}

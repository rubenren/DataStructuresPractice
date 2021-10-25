#pragma once

// Going to try to use pointers instead of direct array accessing
class MyVector{
    private:
        int size;
        int capacity;
        int *arr;
        int growthFactor = 2;

        int minSize = 16;

        // use when capacity reached, double size
        // when size is 1/4 of capacity, half the size
        void resize();
        
        // used to move elements of the array over
        void shifter(int idx);

    public:
        // Default Constructor
        MyVector();

        // Returns the size of the vector
        int get_size();

        // Returns how much the array can hold
        int get_capacity();

        // Returns if the array is empty
        bool is_empty();

        // Returns the value at the given index
        int at(int idx);

        // Adds a new value to the end of the vector
        // returns true if successful false otherwise
        void push_back(int item);

        // inserts the value at the given index
        bool insert(int idx, int item);

        // inserts the value in the fron of the vector
        bool prepend(int item);

        // removes the last item and returns it
        int pop();

        // deletes the item at the index, (shifts values over)
        void del(int idx);

        // searches and removes all instances of this item
        void remove(int item);

        // returns first index found with the item given
        int find(int item);

};

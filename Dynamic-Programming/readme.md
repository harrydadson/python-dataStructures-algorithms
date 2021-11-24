# Memory Management

## 2 Types of memory

- Stack Memory: Region in the RAM. Specialdata type that stores active funcs and local variables
  Fast acces

- Heap Memory: Region in the RAM. size is bigger, store objects in Heap memory. slow access.

## Recursion

A method (procedure) where the solution to a problem depends on solutions to smaller instances of the same problem

- We break down task into smaller subtasks
- We define base cases in order to avoid infinite loops
- we can solve problems with recursion or with iteration (we can transform recursion into iteration and vice versa)

  - Types of Recursion
    - Tail Recursion: if the recursive call occurs at the end of a function (the tail recursion is to a loop, for or while loop)
    - Head Recursion: if the recursive call occurs at the beginning of a function (this method saves the state before jumping into the next recursive call, more memory)

## Linear Search (Sequential Search)

method for finding an item (element) in an unsorted list, makes N comparisons in worse-case
hence the runtime complexity is O(N) linear, O(logN) or even O(1) runtime with binary search and hash-tables

## Binary Search (Logarithmic Search)

method for finding the position of an item (element) in a sorted list, makes logN comparison in worst-case. hence running time-complexity of O(logN). Has pratical and real-world applications as       O(logN) running time is quite favorable - it is close to O(1) constant running time.

## Selection Algorithms

Algorthms to find the kth smallest (or largest) item in a data structure, such number is called kth order statistic. We find the max, min, or the medium item. The aim is to achieve O(N) linear running time-complexity. Algos: **quickselect** or median of medians method or secretary selection

- Quickselect Algorithm
  - designed by Tony Hoare
  - able to find the k-th smallest or largestitem in an unordered array
  - O(N) linear running time in best-case, O(N^2) quadratic run-time
  - does not need additional memory
  - choose a so-called pivot item at random
  - partition the array (based on the value of the pivot)
  - instead of recursion of both sides, we take just one side

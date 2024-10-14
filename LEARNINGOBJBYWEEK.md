# 2050 Learning Objectives by Week

## Week 1: Basic Python

  - To know the correct usage of and the difference between python's standard collections classes.
    - `list` [ ], `dict` { }, `set` set( ), `tuple` ( ), `string` " "


  - To write python functions and understand the related concepts of local variable, parameter, and return value.

## Week 2: Collections and Object-Oriented Programming

  - To write and understand list comprehensions.
    - L = [item for item in iterable]
    - L = [k+v for k,v in dict.items()]
    - D = {i:"i" for i in L}

### OOP

  - To correctly use vocabulary: object, class, instance, method,
  inheritance, encapsulation, abstraction, subclass, superclass, ADT, semantics.
    - inheritance: "is a", a subclass based on the superclass using a similar implementation
    - encapsulation: hide the internal details of a class in other modules
    - abstraction: exposing essential features while hiding others
    - polymorphism: the ability to treat certain types of data in specific ways
    - ADT: defines, in general terms, how a data structure should behave while given no specifics for concrete implementations


  - To write a class that implements an ADT.

  - To understand that inheritance means "is a" and code should reflect that.

## Week 3: Asymptotic Analysis of Algorithms

  - To analyze the running time of methods as a function of the input size.

  - To correctly use the vocabulary of *linear*, *quadratic*, *logarithmic*, and *exponential* time.
    - linear: O(n)
    - quadratic: O(n^2)
    - logarithmic: O(log(n))
    - exponential: O(2^n)

## Week 4: Linear Data Structures

### Stacks, Queues, and Deques

  - To know the defining characteristics of the Stack, Queue, and Deque ADTs as well as how to implement and use them.
    - stack: push, pop
    - queue: enqueue, dequeue
    - deque: addfirst, addlast, removefirst, removelast

### Linked Lists

  - To know how to traverse a linked list.

```python
def _nodes(self):
    node = self._head
    while node is not None:
        yield node
        node = node.next()
```
  
  - To know how to reverse a linked list.

```python
    def reverse(self):
        current = self._head
        previous = None
        self._tail = current
        while current is not None:
            upnext = current.next()
            current.setnext(previous)
            previous = current
            current = upnext
        self._head = previous
            
```
  
  - To be able to implement the Deque ADT with a doubly-linked list.

## Week 5: Recursion and Dynamic Programming

  - To recognize recursive structure in problem definitions.

  - **To analyze the recursion depth of a recursive algorithm.**

  - To be able to rewrite recursive functions with a loop and an explicit stack.
    - Keep a stack of things to visit/do. Pop the stack and carry out procedure while possibly adding new items to the stack. Loop over stack while stack is not empty

## Week 6: Midterm 1

## Week 7: Searching and Sorting

### Binary Search

  - To know how to implement binary search with and without recursion.
```python
def bsiter(L, n):
    start = 0
    end = len(L)-1
    while True:
        if start == end:
            return n == L[start]
        mid = (start + end)//2
        if n == L[mid]:
            return True
        elif n > L[mid]:
            start = mid+1
        else:
            end = mid-1
```
```python
def bsrecur(L, n):
    if len(L) == 1:
        return n == L[0]
    mid = len(L)//2
    if n == L[mid]:
        return True
    elif n > L[mid]:
        return bsrecur(L[mid+1:], n)
    else:
        return bsrecur(L[:mid], n)
```
  - To be able to analyze the asymptotic running time of binary search and related *prune-and-search* algorithms.

  - To understand how different implementations of the SortedMap ADT make tradeoffs between the efficiency of the different operations.
    - `SortedMapList`:
      - membership, pred: O(log(n))
      - maintains sorted order
    - `SortedMapDict`:
      - membership: O(1)
      - pred: O(nlog(n))
    - `SortedMapLL`:
      - membership, insertion, pred: O(n)

### Quadratic-Time Sorting algorithms

  - To identify and name the basic quadratic-time sorting algorithms:

    - `BubbleSort`: repeatedly compare neighbors and swap if necessary
    - `SelectionSort`: repeatedly pick the smallest element and append
    - `InsertionSort`: repeatedly add new element to sorted result


  - To understand the concept of a loop invariant and how it can be used to reason that an algorithm is correct.
    - `invariant`: something that is true every time we reach a certain point in the algorithm
      - ex. After *i* iterations of `BubbleSort` we know the last *i* elements are in their final places. When n=*i*, the list is sorted.

## Week 8: Divide-and-Conquer

  - To identify and classify the three (plus one) aspects of a divide-and-conquer algorithm: *Divide*, *Conquer*, and *Combine* (plus a *Base case*).

  - To write a simple divide and conquer algorithm to solve a problem on lists.

  - To describe the main features of the two main divide-and-conquer sorting algorithms:

    - `MergeSort`:
      - average: O(nlog(n))
      - worst: O(nlog(n))
      - not-in-place
      - work done in combine step
    - `QuickSort`:
      - average: O(nlog(n))
      - worst: O(n^2)
      - in-place
      - work done in divide step


  - To analyze the asymptotic running time of a simple divide-and-conquer algorithm.

### Selection

  - To understand why `quickselect` is asymptotically faster than `quicksort`.
    - `quickselect`: "prune-and-conquer", O(n)


```python
def qs(k, L, left, right):
    pivot = partition(L, left, right) # pivot is index
    if k < pivot - left: # in left side?
        return qs(k, L, left, pivot)
    elif k == pivot - left + 1: # in pivot location?
        return L[pivot] # return the item at pivot location
    else: # in right side?
        return qs(k - (pivot - left + 1), L, pivot + 1, right)
```

  - To understand the relationship between the median problem and the selection problem.

## Week 9: Maps, Sets, and Hash Tables

  - To know the Map ADT as well as several implementations.

  - To understand why the average running time of hash table operations are constant.

  - To understand the concepts of hash function and hash collision.
    - `chaining`: if a collision occurs, then new item is appended onto a list representing the bucket
    - `linear probing`: if a collision occurs, then new item in placed into next available adjacent bucket


  - To understand why keys must be immutable, and for example, why a `list` cannot be used as the key in a `dict`.
    - keys cannot be mutable because then the corresponding value may not be accessible if the key changes, this is because the retrieval of the value depends on the original key to pass through the hash function


  - To know the relationship between a `dict` and a `set` in terms of their common implementation with hash tables, and further, to be able to implement the Set ADT with a hash table.
    - `Set` implementation: use key for both the key and value

## Week 10: Midterm 2

## Week 11: Trees

### Tree Traversal

  - To correctly use the vocabulary for *tree*, *height*, *depth*, *parent*, and *child*.
  
  ![tree](https://user-images.githubusercontent.com/18701989/46369758-e1569a80-c651-11e8-8546-80485d1ce361.PNG)


  - To recognize and implement the basic tree traversal algorithms: *pre-order*, *post-order*, and *in-order* traversal.
    - *pre-order*: self -> children
    - *post-order*: children -> self
    - *in-order*: left -> self -> right
      - Note: `BinaryTree` only

### Binary Search Trees (BSTs)

  - To be able to implement the basic operations on BSTs: *insertion*, *search*, *predecessor search*, *removal*.

  - To know the asymptotic running times of basic operations on BSTs and their relationship to the tree depth.

  - To understand tree rotations, how they work, and why they are useful for Binary Search Trees.
  
  ![treerotation](https://user-images.githubusercontent.com/18701989/46369813-03e8b380-c652-11e8-8be8-1a4714735977.PNG)
  
  - **To understand the rotate-to-root heuristic for BSTs and two variants: `splayinsert` and `treapinsert`.**

## Week 12: Priority Queues and Heaps

  - To know the characteristics of the Priority Queue ADT.
    - insert: add item to PQ
    - removemin: pop off item with highest priority (smallest key)


  - To know how to implement a priority queue using a `list`.
    - `UnsortedListPQ` has O(1) insertion but O(n) removemin
    - `SortedListPQ` has O(n) insertion but O(1) removemin


  - To know how to implement a priority queue using a `BST`.
    - `BST` where the key of every node is less than the keys of its children


  - To know how to implement a priority queue using a heap.
    - Use a `list` that is heap ordered, i.e. the children of a parent at location *i* are located at *2i* and *2i+1* if they exist. Then we insert and removemin by calling upheap and downheap to move nodes around in the heap.


  - To understand the list representation of a complete binary tree and to be able to transform between the tree and list representations.

## Week 13: Graphs I: DFS, BFS, and Connectivity

  - To correctly use graph vocabulary: *graph*, *vertex*, *edge*, *directed*, *undirected*, *path*, *connected*, *degree*.
    - *path*: a sequence of vertices or edges (or both) between nodes
    - *connected*:
      - vertices u,v are *connected* if there exists a path from u to v
      - a graph is *connected* if for all u,v in the graph, u and v are connected
    - *degree*: # of edges incident to a given vertex


  - To know some different concrete data structures to implement graphs including *the edge list*, *the adjacency set*, and *the adjacency matrix*.
    - `EdgeList`: stores list of edges and list of vertices, must traverse list for many operations
    - `AdjacencySet`: stores a set of vertices and a set of neighbors for each vertex, edges are implied
    - `AdjacencyMatrix`: a matrix of zeros that stores edges between vertices as ones


  - To be able to test if two vertices in a graph are connected using either a recursive or non-recursive algorithm.

```python
def connectedrecur(u, v, visited):
    if u is v: return True
    for w in nbrs(u):
        if w not in visited:
            visited.add(w)
            if connectedrecur(w, v, visited): return True
    return False
```

```python
def connectediter(u, v, visited):
    tovisit = [u]
    while tovisit:
        n = tovisit.pop()
        if n is v: return True
        for w in nbrs(n):
            if w not in visited:
                tovisit.append(w)
                visited.add(w)
    return False
```

  - To recognize and understand the characteristic features of **Depth-First Search** and **Breadth-First Search** in a graph.
    - `dfs`: use stack, finds max distance away from starting vertex first
    - `bfs`: use queue, finds shortest path first


  - To understand how to represent a directed forest using a `dict` or other map.

## Week 14: Graphs II: Shortest Paths and Minimum Spanning Trees

  - To know Dijkstra's algorithm for the single source all-shortest path problem.

```python
def dijkstra(G, u, D, forest):
    # init D to have all values of float('inf')
    tovisit = PQ()
    while tovisit:
        v = tovisit.removemin()
        for w in G.nbrs(v):
            newdist = D[v] + G.wt(v, w) # Prim's: newdist = G.wt(v, w)
            if newdist < D[w]:
                forest[w] = v
                D[w] = newdist
                tovisit.reducepriority(w, D[w])
```

  - To know how to extract shortest paths from the `forest` map populated by Dijkstra's algorithm.

  - To know Prim's algorithm for computing the minimum spanning tree of an undirected graph.

  - To know how to analyze different *priority-first search* algorithms such as Dijkstra's and Prim's algorithms.
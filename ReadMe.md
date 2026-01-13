# DSA 

Learning the fundamentals of data structures and algorithms, including algorithmic thinking, time and space complexity, and Big-O notation, to build a strong analytical foundation.

## Progress
- Linear Data Structures: Linked Lists, stacks, queues
- Non Linear Data Structures: Binary trees, Binary Search Trees (transversal techniques and efficient data organisation)
- Priority Based and Constant-time lookup strategies (Heaps and hashing)
- Search algorithms 
- Recursion 
- Hands-on Practice and Consolidation

## Big O

Time Complexity -- measure of the number of operations it takes to complete a task

Space Complexity -- measure of the memory space occupied by a program as it runs

### Worst Case Scenario 

> **Using an Example**
>
> with `1 2 3 4 5 6 7` a group of numbers and you are supposed to find one number

$\omega$ - best case scenario (looking for number 1 takes only one step)

$\theta$ - average time (takes 4 steps)

$\omicron$ - worst case scenario (takes all the sevens steps)

> The focus of this study is to understand the worst case
> 

1. **Big O O(n)** - For a given n tasks the program takes n steps to complete the project
2. **Big O O($n^2$)** - For a given n tasks. The program takes $n^2$ steps to complete the task
3. **Big O O(1)** - there is only one operation being carried out. Even if N increases there remains only one operation
4. **Big O O(log n)** - how many times can you divide n steps into 2 parts to find your 1 item
5. **Big O O(n log n)** - the most efficient sorting algorithm

### Simplifying Big O Notation

1. Drop the constant -- if a program produces m times the output for n tasks. The program runs at O(m * n) simplified to O(n)
2. Drop the non-dominant -- if the program runs at O($n ^2$ + n) increasing n to a large value affects $n^2$ more than n. So the program runs at O($n^2$)

| Operation           | What Happens                                 | Big O |
| ------------------- | -------------------------------------------- | ----- |
| `list.append(x)`    | Adds one element to the end                  | O(1)  |
| `list.pop()`        | Removes the last element                     | O(1)  |
| `list.insert(i, x)` | Shifts elements to the right after index `i` | O(n)  |
| `list.pop(i)`       | Shifts elements to the left after index `i`  | O(n)  |
| `list.index(x)`     | Scans elements until `x` is found            | O(n)  |
| `list[i]`           | Directly accesses element at index `i`       | O(1)  |

### Analogy

> O($n^2$) -- loop within a loop
> 
> O(n) -- proportional
> 
> O(log n) -- divide and conquer
> 
> O(1) -- constant
> 

[big O cheatsheet](https://bigocheatsheet.com)


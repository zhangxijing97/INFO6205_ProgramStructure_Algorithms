# INFO6205_ProgramStructure_Algorithms

# Table of Contents

- [INFO6205_ProgramStructure_Algorithms](#info6205_programstructure_algorithms)
  - [Lecture 1](#lecture-1)
    - [Course Overview](#course-overview)
    - [Array](#array)
    - [Linked List](#linked-list)
    - [LaTeX Overview](#latex-overview)
  - [Lecture 2](#lecture-2)
    - [Stacks (LIFO – Last In, First Out)](#stacks-lifo--last-in-first-out)
    - [Queues (FIFO – First In, First Out)](#queues-fifo--first-in-first-out)
    - [Asymptotic Analysis (Big-O Notation)](#asymptotic-analysis-big-o-notation)
      - [O-notations Example](#o-notations-example)
      - [Ω-notations Example](#ω-notations-example)
      - [Θ-notations Example](#θ-notations-example)
    - [Sorting Algorithms](#sorting-algorithms)
    - [Insertion Sort](#insertion-sort)
  - [Lecture 3](#lecture-3)
    - [Quicksort (Divide and Conquer Sorting Algorithm)](#quicksort-divide-and-conquer-sorting-algorithm)
    - [Counting Sort (O(n))](#counting-sort-on)
    - [Radix Sort (O(nk))](#radix-sort-onk)
    - [Recurrence](#recurrence)

## Lecture 1

### Course Overview

- Algorithm design techniques (recursion, divide & conquer, greedy, dynamic programming)
- Data structures (arrays, linked lists, stacks, queues)
- Algorithm analysis (correctness, complexity)

### Array

NumPy Arrays Example
```
import numpy as np

arr1D = np.array([1, 2, 3, 4, 5])
print(arr1D)

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

# Accessing elements
print(arr2D[1, -1])  # Last element of the second row
```

NumPy Slicing and Reshaping
```
# Slicing: [start:end:step]
print(arr1D[1:5:2])  # Every other element from index 1 to 5
print(arr1D[::2])    # Every other element from entire array

# Reshaping: Convert 1D to 2D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr2D = arr.reshape(4,3)  # Converts into 4 rows & 3 columns
print(newarr2D)
```

Advantages of Arrays<br>
- ✔ Constant time access (O(1)) due to direct indexing.
- ✔ Efficient memory usage (contiguous storage, good cache locality).
- ✔ Supported in all programming languages (widely used).
- ✔ Simple and easy to use compared to other data structures.
- ✔ Supports multi-dimensional structures (2D, 3D arrays).


Disadvantages of Arrays<br>
- ✖ Fixed size – cannot grow dynamically like linked lists.
- ✖ Insertion and deletion are costly (O(n)) due to shifting elements.
- ✖ Only supports one data type – lacks flexibility.

### Linked List

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.print_list()
```

Advantages of Linked Lists<br>
- ✔ Dynamic sizing – can grow/shrink as needed.
- ✔ Efficient insertions and deletions – no need to shift elements.
- ✔ More flexible memory allocation – does not require contiguous memory like arrays.

Disadvantages of Linked Lists<br>
- ✖ Extra memory for pointers – each node requires storage for links.
- ✖ Sequential access (O(n)) – no direct indexing like arrays (O(1)).
- ✖ More complex implementation due to pointer management.

### LaTeX Overview

Basic Document Structure
```
\documentclass{article} % Specifies the type of document (e.g., article, report, book)
\usepackage{amsmath}    % Include extra features like advanced math formatting
\begin{document}        % Start of the document content

Hello, World!           % Your content goes here

\end{document}          % End of the document
```

Sections and Subsections
```
\section{Section Title}
\subsection{Subsection Title}
\subsubsection{Sub-subsection Title}
```

Mathematical Equations
```
\[
a^2 + b^2 = c^2
\]
```

Lists (Bulleted & Numbered)
```
\begin{itemize}
  \item First item
  \item Second item
\end{itemize}

\begin{enumerate}
  \item First item
  \item Second item
\end{enumerate}
```

Tables
```
\begin{tabular}{|c|c|c|}
\hline
Header 1 & Header 2 & Header 3 \\ \hline
Cell 1   & Cell 2   & Cell 3   \\ \hline
Cell 4   & Cell 5   & Cell 6   \\ \hline
\end{tabular}
```

Adding Images
```
\usepackage{graphicx}

\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{image.jpg} % Adjust width as needed
\caption{A sample image}
\end{figure}
```

## Lecture 2

### Stacks (LIFO – Last In, First Out)

| Operation  | Time Complexity |
|------------|----------------|
| **Push(item)** – Add element | `O(1)` (without resizing) |
| **Pop()** – Remove top element | `O(1)` |
| **Peek()** – Get top element without removing | `O(1)` |
| **Size()** – Get number of elements | `O(1)` |
| **IsEmpty()** – Check if stack is empty | `O(1)` |

Stack Applications<br>
- **Depth-First Search (DFS)** in graphs
- **Tree Traversals** (Recursion uses an implicit stack)
- **Undo functionality** in text editors
- **Reversing a string**

### Queues (FIFO – First In, First Out)

| Operation  | Time Complexity |
|------------|----------------|
| **Enqueue(item)** – Add element at end | `O(1)` (without resizing) |
| **Dequeue()** – Remove front element | `O(1)` |
| **Peek()** – Get front element without removing | `O(1)` |
| **Size()** – Get number of elements | `O(1)` |
| **IsEmpty()** – Check if queue is empty | `O(1)` |

Queue Applications<br>
- **Task scheduling** in operating systems (OS)
- **Managing network packets** (TCP/IP, routers)
- **Breadth-First Search (BFS)** in graphs
- **Preorder traversal** in trees (flattening a tree)

### Asymptotic Analysis (Big-O Notation)
- **Measures how an algorithm's running time grows with input size `n`**.
- Focuses on the **leading term** (ignores constants and lower-order terms).
- **Three types of asymptotic bounds**:
  - **Big-O (`O`)** → Upper bound (worst case).
  - **Big-Omega (`Ω`)** → Lower bound (best case).
  - **Big-Theta (`Θ`)** → Tight bound (both upper and lower).

#### O-notations Example

What is `O` for `f(n) = n² + 2n + 1`?<br>

Let `g(n) = n²`,<br>
We need to find constants `c` and `n₀` such that:<br>
`f(n) ≤ c * g(n) for all n > n₀`<br>
which is `n² + 2n + 1 ≤ c * n²`<br>
Since `n² + 2n + 1 ≤ n² + 2n² + n²` for all `n > 1`<br>
We can get `n² + 2n + 1 ≤ 4n²` for all `n > 1`<br>
Therefore, `n₀ = 1` and `c = 4`<br>
`f(n)` grows as `O(n²)`<br>

#### Ω-notations Example

What is `Ω` for `f(n) = log(n⁴) + 2ⁿ`?<br>

Let `g(n) = log(n)`,<br>
We need to find constants `c` and `n₀` such that:<br>
`f(n) ≥ c * g(n) for all n > n₀`<br>
which is `log(n⁴) + 2ⁿ ≥ c * log(n)`<br>
Since `log(n⁴) + 2ⁿ = 4log(n) + 2ⁿ`<br>
and `4log(n) + 2ⁿ ≥ c * log(n)` for all `n > 1`<br>
We can choose `c = 1` and `n₀ = 1`<br>
Therefore, `f(n)` is lower-bounded as `Ω(log(n))`<br>

#### Θ-notations Example

What is `Θ` for `f(n) = n² + 5n log n`?<br>

Let `g(n) = n²`,<br>
We need to find constants `c₁`, `c₂`, and `n₀` such that:<br>
`c₁ * g(n) ≤ f(n) ≤ c₂ * g(n) for all n > n₀`<br>

For the **upper bound (Big-O)**:<br>
Since `5n log n ≤ 5n²` for all `n > 1`, choosing `c₂ = 6` gives:<br>
`n² + 5n log n ≤ 6n²` for all `n > 1`<br>
Thus, `f(n)` is **upper-bounded by `O(n²)`**.<br>

For the **lower bound (Big-Omega)**:<br>
Since `n² + 5n log n ≥ n²` for all `n > 1`, choosing `c₁ = 1` gives:<br>
`n² + 5n log n ≥ n²` for all `n > 1`<br>
Thus, `f(n)` is **lower-bounded by `Ω(n²)`**.<br>

Therefore, `n₀ = 1`, and `f(n) ∈ Θ(n²)`.<br>

### Sorting Algorithms

The Sorting Problem<br>
- Input: Sequence of n numbers.
- Output: Reordering of numbers into increasing order.

Comparison-based sorting:<br>
- Insertion Sort
- Quicksort
- Heapsort
- Merge Sort

Non-comparison-based sorting:<br>
- Counting Sort
- Radix Sort

### Insertion Sort

Algorithm:<br>
- Assume the first j-1 elements are sorted.
- Insert A[j] into the correct position.

```
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
```

Time Complexity:<br>

- Best Case: O(n) – when the array is already sorted.
- Average Case: O(n²) – when elements are in random order.
- Worst Case: O(n²) – when the array is sorted in reverse order.

## Lecture 3

### Quicksort (Divide and Conquer Sorting Algorithm)

```
def quickSort(arr, start, end):
    if start < end:
        pivot = end
        i = start - 1
        for j in range(start, end):
            if arr[j] <= arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
        p = i + 1
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)

arr = [5, 4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5]
```

Time Complexity:<br>

- Best Case (O(n log n)): Pivot is near the middle.
- Average Case (O(n log n)): Randomized pivot selection.
- Worst Case (O(n²)): Pivot is always the smallest/largest (e.g., sorted/reverse sorted arrays).

### Counting Sort (O(n))

Steps:<br>
- Find the maximum value in the array.
- Create a count array initialized with zeros.
- Store occurrences of each element in the count array.
- Compute cumulative sums to determine final positions.
- Place elements into the sorted array.

### Radix Sort (O(nk))

Example:<br>
Sorting [121, 432, 564, 23, 1, 45, 788]:<br>
Sort by units digit → [1, 121, 432, 23, 564, 45, 788]<br>
Sort by tens digit → [1, 23, 121, 432, 45, 564, 788]<br>
Sort by hundreds digit → [1, 23, 45, 121, 432, 564, 788] (Sorted)<br>

### Recurrences and Solving Recurrences

Why Use Recurrences?<br>

- Many algorithms (e.g., Divide and Conquer, Dynamic Programming) use recursion, making it hard to determine their time complexity directly.
- Recurrences give a general method to analyze running time.

Solving Recurrences: <br>
- Substitution Method
- Recursion Tree Method
- Master Theorem

### Substitution Method

It works by guessing a solution and proving it using mathematical induction.<br>

#### Substitution Method Example

What is `O` for `T(n) = 2T(⌊n/2⌋) + Θ(n)`?<br>

The recurrence: `T(n)=2T(n/2)+O(n)` is very similar to Merge Sort, which we already know has complexity `O(n log n)`.<br>
So, we suspect that `T(n) = O(n log n)` might be the correct answer.<br>

Guess `T(n) = O(n log n)`,<br>
We need to prove that `T(n) ≤ c * n log n` for all `n > n₀`.<br>

Inductive Hypothesis:
Assume that `T(n) ≤ c * n log n` holds for `⌊n/2⌋`, meaning:<br>
`T(⌊n/2⌋) ≤ c ⌊n/2⌋ log ⌊n/2⌋`.<br>

Substituting into the recurrence: <br>
`T(n) = 2T(⌊n/2⌋) + Θ(n)`<br>
`≤ 2(c ⌊n/2⌋ log ⌊n/2⌋) + Θ(n)`<br>
`≤ 2(c (n/2) log(n/2)) + Θ(n)`<br>
`= c n log(n/2) + Θ(n)`<br>
`= c n (log n - log 2) + Θ(n)`<br>
`= c n log n - c n log 2 + Θ(n)`<br>
`≤ c n log n`<br>

Since `-c n log 2 + Θ(n)` is a lower-order term,<br>
we can conclude:<br>

Therefore, `T(n) = O(n log n)`.<br>

### Recursion trees Method

- Original problem: root with size n.
- Each non base node has a children with size n/b.
- By summing across each level, the recursion tree shows the cost at each level of recursion.
`Total cost = sum of all levels`
- Can be used to generate a guess. Then verify by substitution method.

#### Recursion trees Method Example

The given recurrence is:
`T(n) = 3T(n/4) + Θ(n²)`
This means:
- The problem of size `n` breaks into 3 smaller subproblems, each of size `n/4`.
- Each level does some extra work of `Θ(n²)` before calling the next level.
- This continues until the problem size reaches `1` (base case).

Step 1: Drawing the Recursion Tree<br>
- Level 0 (Root Node):
  - We start with the original problem `T(n)`, which does `Θ(n²)` work.
- Level 1:
  - The problem splits into 3 subproblems: `T(n/4)`, `T(n/4)`, `T(n/4)`.
  - Each subproblem does its own work of `Θ((n/4)²)`.
- Level 2:
  - Each `T(n/4)` now splits into 3 more subproblems of size `T(n/16)`.
  - This pattern continues until `n = 1`.

Step 2: Finding the Depth of the Tree<br>
- Since each subproblem is reduced by a factor of `4`, the number of levels is:
`log₄(n)`
- So, the tree has `log₄(n)` levels before reaching the base case `T(1) = Θ(1)`.

Step 3: Counting the Number of Leaves<br>
- Each level triples the number of nodes (because `T(n) = 3T(n/4) + Θ(n²)`).
- The total number of leaf nodes at the last level is:
`3^(log₄(n)) = n^(log₄(3))`

Step 4: Calculating the Total Work<br>
- At each level, the work done is decreasing:
`Θ(n²) + Θ((n/4)²) + Θ((n/16)²) + ... + Θ(1)`
- The total work forms a geometric series, which sums to `O(n²)`.

Final Answer<br>
- Depth of the tree: `log₄(n)`
- Number of leaves: `n^(log₄(3))`
- Total work done: `O(n²)`

### Master method

`T(n) = aT(n/b) + f(n)`

Where:<br>
- `a` is the number of recursive subproblems.
- `b` is the factor by which the problem size is reduced.
- `f(n)` is the extra work done at each level outside the recursion.

1. **Case 1** (`f(n)` grows slower than `n^(log_b(a))`):<br>
`f(n) = O(n^(log_b(a) - ε)), where ε > 0`<br>
=>  `T(n) = Θ(n^(log_b(a)))`<br>

2. **Case 2** (`f(n)` grows at the same rate as `n^(log_b(a))`):<br>
`f(n) = Θ(n^(log_b(a)) log^k(n)), where k ≥ 0`<br>
=>  `T(n) = Θ(n^(log_b(a)) log^(k+1)(n))`<br>


3. **Case 3** (`f(n)` grows faster than `n^(log_b(a))`):<br>
`f(n) = Ω(n^(log_b(a) + ε)), where ε > 0`<br>
=>  `T(n) = Θ(f(n))`<br>

#### Master method Example Case 1

`T(n) = 5T(n/2) + Θ(n²)`

Using the Master Theorem for recurrences of the form:<br>

`T(n) = aT(n/b) + f(n)`

where:
- `a = 5` (5 subproblems)
- `b = 2` (each subproblem size is `n/2`)
- `f(n) = Θ(n²)`

We calculate:<br>

`log₂(5) ≈ 2.32`, so `n^(log₂(5)) ≈ n^2.32`.<br>

We try case 1 in here, which mean that `Θ(n²) <= O(n^(log_b(a) - ε))`<br>
For some constant `c > 0`:<br>
`cn² <= c(n^(log_b(a) - ε))`<br>
So we need to find `n² <= n^(log_b(a) - ε)` where `ε > 0`<br>

Comparing `f(n) = Θ(n²)` with `n^(log₂(5)) = Θ(n^2.32)`, we see that `n²` grows slower than `n^2.32`, meaning `log₂(5 - ϵ) >= 2` for `ϵ <= 1`.<br>

Since `f(n) = O(n^(log_b(a) - ϵ))`, we use Case 1 of the Master Theorem:<br>

`T(n) = Θ(n^(log_b(a)))`<br>

Final result:<br>

`T(n) = Θ(n^(lg 5))`<br>

#### Master method Example Case 2

`T(n) = 27T(n/3) + Θ(n³ log n)`

Using the Master Theorem for recurrences of the form:<br>

`T(n) = aT(n/b) + f(n)`

where:
- `a = 27` (27 subproblems)
- `b = 3` (each subproblem size is `n/3`)
- `f(n) = Θ(n³ log n)`

We calculate:<br>

`log₃(27) = 3`, so `n^(log₃(27)) = n³`.<br>

We try case 2 here, which means that `f(n) = Θ(n^(log_b(a)) log^k n)`<br>
For some constant `c > 0`:<br>
`cn³ log n = c(n^(log_b(a)) log^k n)`<br>

Comparing `f(n) = Θ(n³ log n)` with `n^(log₃(27)) = Θ(n³)`, we see that `f(n)` has an extra `log n` factor, meaning `k = 1`.<br>

Since `f(n) = Θ(n^(log_b(a)) log^k n)`, we use Case 2 of the Master Theorem:<br>

`T(n) = Θ(n^(log_b(a)) log^(k+1) n)`<br>

Final result:<br>

`T(n) = Θ(n³ log² n)`<br>
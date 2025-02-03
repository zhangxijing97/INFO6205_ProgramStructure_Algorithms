# INFO6205_ProgramStructure_Algorithms

## Lecture 1

### Course Overview

Algorithm design techniques (recursion, divide & conquer, greedy, dynamic programming)<br>
Data structures (arrays, linked lists, stacks, queues)<br>
Algorithm analysis (correctness, complexity)<br>

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




[DPV 0.3 Page 18] Big-O

The Fibonacci numbers $F_0, F_1, F_2, \dots, $ are defined by the rule $F_0=0, F_1=1, F_n=F_{n-1} + F_{n-2}$. In this problem we will confirm that this sequence grows exponentially fast and obtainsome bounds on its growth.

- (a) Use induction to prove that $F_n\geq 2^{0.5n}$ for $n\geq6$.

- (b) Find a constant $c < 1$ such that $F_n \leq 2^{cn}$ for all $n \geq 0$. Show that your answer is correct.
- (c) What is the largest $c$ you can find for which $F_n=\Omega(2^{cn})$?



[DPV 0.2 Page 18] Fibonacci


[DPV 6.2 Page 170] DP1 - Longest Increasing Subsequence (LIS)


[DPV 6.3 Page 174] DP1 - Longest Common Subsequence (LCS)
- [DPV] 6.1 - A contiguous subsequence of a list $S$ is a subsequence made up of consecutive elements of $S$. For instance, if $S$ is $[5, 15, -30, 10, -5, 40, 10]$, then 15, -30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a linear-time algorithm for the following task:

    *Input*: A list of numbers, $a_1, a_2, \dots, a_n$.

    *Output*: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero).

    For the preceding example, the answer would be 10, -5, 40, 10, with a sum of 55.

    <details>

        1. Subproblem Definition

        Define T[i] as the contiguous subsequence of maximum sum using elements of the given sequence S from index 1 to i, where 1 <= i <= n. (We'll use 1-based index) 

        2. Recurrence Definition
        At each step, there are 2 choices for the algorithm:
            1). if the current element S[i] + T[i-1] > 0, then we simply include this element into the current sum;
            2). otherwise, we give up the current element S[i] and mark T[i] as 0
        We initialize T[1] as max{0, S[1]} as the base case
        

        3. Implementation Analysis
            1). We need to compute T[i] for i = 1, 2, ..., n. Therefore, we have O(n) subproblems
            2). Each subproblem takes O(1) time. In total, it takes O(n) time.
            3). We need to find the maximum element from the T[i] table by a linear scan, which takes O(n) time to extract.
            4). The total runtime is O(n).

    </details>

- [DPV] 6.2 - You are going on a long trip. You start on the road at mile post 0. Along the way there are $n$ hotels, at mile posts $a_1 < a_2 < \dots < a_n$, where each $a_i$ is measured from the starting point. The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at. You must stop at the final hotel (at distane $a_n$), which is your destination. You'd ideally like to travel 200 miles a day, but this may not be possible. If you travel $x$ miles during a day, the penalty for that day is $(200-x)^2$. You want to plan your trip so as to minimize the total penalty -- that is, the sum, over all travel days, of the daily penalties. Given an efficient algorithm that determines the optimal sequence of hotels at which to stop.

    <details>
        1. Subproblem Definition

        Define T[i] as the minimum cost this traveller needs to spend to travel from position 0 to A[i], where A is the given hotel positions and 0 <= i <= n by following the penalty rule given by this problem.

        2. Recurrence Definition
        For each next hotel position i, we need to find the hotel j that needs the minimum daily cost to travel to hotel i. This means for hotel j (0 <= j <= i), the distance between hotel j and i is the cloest to 200 miles (to make the daily cost minimum). Therefore, at each hotel i, we have T[i] = min{T[j] + (200 - (A[i] - A[j]) ^ 2)}, where 0 <= i <= n; 0 <= j <= i. The base case is when there is 0 hotel, then T[0] = 0. If there is 1 hotel, then T[1] = (200 - A[1]) ^ 2, where A[1] is the first hotel's position.
        

        3. Implementation Analysis
            1). the number of subproblems is O(n) where each subproblem represents the minimum cost needed to travel to the current position i.
            2). to solve each subproblem, we need O(n) time because we need to traverse from 0 to i (the current hotel) to find the minimum cost.
            3). the last element in the recurrence table T[-1] is the final answer as it represents the minimum cost needed to travel from origin to the destination hotel by following the given rule.
            4). the extraction time is O(1). Therefore, the total runtime of this algorithm is O(n^2).
    </details>


- [DPV] 6.3 - Yuckdonald's is considering opening a series of restaurants along Quaint Valley Highway (QVH). The $n$ possible locations are along a straight line, and the distance of these locations from the start of QVH are, in miles and in increasing order, $m_1, m_2, \dots, m_n$. The constraints are as follows:
    * At each location, Yuckdonald's may open at most one restaurant. The expected profit from opening a restaurant at location $i$ is $p_i$, where $p_i>0$ and $i=1,2,\dots,n$.
    * Any two restaurants should be at least $k$ miles apart, where $k$ is a positive integer.

    Give an efficient algorithm to compute the maximum expected total profit subject to the given constraints.

    <details>

        1. Subproblem Definition
        Let T[i] represents the maximum total profit obtainable if the first i restaurants are available. T[1] represents the profit when only 1 restaurant is available. Therefore T[1] = P[1].
        2. Recurrence Definition
        At each location i, we have 2 choices:
            1). build a restaurant at location i. In this case, we ensure that restaurant i has at least k miles apart from the previous restaurant at location i - 1. T[i] = max{T[j] + P[i]}, where 0 <= j <= i; 0 <=i <= n; M[i] - M[j] >= k.
            2). do not build a restaurant at location i. T[i] = T[i-1].
        3. Implementation Analysis
            1). The number of subproblems is O(n) because we need to compute the maximum profit when the 1st through i-th restaurants are available.
            2). The runtime for solving each subproblem is O(n) because we need to traverse all previous restaurant locations to find the maximum obtainable profit.
            3). We simply extract the last element from the T table T[-1] to get the max profit. Therefore the extraction time is O(1).
            4). The total runtime for this algorithm is therefore O(n^2).

    
    </details>

- [DPV] 6.4 - Your are given a string of $n$ characters $s[1,\dots,n]$, which you believe to be a corrupted text document in which all punctuation has vanished (so that it looks something like "itwasthebestoftimes..."). You wish to reconstruct the document using a dictionary, which is available in the form of a Boolean function `dict(.)`: for any string $w$, 
    ```
    dict(w) = 
        true if w is a valid word
        false otherwise.
    ```
    (a). Give a dynamic programming algorithm that determines whether the string `s[.]` can be reconstituted as a sequence of valid words. The running time should be at most $O(n^2)$, assuming calls to `dict` take unit time.
    (b). In the event that the string is valid, make your algorithm output the corresponding sequence of words.

    <details>
    1. Subproblems Definition
    We define T[i] as whether string s[1...i] can be reconstituted as a sequence of valid words, where 1 <= i <= n.

    2. Recurrence Definition
    The base case: T[0] = True representing that there's no characters in `s`
    Recurrence: at each character, we need to check if s[1...j] can be reconsituted as a sequence of valid words, where 1 <= j <= i. If true, then let T[i] = True. Otherwise, T[i] = False.


    3. Implementation Analysis
        1). The number of subproblems is O(n)
        2). It takes O(n) time to solve each subproblem given that dict() takes unit time O(1).
        3). We extract T[-1] as the final output which represents if the given string s[1...n] can be reconstituted as a sequence of valid words.
        4). The extraction time is O(1). Therefore the total runtime is O(n^2).


    </details>

- [DPV] 6.5 Pebbling a checkerboard. We are given a checkerboard which has 4 rows and n columns, and has an integer written in each square. We are also given a set of 2n pebbles, and we want to place some or all of these on the checkerboard (each pebble can be placed on exactly one square) so as to maximize the sum of the integers in the squares that are covered by pebbles. There is one constraint: for a placement of pebbles to be legal, no two of them can be on horizontally or vertically adjacent squares (diagonal adjacency is fine). 

(a). Determine the number of legal patterns that can occur in any column (in isolation, ignoring the pebbles in adjacent columns) and describe these patterns.

There are 3 conditions: one is 0 pebbles are placed (1 case); second is 1 pebble is placed (4 cases); third is 2 pebbles are placed (3 cases). Totally, 8 cases.


Call two patterns compatible if they can be placed on adjancet columns to form a legal placement. Let us consider subproblems consisting of the first k columns 1 <= k <= n. Each subproblem can be assigned a type, which is the pattern occuring in the last column.

(b). Using the notions of compatibility and type, give an O(n)-time dynamic programming algorithm for computing an optimal placement.

<details>
1. Subproblem Definition
We let M[i, j] represent the checkerboard, where 1 <= i <= 4; 1 <= j <= n (4 rows, 4 columns).
Let T[i, j] represent the optimal placement when checkerboard size is i x j.
Define a matrix C to represent if a square is chosen or not, where C is a 4 x n boolean matrix.


2. Recurrence Definition
* Base case: T[1, 1] = max{M[1, 1], 0}
* Recurrence: we zig-zag traverse the matrix from left to right and top to bottom. We let T[i, j] = 
    * if M[i, j] can be chosen
        * if T[i-1, j] > T[i, j-1], then T[i, j] = T[i-1, j] + M[i, j]. Let C[i, j] = True.
        * Otherwise, T[i, j] = T[i, j-1] + M[i, j]. Let C[i, j] = True.
    * if M[i, j] can't be chosen, T[i, j] = max{T[i-1, j], T[i, j-1]}

Additionally, we define a method to determine if a given square C[i, j] can be chosen as follows:
* if C[i-1, j] is false and C[i, j-1] is false and M[i, j] > 0, then M[i, j] square can be chosen.

Finally, we return the bottom right element from the T table as the final output (optimal placement).

3. Implementation Analysis

    1). The number of subproblems is O(n)
    2). The runtime to solve a subproblem is O(1)
    3). The extraction time is O(1) as we only need to return the bottom right element from the T table.
    4). The overall runtime of this algorithm is O(n).


</details>


- [DPV] 6.7. A subsequence is palindromic if it's the same whether read left to right or right to left. For instance, the sequence [A, C, G, T, G, T, C, A, A, A, A, T, C, G] has many palindromic subsequences, including A, C, G, C, A and A, A, A, A. Devise an algorithm that takes a sequence $x[1, \dots, n]$ and returns the length of the longest palindromic subsequence. Its running time should be $O(n^2)$.


<details>
1. Subproblem Definition
We are copying x[1...n] to its reverse y[1...n] and looking for LCS.
Let T(i, j) = length of longest common subsequence in x[1...i] and y[1...j] such that y[1...n] is the reverse of x[1...n].


2. Recurrence Definition
y[i] = x[n-1+1], where 1 <= i <=n.
T(i, 0) = 0, where 0 <= i <= n
T(0, j) = 0, where 0 <= j <= n

T(i, j) = T(i-1, j-1) + 1, if x[i] = y[j]
T(i, j) = max{T(i-1, j), T(i, j-1)}, if x[i] != y[j]


3. Implementation Analysis
    1). the number of subproblems is O(n^2)
    2). runtime to fill the table is O(n^2)
    3). the final return is T(n, n) which takes O(1) time.
    4). the overall runtime is O(n^2)



</details>



- [DPV] 6.11


[DPV 6.4 Page 181] DP2 - Knapsack
- [DPV] 6.17 (换钱问题) - Given an unlimited supply of coins of denominations $x_1, x_2, \dots, x_n$, we wish to make change for a value $v$; that is, we wish to find a set of coins whose total value is $v$. This might not be possible: for instance, if the denominations are 5 and 10, then we can make change for 15 but not for 12. Give an $O(nv)$ dynamic-programming algorithm for the following problem.
    *Input*: $x_1, \dots, x_n; v$.
    *Question*: Is it possible to make change for $v$ using coins of denominations $x_1, \dots, x_n$?

    <details>
    1. Subproblem Definition
    We let T[i] represent if value $i$ is able to be reached by using coins of denominations x1, ...xn, where 0 <= i <= v.

    2. Recurrence Definition
    We define T[0] = True as the base case.
    Recurrence T[i] = 
        if i = x_j, then T[i] = True
        if i >= X[j], then T[i] = T[i - x_j], where 1 <= j <= n (case 2)
        else T[i] = False
    Case 2 above means if any value of i - x_j can be reached, then value i can be reached by adding a coin x_j too.

    3. Implementation Analysis
        1). The number of subproblems is O(v)
        2). To solve a subproblem, we need to take O(n) time because we need to traverse all conis
        3). The final output is T[-1] and extraction time is O(1).
        4). The total runtime of this algorithm is O(nv).
    
    </details>

- [DPV] 6.18 (换钱问题变种)


- [DPV] 6.19 (换钱问题变种) - Here is yet antoerh variation on the change-making problem (Exercise 6.17). Given an unlimited supply of coins of denomiations $x_1, \dots, x_n$, we wish to make change for a value $v$ using at most $k$ coins; that is, we wish to find a set of $\leq k$ coins whose total value is $v$. This might not be possible: for instance, if the denominations are 5 and 10 and $k = 6$, then we can make change for 55 but not for 65. Give an efficient dynamic-programming algorithm for the following problem.
    *Input*: $x_1,\dots, x_n; k; v$
    *Question*: Is is possible to make change for v using at most $k$ coins, of denominations $x_1,\dots, x_n$?

    <details>
    1. Subproblem Definitions
    We define T[i,j] as the minimum number of coins needed to reach value i, where 0 <= i <= v; 1 <= j <= n. 

    2. Recurrence Definition
    We define the recurrence rule as:
    We set T[0, :] = inf as base case
    T[i, j] = 
        if X[j] = i, then T[i, j] = 1
        if i > X[j], then T[i, j] = min{T[i - X[j], j] + 1}, for all 1 <= j <= n
        otherwise, T[i, j] = inf, meaning there's no way to make change using the given conins of denominations.


    3. Implementation Analysis
        1). The number of subproblems is O(v)
        2). The runtime of solving each subproblem is O(n)
        3). We extract the minimum element value of the last row of T table as the final solution. This will take O(n) time for extraction.
        4). The overall runtime for this algorithm is O(nv)
    
    </details>

- [DPV] 6.20 (optimal BST问题)


- [DPV] 6.26 (Alignment)


- [DPV] 6.7 (Longest Palindrome Subsequence问题和 Longest Palindrome Substring问题)


- [HW1] - Thief Problem

    ```
    def solution(P, F):
        T = [0] * len(P)
        T[0] = P[0]
        
        for i in range(0, len(T)):
            for j in range(i-1, -1, -1):
                if j + F[j] < i:
                    if P[i] + T[j] > T[i-1] and i - F[i] - j > 1:   # look back and look forward
                        T[i] = P[i] + T[j]
                        print('chose: ', j, ' at ', i)
                        break
                else:
                    T[i] = T[i-1]
        print(T)
        return T[-1]
        
        
    P = [30, 20, 20, 10, 30]
    F = [2, 0, 1, 1, 0]
    print(solution(P, F))
    ```
[DPV 2.5, 6.5 Page 184] - Chain Matrix Multiplication
- [DPV] 



[DPV 6.1, 6.6, 4.6, 4.7 Page 186] - Shortest Paths



---


- [DPV 2.1 Page Page 55] - Fast Integer Multiplication (D&C1). Use the divide-and-conquer integer multiplication algorithm to multiply the two binary integers 10011011 and 10111010.

    <details>
        1. Algorithm
        This is a traditional faster integer multiplication problem. We can divide each integer into halves, namely X_L, X_R, Y_L, and Y_R. Each recursion, we compute (X_L * Y_L * 2^n) + (X_L * Y_R + X_R * Y_L) * 2^(n/2) + X_R * Y_R, where n represents the length of the two given integers.

        2. Justification of Correctness
        This algorithm can calculate integer multiplication correctly because it calculates the left and right halves of the original integers. By the rearragement law of multiplication, it ensures the correctness of the computation results in each recursion step. We can further optimize each recursion step to make it calculate only 3 multiplications as following: (X_L + X_R) * (X_L + X_R) - X_L * Y_L - X_R * Y_R + X_L * Y_L * 2^n + X_R * Y_R. In this way, we simplified to 3 multiplications for each recursion while ensured correctness.

        3. Runtime Analysis
            1). This recursion algorithm takes O(n ^ (log 3)) runtime
            


    </details>


[DPV 2.3 Page Page 60] - Sorting (D&C2). Section 2.2 describes a method for sovling recurrence relations which is based on analyzing the recursion and deriving a formula for the work done at each level. Another (closely related) method is to expand out the recurrence a few times, until a pattern emerges. For instance, let's start with the faimiliar $T(n) = 2T(n/2) + O(n)$. Think of $O(n)$ as being $\leq cn$ for some constant $c$, so: $T(n)\leq 2T(n/2)+cn$. By repeatedly applying this rule, we can bound $T(n)$ in terms of $T(n/2)$, then $T(n/4)$, then $T(n/8)$, and so on, at each step getting closer to the value of $T(.)$ we do know, namely $T(1) = O(1)$.

A pattern is emerging.. the general term is: $T(n) \leq 2^kT(n/2^k)+kcn$

Plugging in $k=\log_2n$, we get $T(n)\leq T(1) + cn \log_2n=O(n \log n)$

(a). Do the same thing for the recurrence $T(n) = 3T(n/2) +O(n)$. What is the general $k$-the term in this case? And what value of $k$ should be plugged in to get the answer?

should be $O(n^{\log_2 3})$.

(b). Now try the recurrence $T(n)=T(n+1)+O(1)$, a case which is not covered by the master theorem. Can you solve this too?

Should be $O(n)$


[DPV 2.4 Page Page 64] - Linear Time Median (D&C2)


- [DPV 2.5] Solving Recurrence. Solve the following recurrence relations and give a $O$ bound for each of them.

    (a). $T(n)=2T(n/3)+1 = n^{\log_3 2} + \log n = O(n^{\log_3 2})$

    (b). $T(n)=5T(n/4)+n = O(n^{\log_4 5})$

    (c). $T(n)=7T(n/7)+n = O(n \log_7 n)$

    (d). $T(n)=9T(n/3)+n^2 = O(n^2 \log_3 n)$

    (e). $T(n)=8T(n/2)+n^3 = O(n^3 \log_8 n)$

    (f). $T(n)=49T(n/25)+n^{3/2}\log n = n^{3/2} \log_{25} n$

    (g). $T(n)=T(n-1)+2 = O(n)$

    (h). $T(n)=T(n-1)+n^c$, where $c\geq 1$ is a constant. $=O(n^{c+1})$

    (i). $T(n)=T(n-1)+c^n$, where $c\geq 1$ is a constant. $=O(c^{n+1})$

    (j). $T(n)=2T(n-1)+1 = O(2^n)$

    (k). $T(n)=T(\sqrt{n})+1 = O(\log \log n)$


- [DPV 2.16] Infinite Array. You are given an infinite array $A[.]$ in which the first $n$ cells contain integers in sorted order and the rest of the cells are filled with $\infty$. You are not given the value of $n$. Describe an algorithm that takes an integer $x$ as input and finds a position in the array containing $x$, if such a s position exists, in $O(\log n)$ time. (If you are disturbed by the fact that the array $A$ has infinite length, assume instead that it is of length $n$, but that you don't know this legnth, and that the implementation of the array data type in your programming language return s the error message $infty$ whenever elements $A[i]$ with $i > n$ are accessed.)

    <details>
    1. Algorithm
    Given that the infinite array A[.] is sorted, we can start by integer y = 1. Then, each recursion step, we double the current integer y as 2 * y. If 2y > x, then we find (y + 2y) / 2; If 2y < x, we find 2y * 2. Otherwise, we return 2y = x.

    2. Justification of Correctness
    This algorithm uses the idea of binary search. Each time, it cuts solution search space by half and finally narrows down to the target integer value x. Therefore, it ensures the correctness of this algorithm.

    3. Runtime Analysis
    Since each recursion cuts the solution space by half, it needs O(log n) time to find the target integer x.

    </details>


- [DPV 2.23] Majority Element. An array $A[1\dot n]$ is said to have a *majority element* if more than half of its entries are the same. Given an array, the task is to design an efficient algorithm to tell whether the array has a majority element, and, if so, to find that element. The elements of the array are not necessarily from some ordered domain like integers, and so there can be no comparisons of the form "is $A[i] > A[j]$?" (Think of the array elements are GIF files, say.) However you can answer questions of the form: "is $A[i] = A[j]$?" in constant time.

    (a). Show how to solve this problem in $O(n\log n)$ time.
    <details>
    1. Algorithm
    Given such an array, we need to first sort it in ascending order. With the sorted array A, we let mid represend the index of the middle element of the sorted array A. In this way, we will have 2 arrays with n/2 length. For the left half array A_L, we let left be the middle index of A_L and right be the middle index of A_R. If array A satisfies the "majority element" property, then for A_L[left] and A_R[right], at least 1 of these two equals to A[mid]. We also denote l and r as 1 and n to represent the left-most and right-most index such that A[l:r] includes all target values.

        * If not, then A is not a "majority element" array. 
        * Otherwise, 
            1. if A_L[left] = A[mid], then it means the left most target value exists to the left of A_L[left]. Therefore, we let left = (l + left) / 2. If A_L[left] != A[mid], it means the left most target value exists to the right of A_L[left]. Therefore we let l = left + 1. We stop searching the left half subarray A_L when l meets left and A_L[left] = A[mid].
            2. if A_R[right] = A[mid], it means the right most target value exists to the right of A_R[right]. Therefore, we let right = (r + right) / 2. If A_R[right] != A[mid], it means the right most target value exists to the left of A_R[right]. Therefore, we let r = right - 1. We stop searching the right half subarray A_R when r meets right and A_R[right] = A_R[mid].

    2. Justification of Correctness
    In this algorithm, we applied binary search on left and right half subarrays to search the left-most and right-most elements that equal to the middle element A[mid]. This ensures the searching space always includes all target values of A[mid] and therefore guarantees the correctness of this algorithm.


    3. Runtime Analysis
    Given the array needs to be sorted, we need O(n log n) time to do this. In the binary search part, we need O(log n) time. Therefore, the overall runtime is O(n log n)

    </details>

    (b). Can you give a linear-time algorithm?
        * Pair up the elements of $A$ arbitrarily, to get $n/2$ pairs.
        * Look at each pair: if the two elements are different, discard both of them; if they are the same, keep just one of them.
    Show that after this procedure there are at most $n/2$ elements left, and that they have a majority element if and only if $A$ does.


- [DPV 2.32] In this problem, we will develop a divide-and-conquer algorithm for the following geometric task.

    CLOSEST PAIR

    *Input*: A set of points in the plane, ${p_1= (x_1, y_1), p_2 = (x_2, y_2), \dots, p_n=(x_n, y_n)} $

    *Output*: The closest pair of points: that is, the pair $p_i \neq p_j$ for which the distance between $p_i$ and $p_j$, that is, $\sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$, is minimized.

    For simplicity, assume that $n$ is a power of two, and that all the $x$-coordinates $x_i$ are distinct, as are the $y$-coordinates. Here is a high-level overview of the algorithm:

    * Find a value $x$ for which exactly half the points have $x_i < x$, and half have $x_i > x$. On this basis, split thepoints into two groups, $L$ and $R$.
    * recursively find the closest pair in $L$ and $R$. Say these pairs are $p_L, q_L \in L$ and $p_R, q_R \in R$, with distances $d_L$ and $d_R$ respectively. Let $d$ be the smaller of these two distances.
    * It remains to be seen whether there is a point in $l$ and a point in $R$ that are less than and sort the remaining points by $y$-coordinate.
    * Now, go through this sorted list, and for each point, compute its distance to the $seven$ subsequent points in the list. Let $p_M, q_M$ be closest pair found in this way.
    * The answer is one of the three pairs ${p_L, q_L}, {p_R, q_R}, {p_M, q_M}$, whichever is closest.

    (a). In order to prove the correstness of this algorithm, start by showing the following property: any square of size $d\times d$ in the plane contains at. most four points of $L$.

    <details>
    
    </details>
    
    (b). Now show that the algorithm is correct. The only case which needs careful consideration is when the closest pair is split between $L$ and $R$.

    <details>
    
    </details>
    
    
    (c). Write down the pseudocode for the algorithm, and show that its running time is given by the recurrence: $T(n)=2T(n/2) + O(n \log n)$. Show that the solution to this recurrence is $O(n \log^2 n$.

    (d). Can you bring the running time down to $O(n \log n)$?


- [DPV 2.18] Consider the task of searching a sorted array $A[1,\dots, n]$ for a given element $x$: a task we usually perform by binary search in time $O(\log n)$. Show that any algorithm that accesses the array only via compairsons (that is, by asking questions of the form "is $A[i]\leq z$?"), must take $\Omega(\log n)$ steps.


- [DPV 2.19] A k-way merge operation. Suppose you have k sorted arrays, each with n elements, and you want to combine them into a single sorted array of $kn$ elements.

    (a). Here's one strategy: Using the `merge` procedure, merge the first two arrays, then merge in the third, and so on. What is the time complexity of this algorithm, in terms of $k$ and $n$?

    <details>
    There are k arrays to be merged. It takes O(n) time to merge two arrays. Therefore the total runtime of this approach is $O(n * k^2)$.
    </details>

    (b). Give a more efficient solution to this problem, using divide-and-conquer.

    <details>
    1. Algorithm
    Given n sorted arrays, we want to merge them to get a combined sorted array. When k = 2, we can simply merge 2 sorted arrays using two points as mentioned in (a). This is the base case of our algorithm. When we have more than 2 arrays, we can recursively separate n arrays into 2 groups, each with k/2 arrays. When it reaches the base case, do the merge step. Finally, this algorithm will return a combined sorted array.


    2. Justification of Correctness
    The base case uses the merge approach which ensures the output array is sorted. Each recursion step, we have two sorted arrays from the previous recursion. This ensures the final output is sorted and is combined from the given n arrays. Therefore it ensures the correctness of this algorithm.

    3. Runtime Analysis
    To merge two sorted arrays, it takes O(n) time. Since we have k arrays and we need to separate them into 2 groups during each recursion step, the recursion tree's depth is O(log k). Therefore, the total runtime T(k) = 2T(k/2) + O(kn) = O(nk log k)

    </details>




 
[DPV 2.2 Page Page 58] - Recurrence (D&C3)




















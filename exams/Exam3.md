


| Problem A | Input | Output |
|---|---|---|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |





### Rudrata Cycle -> TSP

TSP
* Input - 
    * n cities (nodes); 
    * distance matrix of each city pair. d[i][j] represents the distance from city i to j.
    * B budget
* Output
    * Yes/No - if there's a total distance such that the total cost <= B。这里我们直接改写成：是否存在一个tour，使得恰好经过所有城市 一次，且总距离 <= B


Rudrata Cycle

* Input
    * Graph G = (V, E)

* Output
    * Yes/No - represents if Rudrata Cycle exists



----



- [DPV 8.16]



----

- [DPV 8.10]

Proving NP-Completeness by generalization. For each of the problems below, prove that it is NP-complete by showing that it is a generalization of some NP-complete problem we have seen in this chapter.

* a. Subgraph Isomorphism: Given as input two undirected graphs G and H, determine whether G is a subgraph of H (i.e., whether by deleting certain vertices and edges of H we obtain a graph that is, up to remaining of vertices, identical to G), and if so, return the corresponding mapping of V(G) into V(H).


Verification - Given two undirected graphs G and H, we first check if all nodes in G=(V',E') occur in graph H=(V,E). Second, we check if all edges in G occur in graph H. Therefore, this verification takes O(|E|\*|E'| + |V|\*|V'|) time.



Reduction

We will show that Isomorphism problem's difficulty is at least Clique problem, meaning Isomorphism problem is a generalization of Clique problem. For Clique problem, given a graph G and an integer k, does G contain a clique of size k?

Input transformation f - given an instance of clique with graph G=(V,E) and integer k, we build an instance of subgraph isomorphism as follows:
* let G' be a complete graph K_k with k vertices
* let H' be G
* the subgraph isomorphism instance asks "Is G' a subgraph of H'"?
This transformation simply creates a complete graph of size k and uses the original G as H. the construction takes O(k^2) time to create K_k, which is polynomila in the input size. The total runtime of the input transformation is O(k^2+|V|+|E|) which is polynominal.

Output transformation h - If subgraph isomorphism returns a mapping M: V(K_k) -> V(G), then the k vertices in G that are mapped to form the clique of size k in G. We simply return these k vertices as the solution to the clique problem. This takes O(k) time. If subgraph isomorphism returns NO, we return NO for the clique problem. The runtime for the output transformation is O(k) which is polynomial.


IFF

Forward -> if subgraph isomorphism has a solution, then clique has a solution:

Suppose that subgraph isomophism finds a valid mapping M: V(K_k) -> V(G) showing that K_k is a subgraph of G. This means there exist k vertices in G such that each pair of these vertices is connected by an edge. By definition, these k vertices form a clique of size k in G. Therefore, the clique instance has a solution.

Backward -> if clique has a solution, then subgraph isomorphic has a solution:

Suppose the clique instance has a solution: there exists a set S of k vertices in G that form a clique. This means every pair of vertices in S is connected by an edge in G. We can construct a mapping M from the vertices of K_k to the vertices in S. Since S forms a complete subgraph and K_k is also complete with the same number of vertices, this mapping shows that K_k is isomorphic to the subgraph induced by S in G. Therefore, the subgraph isomorphism instance has a solution.





* b. Longest Path - Given a graph G and an integer g, find in G a simple path of length g. 


1. Verification

Given an instance with G=(V,E) and integer g, and a candidate solution p, we can verify it in polynomial time as follows:

    1. check if all nodes on p are in V, which will take O(|V|*g)
    2. check if p is a path, which will take O(g) time
    3. check the length of p and see if it's g. This takes O(g) time.

Therefore, the verification steps overall will take polynomial time.


We want to find a reduction from known problem Rudrata path (A) to the longest path problem (B, unknown). 

2. Input transformation f - 

In Rudrata path, the input instance I is an undirected graph G=(V,E) and we want to find a path that passes through each vertex exactly once. Next, we need to find an input transformation f such that f(I) is an input instance for the longest path problem (B). We can do the transformation f in this way:

    1. create a graph G'=(V, E) with g nodes.

The G' and g will be f(I) which is the input instance for the problem B. This transformation will take O(|V| + |E|) time because we just simply created a new graph, which is polynomial.

3. Output transformation h

If the problem B returns a solution S (a path of length g), then we need to find a transformation h such that h(S) is a soltuion to the instance of problem A. We can define the output transformation h as follows:

    1. since the input graph G'=(V,E) has g nodes, therefore the output path with length g (i.e., S) is the longest path and is a path that passes each vertex exactly once. This defines the output transformation.

This transformation takes O(1) time which is polynomial.


4. Forward -> If problem B has a solution then A has a solution

If we can find a path with length g, since there are g nodes in G', this path is guaranteed to be the longest. Otherwise, it will form a cycle. This matches the definition of Rudrata path. 

5. Backward -> If B has a solution then A has a solution

If Rudrata path problem (A) has a solution, meaning we can find a path that passes each vertex exactly once, then this path must be the longest path we can find in the given instance G=(V,E) because there are only g nodes.


c. Max SAT: Given a CNF formula and an integer g, find a truth assignment that satisfies at least g clauses



1. Verification

Given a CNF and an integer g, we can always convert any CNF into 3SAT CNF formula. Let's denote there are n literals x1, ..., xn and m clauses after the conversion. Given a candidate solution assignment X, we simply need to check each clause's value (true or false). Count the number of true clauses and see if the count is >= g. This will take O(nm) time which is polynomial.

We will use a known 3sat problem (A) to prove that max-sat problem (B) is np-complete. 

2. Input transformation

the input instance for 3SAT problem (A) is a CNF formula (CNF3) with each clause's size <= 3. There are n literals and m clauses. We now need to find a transformation f such that f(I) is a valid input instance for the max-sat problem, where I = (CNF3, n, m). We can:

    1. let CNF = CNF3
    2. let n' = n
    3. let g = m

This transformation f will take O(1) time which is polynomial.

3. output transformation

Now, suppose max-sat returns a soltuion S. Then we need to find an output trnasformation h such that h(S) is a valid solution to the instance I of 3SAT problem (A). Since n' = n, CNF = CNF3, g = m, this means the soltuion to max-sat problem must have at least m satisfying clauses. Since there are only m clauses, this means all clauses are satisfied. Therefore, The output instance S is equivalent to the output instance I of 3SAT problem. Therefore, no transformation needed.

4. direction 1 -> If A has a soltuion then B has

If 3SAT problem has a solution, meaning all m clauses are satisfied. Because g = m and CNF = CNF3, if m clauses are satisfied, then at least g clauses satisfied. Therefore, if A has a solution, then B has.

5. direction 2 -> If B has a soltuion then A has

If B has a solution, then at least g clauses are satisfied. Since there are only g clauses and g = m, the CNF3 in problem A has a solution too. 



d. [x] Dense subgraph - Given a graph and 2 integers a and b, find a set of a vertices of G such that there are at least b edges between them.

1. Verification

Given a candidate solution (i.e., a set of vertices, V') for the dense subgraph problem, we will need to do the followings to verify if this is a valid solution:

    1. check if |V'| = a
    2. for each node pair (u', v') in V', we count the number of node pair that are connected by an edge in the original graph G=(V,E) and see if the count >= b. 

This verification procedure will take O(|V'| + |V'|^2 * |E|), which is polynomial.

Next, we will use clique problem (A) to reduce to the dense subgraph problem (B).

2. input transformation f

We need to find an input transformation f such that f converts an input instance of A into an input instance of B. For problem A, let's denote the input instance as I = (G=(V,E)). To do the transformation, we:

    1. let a = |V|
    2. let b = |V| * (|V|-1) / 2
    3. let G' = G

Therefore, we have input instance for problem B, f(I) = (G'=(V, E), a, b)


3. output transformation h

Suppose problem returns a solution S, we need to find an output transformation h such that h(S) is a valid solution to problem A as well. According to the construction of the input transformation, we know that G' is a clique, meaning all nodes are directly connected. In a clique, the number of edges m can be represented as n*(n-1)/ 2 where n is the number of nodes. We only need to connect all vertex pairs for vertices in vertex set a. This will form a clique. This will take O(n^2) time which is polynomial.

4. direction 1 -> if B has a solution then A does

If we can find a set of vertices a from G' with at least b edges between them, this means we choose |V| nodes and at least |V|*(|V|-1)^2 edges. By definition, this forms a clique. 

5. direction 2 -> if A has a solution then B does

If graph G has a solution, meaning we can find a set of vertices a. And, each 2 vertices are directly connected, meaning there are |V| * (|V|-1) / 2 edges. Then problem B has a solution because it satisfies the requirement that $a$ vertices have at least (exactly) b (= a*(a-1)/2) edges. 


e. Sparse Subgraph - Given a graph and 2 integers a and b, find a set of a vertices of G such that there are at most b edges between them.

1. verification

Given 2 integers a and b and a graph G=(V,E), we want to have a set of vertices S such that |S| = a and at most b edges are between the vertices in S. Here's what we need to do to verify:

    1. check the size of S. Assume we can't directly get the length but have to do a linear scan. Then it will need O(|V|) time.
    2. for each node pair (u, v) in S, we check if there is an edge in G. And, see if the number of edges <= b. This will take O(|E|^2) time. 

So, the verification step takes polynomial time.


Next, we will find a reduction from the known independent set problem (A) to the sparse subgraph problem (B). For problem A: given an undirected graph G and integer k, find a set of vertices S such that there are at most k vertices and no edges between any two nodes in S.

2. input transformation f

Now, we can define the input transformation f as follows:

    1. let G' = (G=(V,E))
    2. let a = k
    3. let b = 0

Since we just simply copy the original graph G, the runtime for the input transformation is O(|V|+|E|) which is polynomial.


3. output transformation h

suppose the problem B returns a solution S, we want to find a transformation h such that h(S) is a valid solution to A. Since S contains a set of a vertices such that there are at most b edges between them, we don't need any transformation. The IS problem needs a set of vertices that does not form any edge, meaning b = 0. This is what we constructed. And, we want at least k vertices and a = k. Therefore, h(S) is a valid solution to A.

4. direction 1 -> if B has a solution then A does

If B has a solution, according to the construction, there must be a = k nodes and b = 0 edges between these nodes. Therefore, A must have a solution if B does.

5. direction 2 -> if A has a solution then B does

If A has a solution, then we can find an independent set with at least k size. There are no edges between any nodes in the independent set. This satisfies our construction.


g. Reliable Network - We are given 2 n x n matrics, a distance matrix d_ij and a connectivity requirement matrix r_ij, as well as a budget b; we must find a graph G = ({1, 2, ... n}, E) such that (1) the total cost of all edges is b or less and (2) between any two distinct vertices i and j there are r_ij vertex-disjoint paths. 






----

- [DPV 8.13]

Determine which of the following problems are NP-complete and which are solvable in polynomial time. In each problem you are given an undirected graph G = (V,E), along with:
(a) A set of nodes L ⊆V , and you must find a spanning tree such that its set of leaves includes the set L.  ---- np complete
(b) A set of nodes L ⊆ V , and you must find a spanning tree such that its set of leaves is precisely the set L.  ---- np complete
？？？？？？？(c) A set of nodes L ⊆ V , and you must find a spanning tree such that its set of leaves is included in the set L.  ---- np complete
(d) An integer k, and you must find a spanning tree with k or fewer leaves.  ---- np complete
？？？？？？？(e) An integer k, and you must find a spanning tree with k or more leaves.  ---- np complete
(f) An integer k, and you must find a spanning tree with exactly k leaves.  ---- np complete



----

- [DPV 8.14] Prove that the following problem is NP-complete: given an undirected graph G=(V,E) and an integer k, return a clique of size k as well as an independent set of size k, provided both exist.

1. verification

Given problem B and a candidate solution Y, we can verify it as follows:

    1. for each pair of nodes (u, v) in Y that has an edge, check if every pair of nodes has an edge between them and see if the number of nodes = k.
    2. For the remaining nodes, see if any two of them does not have an edge and see if there are k nodes.
    3. check, after removal, if both graphs have at least b nodes.

These will take O(|V|^2) time which is polynomial. We here use the strict upper bound |V| to represent the runtime.

2. input transformation f

IS problem (A). Input instance I = G0=(V0,E0), k0. We next need to transform I into a valid input instance to problem B.

    1. let G = G0 + G1, where G0=(V0, E0); G1 = (V0,E0_bar) (complement graph of G0)
    2. let k = k0

This will take O(|E|+|V|) time, which is polynomial.

3. output transformation h

The problem B returns a solution S which contains an independent set and a clique both in size k. The independent set found will be a valid solution to problem A. We only need to remove the clique while keep the IS part. This takes O(|V|+|E|) time.

4. direction 1 -> if A has a solution, then B does

If A has a solution, meaning we can find an IS from G0=(V0,E0) with size k. Hence, we can find the same IS for problem B. According to the reduction from IS to Clique, we know that the clique found from G1 will be in size k as well. Therefore, we found an IS and a clique both in size k for the problem B. Hence B has a solution too.

5. direction 2 -> if B has a solution, then A does.

As mentioned, if B has a solution, then we will find an IS from G0 part and a clique from the G1 part. After removing the clique in G1, we guarantee there's an IS which is identical to the expected IS by problem A. Therefore A has a solution too.


----

- [DPV 8.15] Show that the following problem is np-complete:

MAXIMUM COMMON SUBGRAPH (MCS)

    - input: two graphs G1 = (V1, E1); G2=(V2,E2)
    - output: 2 set of nodes V′1 ⊆ V1 and V′2 ⊆ V2 whose deletion leaves at least b nodes in each graph, and makes the 2 graphs identical

1. verification

we can verify a candidate solution y of MCS problem as follows:

    1. remove nodes of V'1 from V1 and get the remaining graph G1'
    2. remove nodes of V'2 from V2 and get the remaining graph G2'
    3. compare if G1' and G2' is identical

This will take O(|V1'| + |V'2| + |V| + |E|) time to verify, which is polynomial.

2. input transformation f

The Clique problem (A) has an input instance of I = G=(V,E) and k, where we want to find a clique of at least size k from graph G. We can do the transformation as follows:

    1. G1 = G=(V,E)
    2. G2 = fully connected G. G2=(V, E2) where E is a subset of E
    3. b = k

This transfromation will take O(|V|*2) to complete, which is polynomial.

3. output transformation h

Suppose problem B returns a solution S, we let C = G1 without vertices in V'1. Return C as problem A's solution. C takes O(|V|) time which is polynomial. If B has no solution, return no solution for problem A.

4. direction 1 -> if B has a solution then A does

By setting G2 as a fully connected graph with V vertices, in this way, no matter which vertices were removed from G2, the remaining graph will always be a clique. In G1, since G1 = G, after removing V'1 vertices, the remaining graph will be a clique and will be identical with the remaining graph of G2. Also, the remaining G1 will be the clique can be found from G. Therefore if B has a solution, then A does.

5. direction 2 -> if A has a solution then B does.

Since we made G=G1, therefore, if finding clique from G or G1 is the same question. By setting G2 as a fully connected grpah with V vertices, this guarantees that G1 is a subgraph of G2. So, we simply trim vertices till we get the same graph as the remaining G1. In this way, if A has a solution, then B does.

----

- [DPV 8.17] show that for any problem II in NP, there is an algorithm which solves II in time $O(2^{p(n)})$, where n is the size of the input instance and p(n) is a polynomial (which may depend on II)





----

- [DPV 8.1]

The search version TSP problem is np-complete. The optimization version of the same problem has at most the same difficulty as the search version of TSP. This means, if NP-complete TSP has a polynomial time solution, then the optimization version of TSP has a polynomial time solution too



----

- [DPV 8.2] search versus decision. Suppose you have a procedure which runs in polynomial time and tells you whether or not a graph has a Rudrata path. Show that you can use it to develop a polynomial time algorithm for RUDRATA PATH (which return the actual path, if it exists).

a rudrata path problem is defined as: given an undirected graph G=(V,E), we want to find a path that passes each vertex in V exact once.

the given procedure (A) says: given an undirected graph G=(V,E), A is able to tell whether there is a Rudrata path in G.

we can run A multiple times. Each time, we determine whether a subgraph G' of G has a valid rudrata path in size k or not. Since the size of G is polynomial, this means, we will need to run A polynomial times to find a valid rudrata path. Therefore, to find the final rudrata path for G, we run polynomial times A, which will finally be polynomial time too.

【写的算法不够清楚。这里可以逐个边添加。即，每次引入一条没被 A 判断过的边，然后看新图中有没有rudrata path，如果有则保留这条边，继续看下一条边。如果没有则不要这条边，继续看下一条边】所以最后是poly * poly的时间，最后还是poly




----

- [DPV 8.3] Stingy SAT is the following problem: given a set of clauses (each a disjunction of literals) and an integer k, find a satisfying assignment in which at most k variables are true, if such an assignment exists. Provie that Stingy SAT is np-complete

1. verification

denote that we have n literials and m clauses. We are also given an integer k. Now, we want to verify if a candidate solution is a valid solution. The candidate solution is an assignment of literals. To verify, we do:

    1. calculate each clauses boolean value by using the assignment of literals
    2. count the number of literals whose value is true. And, see if the number of such literals <= k

This will take O(nm) time to verify.

Next, we want to find a reduction from 3SAT to Stingy SAT (SS) problem. 

2. input transformation f

The input instance for 3sat problem is a CNF3 (meaning each clause has at most 3 literals). There are m clauses and n literals. We do the following transformation to 3sat's instance:

    1. let CNF = CNF3 (CNF means the input CNF for SS problem)
    2. k = n
    
This transformation takes O(nm) time because we only need to create the same CNF3 for SS.

3. output transformation h

The SS returns a solution assignment such that at most k literals are true. Therefore, no transformation needed.

4. direction 1 -> If SS has a solution, then 3SAT does

If we can find an assignment such that at most k literals are true, then all clauses are satisfied in CNF. So is CNF3 because CNF=CNF3. Therefore, if SS has a solution, then 3SAT does.

5. direction 2 -> If 3SAT has a solution, then SS does

If 3sat has a solution, then there are at most n literals are true. Because n = k, there are at most k true literals for SS problem. Therefore, SS has a solution too.

If 3SAT doesn't have a solution, then SS doesn't.

The completes the proof of np-complete for SS problem

----

- [DPV 8.8] In the EXACT 4SAT problem, the input is a set of clauses, each of which is a disjunction of exactly four literals, and such that variable occurs at most once in each clause. The goal is to find a satisfying assignment, if one exists. Prove that e4s is np complete.

【这个解不对。问题在于，从CNF3 -> CNF4的变换，应该是 (x1 v x2 v x3 v z1) ^ (x2 v x4_bar v x3 v z1_bar)。 也就是要添加的是 值相异的 变量。 要给每个clause都添加，直到满足 E4S 为止，才能作为E4S问题的input instance】

1. verification

Given a CNF4 and an assignment A, we can do the follows to verify if A is a valid solution:

    1. calculate each clauses value see if they're all true

This will take O(nm) time, where n is the number of literals and m is the number of clauses in CNF4. This poly time.


Next, we need to find a reduction from 3sat (A) to e4s (B)

2. input transformation f

We can do this transformation f to the input instance of A:

    1. CNF4 = add a False value to each clause in CNF3. For example (x1 v x2 v x3 v false) .....

This will take O(nm) time to transform. 


3. output transformation h

Suppose problem B returns a solution (which is a valid assignment the satisfies the CNF4), this solution is a valid assignment to CNF3.

If there's no valid solution, then CNF3 doesn't either.

This takes O(1) time.

4. direction 1 -> If A has a solution, then B does.

Suppose A has a valid assignment, then each clause has at least 1 literal that is true. By adding a false to each clause, we force the CNF3 to be in CNF4 form. In this way, if A has a solution, then B does.


5. direction 2 -> If B has a solution, then A does.

Key observation: The newly added false values to each clause doesn't affect the final solution. Therefore, if B has a solution, then A does.

This completes the proof.



----

- [DPV 8.19] a kite is a graph on an even number of vertices, say 2n, in which n of the vertices form a clique and the remaining n vertices are connected in a "tail" that consists of a path joined to one of the vertices of the clique. Given a graph and a goal g, the KITE problem asks for a subgraph which is a kite and which contains 2g nodes. Prove that KITE is np complete.

【这题的关键点在于，一个是要自己创建一个k-tail；第二个是要将k-tail的一个叶节点 与 clique问题的 G=(V,E) 中的所有节点 都添加一条边相连，这样是确保即使是在不知道clique 在G的什么地方的情况下，也能保证 k-tail 连接到了 clique】


1. verification

given a graph G=(V,E) and a goal g, we want to verify if a given candidate G' is a subgraph of G such that G' is a kite. we can do these to verify:

    1. check if the total nubmer of nodes in G' is 2g
    2. check if G' is a subgraph of G
    3. partition V into C and T and see if |C| = |T| = g
    4. check if C forms a clique
    5. check if T forms a tail
    6. check if there's only 1 edge connects C and T

If all satisfied, then G' is a valid solution. This will take O(|V|+|E|+g^2) time

We want to find a reduction from Clique problem (A) to kite problem (B)

2. input transformation

The input instance for problem A is I= (G=(V,E), k), where we want to find a clique  from grpah G such that the size of the clique is at least k. We can do the following transformation to form an input instance for problem B:

    1. Add a tail T in size g to G=(V,E), G is a k-clique.
    2. g = k

This transformation, since a new graph is created, will take O(|V|+|E|) time.

3. output transformation

Suppose problem returns a solution S. This will be a graph G with g sized clique and g size tail. Next, we find g connected nodes whose degree <= 2. The remaining graph will be a clique with size g.

This will take O(|V|) time 

4. direction 1 -> if B has a solution, then A does

Suppose B has a solution, this means we have a graph G' which contains a g-clique and g-tail. By output transformation and removing the g-tail, we ensure there is a g-clique which is identical to A's solution.

5. direction 2 -> if A has a solution, then B does

Suppose A has a solution, this means we have a clique at least k size. Since we added a g-tail to the original graph G, this guarantees a kite with g-clique and g-tail exists. Therefore, if A has a solution, then B does.

Therefore, this completes the proof.


- [DPV 8.6] we saw that 3sat remains np-complete even when restricted to formulas in which each literal appears at most twice.

(a) show that if each literal appears at most once, then the problem is solvable in polynomial time.

If each literal appears at most once, this means all clauses' length in CNF is at most 1. This further means, we only need to calculate and ensure each literal value is true. This problem becomes solvable in poly time. 

(b) show that IS remains np-complete even in the special case when all the nodes in the graph have degree at most 4.

All nodes in the graph have degree at most 4, meaning we should reduce from 4SAT to IS4 problem. Since 4SAT is np complete, IS4 is np complete too.



- [DPV 8.9] Hitting set problem - we are given a family of sets {S1, S2, ... Sn} and a budget of b. We want to find a set of H of size <= b which intersects every Si, if such an H exists. In other words, we want $H\cap S_i \neq \emptyset$ for all i. Show that Hitting set problem (HS) is np complete.


1. verification

Given a candidate solution H, we want to verify if H is a valid solution to HS problem. Here's what we should do:

    1. check the size of H and see if it's <= b
    2. check, for each set Si in S = {S1, S2, ... Sn}, check if at least 1 element of Si exists in H

This will take O(nm) time, where m represents the max length of Si. This is polynomial.


Next, we want to find a reduction from VC to HS problem

2. input transformation

The input instance for VC problem is I = (G=(V,E), k). And, we want to find a set of vertices C such that at least 1 ending point of every edge in G appear in C. And, we want to find at most k nodes in C. Therefore, we can do a transformation below:

    1. For each vertex vi in V, we create a set Si. In graph G, we add all adjacent vertices of vi into Si. Then, add vi into Si.
    2. b = k

This transformation will take O(|V| + |E|) time as we traversed the whole graph. This is poly time.

3. output transformation

Suppose HS problem returns a set H of size <= b. We can do this transformation:

    1. for each element Hi in H, add it to a vertex set S. S will be the VC set with at most b size.
If such H doesn't exist, then VC problem returns No.

This will take O(k) time, poly time too.

4. direction 1 -> If HS has a solution, then VC has a solution

Key observation is that the input transformation essentially regards the family of sets S as an adjacenty list. It builds a transforation from an undirected graph G=(V,E) to an adjacency list. Therefore, the problem is essentially searching for a set of vertices that can cover all edges in G, which is identical to the definition of VC. Therefore, if HS has a solution, then VC has a solution. 

5. direction 2 -> If VC has a solution, then HS has a solution.

Suppose VC has a solution, then we can find a vertex set C such that all edges in G has at least 1 ending point occur in C, where |C| <= k. This is identical to the HS problem because we want to find a set H such that at least one of its elements occurs in every set Si. 

This completes the proof.

---

- [DPV 7.1] consider the following linear program:

maximize 5x + 3y

s.t.
    * 5x - 2y >= 0
    * x + y <= 7
    * x <=5
    * x >= 0
    * y >= 0

convert to the standar form:

maximize 5x + 3y

s.t.
    * -5x + 2y <= 0
    * x + y <= 7
    * x <=5
    * x >= 0
    * y >= 0


- [DPV 7.4] Moe is deciding how much regular duff beer andhow much duff strong beer to order each week. Regular duff costs Moe $1

maximize R + 1.5 * S

s.t. R + S <= 3000
     -R <= -2S
     R, S >= 0


- [DPV 7.5]

maximize (7-1.4-4)F + (6-0.6-2-2)H

s.t. F + 2H <= 240000
     1.5F + H <= 180000
     F <= 110000
     F, H >= 0



- [DPV 7.6]





- [DPV 7.11]





- [DPV 7.12]


- [HW 9] a flower of size N is a graph with exactly N+4 vertices such that N vertices from a clique, and the other 4 form a star connected to the clique by exactly 1 edge to the star's central vertex. Consider the flower problem:

- input: a graph G = (V,E) and a natural number N>0
- ouput: a set of N+4 vertices such that the induced subgraph is a flower, or report NO if such a set doesn't exist.

Show that the flower-search problem is np complete


1. verification

Suppose we have a candidate solution S to the flower-search problem, we need to:
    
    1. check if there are exactly 3 nodes whose degree = 1.
    2. remove the 3 nodes and their connected edges. check if the remaining graph G' has only 1 edge e' whose degree = 1
    3. remove e' and get the remaining graph G''. In G'', check if every two nodes has an edge directly connects them.
    4. check if |S| = N+4

This will take O(|V|+|E|) time because we traversed all nodes and edges in G.

Next, we want to find a reduction from known Clique problem to the unknown flower problem.

2. input transforamtion

An input instance to the Clique problem is an undirected graph G=(V,E) and an integer k. We want to find a clique with at least k nodes. Here's the transformation we can do:

    1. create a "star" and connect "star"'s center to every vertex on G. This way, we get a new graph G'
    2. N=k

Since we created a new graph, the runtime is O(|V|+|E|). This is poly

3. otuput transformtion

Suppose the flower problem returns a solution, which is a set of N+4 vertices that forms a "Clique+Star" structure, then we can simply remove the "Star" and the edge that connects the "star" and "clique". The remaining graph will be a clique and will be identical to the Clique problem's expected solution. This will take O(|V|) time if we don't know where the "star" is. 

4. direction 1 -> If B has a solution, then A does

The flower problem will return a "Clique+Star" structure, then we can simply remove the "Star" and the edge that connects the "star" and "clique". The remaining graph will be a clique and will be identical to the Clique problem's expected solution. If there's no such "Clique+Star" structure, then there's no Clique, therefore the Clique problem has no solution either.

5. direction 2 -> If A has a solution, then B does

The Clique problem returns a clique. By connecting the star's center to every vertex in G=(V,E), we guarantee at least 1 node of the clique in G will be connected directly with the star if clique exists. Therefore, if A has a solution, then B does.



---

[HW 10] Consider the white and gold path problem:

- input:
    - an undirected graph G=(V,E)
    - a vertex t
    - the minimum number of gold vertices g > 2
    - the minimum number of white vertices w > 2
    - a list c[] representing every vertex's color [accessible in O(1) time].

- output
    - all gold vertices come before any white vertices
    - at least g vertices are gold
    - at least w vertices are white
    - all colored vertices are present in the path

prove that the white and gold problem is np complete


1. verification


2. input transformation


3. output transformation


4. direction 1


5. direction 2




























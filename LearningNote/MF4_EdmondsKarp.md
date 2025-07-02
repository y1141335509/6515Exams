
# 10. Edmonds-Karp ALgorithm

## 10.0. 回顾

Ford-Fulkerson Algorithm

1. Set $f_e=0$ for all $e\in E$
2. Build residual network $G^f$
3. Check for st-path $P$ in $G^f$ using BFS or DFS
4. If no such path, return $(f)$.
5. Let $c(P)$ be the minimum capacity along $P$ in $G^f$
6. Augment $f$ by $c(P)$ units along $P$
7. Repeat 2-6 until no st-path in $G^f$


## 10.1.

在Edmonds-Karp算法中，我们默认使用BFS。Ford-Fulkerson中，BFS、DFS都可以。
































































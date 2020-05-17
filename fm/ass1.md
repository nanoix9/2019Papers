---
title: ENSE803 Assessment 1 Algebraic Specifications
author: "Stone Fang (Student ID: 19049045)" 
header: "ENSE803 Assessment 1 Algebraic Specifications"
footer: "Stone Fang (19049045)"
# bibliography: [ass1.bib]

# pagestyle: "empty"
papersize: a4
# mainfont: Times New Roman
# fontsize: 12pt
linestretch: 1
geometry:
    - margin=25mm

header-includes:
    - \def\Q{\mathbb{Q}}
    - \def\Z{\mathbb{Z}}

---

# The Rational Numbers

The set $\Q$ of rational numbers is defined by $\Q = \left\{ (p, q)~|~p, q \in \Z \mbox{~and~} q \neq 0 \right\}$. Then, for two elements $(p_1, q_1), (p_2, q_2) \in \Q$ we can have

Definition of equality: 

$$ (p_1, q_1) = (p_2, q_2) \mbox{~if, and only if~} p_1 q_2 = p_2 q_1 $$

Definition of operations 

- Addition($+$): $(p_1, q_1) + (p_2, q_2) = (p_1 q_2 + p_2 q_1, q_1 q_2)$

- Additive inverse($-$): $- (p, q) = (-p, q)$

- Multiplication($\cdot$): $(p_1, q_1) \cdot (p_2, q_2) = (p_1 p_2, q_1 q_2)$

- Multiplicative inverse($()^{-1}$): $(p, q)^{-1} = (q, p) \mbox{~if~} p \neq 0$

A function $\phi: \Z \rightarrow \Q$ is defined as $\phi(x) = (x, 1)$. Then we can have

- $\phi(x+y) = (x+y, 1) = (x \cdot 1 + y \cdot 1, 1 \cdot 1) = (x, 1) + (y, 1) = \phi(x) + \phi(y)$

- $\phi(-x) = (-x, 1) = -(x, 1) = -\phi(x)$

- $\phi(x \cdot y) = (x \cdot y, 1) = (x \cdot y, 1 \cdot 1) = (x, 1) \cdot (y, 1) = \phi(x) \cdot \phi(y)$

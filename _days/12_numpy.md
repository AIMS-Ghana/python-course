---
title: Intro to `numpy`
math: yes
---

## First, Last Task

For the remainder of the course, you will be working on analyzing a system of
differential equations that forms the basis of a common family of problems:
the *SIR* model.

*SIR* stands for **S**usceptible-**I**nfectious-**R**ecovered (or sometimes
*R*emoved), and it is a basic *compartment* model of the spread of infection
in a population.

<div markdown="0">
\begin{eqnarray}
N &=& S + I + R
\\
\dot{S} &=& \mu N - \beta S I - \mu S
\\
\dot{I} &=& \beta S I - \gamma I - \mu I
\\
\dot{R} &=& \gamma I - \mu R
\end{eqnarray}
</div>

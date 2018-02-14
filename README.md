# Association-Rule-Analysis
## Algorithm
- Frequent itemset generation: generate all itemsets of which support ![img](http://latex.codecogs.com/svg.latex?%5Cge) minsup.
  - Definition of support:
  \begin{center}
  ![equation](<img src="http://www.sciweavers.org/tex2img.php?eq=%20s%28X%20%5Crightarrow%20Y%29%3D%5Cfrac%7B%5Csigma%28X%20%5Ccup%20Y%29%7D%7BT%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" s(X \rightarrow Y)=\frac{\sigma(X \cup Y)}{T} " width="165" height="43" />)
  \end{center}

- Rule generation: generate high confidence rules from each frequent itemset, where each rule is a binary partitioning of a frequent itemset. 

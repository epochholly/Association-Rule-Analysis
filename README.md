# Association-Rule-Analysis
## Algorithm
- Frequent itemset generation: generate all itemsets of which support ![img](http://latex.codecogs.com/svg.latex?%5Cge) minsup.
  - Definition of support: 
  - Definition of confidence: 
![img]http://www.sciweavers.org/tex2img.php?eq=%20c%28X%20%5Crightarrow%20Y%29%3D%5Cfrac%7B%5Csigma%28X%20%5Ccup%20Y%29%7D%7B%5Csigma%28X%29%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0[/img]

- Rule generation: generate high confidence rules from each frequent itemset, where each rule is a binary partitioning of a frequent itemset. 

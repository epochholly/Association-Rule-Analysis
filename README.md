# Association-Rule-Analysis
## Algorithm
- Frequent itemset generation: generate all itemsets of which support $\ge$ minsup.
  - Definition of support: $s(X\rightarrow Y) = \frac{\sigma(X\cup Y)}{T}$
  - Apriori principle: if an itemset is frequent, then all of its subsets must also be frequent. If an itemset is found infrequent, then all the supersets are infrequent as well. It is a support-based pruning to remove itemsets having low support.
  - Algorithm:
    - let $k=1$
    - generate frequent itemsets of length 1
    - repeat until no new frequent itemsets are identified
      - generate lenght $k+1$ candidate itemsets from length $k$ frequent itemsets
      - prune candidate itemsets containing subsets of length $k$ that are infrequent
      - count the support of each candidate by scanning the database
      - eliminate candidates that are infrequent, leaving only those that are different
 
- Rule generation: generate high confidence rules from each frequent itemset, where each rule is a binary partitioning of a frequent itemset. 
  - Definition of confidence: $c(X\rightarrow Y) = \frac{\sigma(X\cup Y)}{\sigma(X)}$
  - For each itemset, the confidence of rules generated from the same itemset satisfying: 
  $c(BCD\rightarrow A)\ge c(BC\rightarrow AD)\ge c(B\rightarrow ACD)$. If $c(BCD\rightarrow A)$ is low confident, then all others are low in confidence as well.
  
## Data
The dataset is from a foodmart database. The transactions are recoded with simpler format. The product table can be used for reference.



  

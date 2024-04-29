# **Misaka_algorithm**  

## **Misaka_algorithm**   
This is an algorithm based on the Misaka Network, which is established in the context of the scientific railgun.   
The idea is that when sisters engage in battles, the results are uploaded to the Misaka Network.   
Although the sisters may die, the outcomes of each battle are recorded. Subsequently,   
based on the results of previous battles, the sisters determine how the battles should be updated,   
enabling them to collectively defeat the enemy.  

### Algorithm Process
1. Establish a group of sisters.
2. Sisters engage in battles sequentially.
3. Upload battle results to the Misaka Network.
4. Determine if a sister has died.
5. If no sister has died, proceed to battle with the next sister. If a sister has died, return to step 2.
6. Continue until the enemy is defeated (convergence), or the sisters are depleted. Then, the algorithm concludes and reports the best outcome.



### Battle Method
The Misaka sisters wield F2000R assault rifles as their combat weapons.  
Within the Misaka Network, records of each battle are kept, but this algorithm only retains the best outcome from all battles.  
In this algorithm, one battle refers to firing one shot.  
  
At the beginning, a random point is designated within the space as the initial reference point and recorded in the Misaka Network.   
During battles, one to five shots are randomly fired into the space.   
There is a 70% chance that each shot will be fired towards the vicinity of the aforementioned reference point,   
or towards another randomly selected point within the specified space. After each shot is fired, it is compared with the reference point.   
If the shot is closer to the target, the reference point is updated to the target of this shot;   
otherwise, the reference point remains unchanged.  
  
So, during each battle, the algorithm evaluates whether the outcome surpasses the best result recorded so far.   
If it does, the next battle will incorporate improvements based on the current battle's outcome.

Since it's necessary to set boundaries for randomly generated points within the specified space,  
we can define the search distance for each dimension as:     
  ~~~
  (Upper Bound - Lower Bound) * 0.05
  ~~~
  Therefore, the search range is:
  ~~~
  [Reference Point - Search Distance, Reference Point + Search Distance]
  ~~~
  Or you can define the Search Distance independently


    
  
### 死亡判定  
Misaka sisters often face high mortality rates during battles due to insufficient combat abilities,   
mistimed decisions, ~~or be killed by Accelerator~~.
Initially, the mortality rate of the sisters is 0.99.  
However, during the course of battles, sisters who survive against the odds can pass on their experience to future sisters.  
Ultimately, we aim for the mortality rate of the sisters to decrease to around 30%.   
Additionally, the mortality rate will only decrease when a sister survives. The calculation method for the mortality rate is as follows:

```
Current Mortality Rate = 0.69 * exp(-gamma * Cumulative Number of Surviving Sisters) + 0.3
```

The source of 0.69 is derived from subtracting the final 30% mortality rate from the initial 99% mortality rate.
Gamma represents the decay rate of the mortality rate, and it is recommended to set it to 0.001. 
Therefore, as the number of times sisters survive increases, their survival rate becomes higher.

***  
## Reference  
Particle Swarm Optimization   
Bat Algorithm  
Grey Wolf Optimizer  

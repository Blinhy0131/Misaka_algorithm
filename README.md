# **Misaka_algorithm**  

## 程式碼將在5/2公開
## Code will public at 5/2

## **御坂美琴演算法**  
是一種基於科學超電磁炮中，御坂妹妹們的御坂網路所建立的演算法  
其構想是妹妹在對戰時，將戰鬥結果上傳至御坂網路  
雖然妹妹們會死亡，但是戰鬥每次戰鬥的結果會記錄下來  
而後續妹妹們會根據前幾次戰鬥結果判斷戰鬥應該如何更新  
進而一起擊敗敵人。  

### 演算法流程
1. 建立一群妹妹
2. 妹妹們依序上場戰鬥
3. 將戰鬥結果上傳至御坂網路
4. 判定妹妹是否死亡
5. 若沒有死亡則與下一個妹妹一起戰鬥，若死亡回到步驟二
6. 直到敵人死亡(收斂)，或妹妹們用光，則演算法結束，回報最佳結果



### 戰鬥方式
御坂妹妹手持F2000R衝鋒槍，作為其戰鬥用的武器  
御坂網路內則是有每次戰鬥的紀錄，但本演算法只記錄最好的一次戰鬥結果  
本演算法中，一次戰鬥指的是開一槍為一次戰鬥  
  
一開始，會隨機在空間內指定一點作為基礎的參照點記錄在御坂網路內  
戰鬥時朝著空間內隨機開一到五槍  
開槍時有70%的機率會朝著前述所提到的參照點周圍進行開槍  
或者朝著指定空間中隨機開槍
每次開槍會與參照點進行比較  
如果比較接近目標，則參照點會更新成這次開槍的目標  
反之參照點不便  
  
所以在每次戰鬥的過程中
都會評估這次戰鬥是否有比最佳戰鬥的結果好  
如果有的話下一次戰鬥就會參考本次戰鬥的結果進行改良  

而'在參照點周圍'的定義方式有兩種  
#### 方法一    
  由於指定空間隨機產生點一定要設定邊界  
  所以我們可以將每個維度的搜索距離設定成
  ~~~
  (上邊界-下邊界)*0.05
  ~~~
  所以搜索範圍為  
  ~~~
  [參考點-搜索距離,參考點-搜索距離]
  ~~~
#### 方法二
  自行定義搜索距離  
  然後重複方法一的搜索範圍公式  



    
  
### 死亡判定  
御坂妹在戰鬥的時候很常因為戰鬥能力不足  
誤判時機，~~或是被一方殺死~~  
導致妹妹在戰鬥的過程中死亡率很高  
一開始妹妹的死亡率為0.99
而在戰鬥過程中，幸運存活下來的妹妹可以把存活的經驗交給未來的妹妹  
在最後，我們期許妹妹的死亡率約落在30%左右  
並且只有妹妹存活下來的時候  
才會降低死亡率  
死亡率計算方式為  

```
當前死亡率=0.69*exp(-gamma*累計存活下來妹妹個數)+0.3
```

0.69的來源是一開始的99%減掉最終的30%  
gamma是死亡率的衰減速度 建議設定為0.001  
所以當妹妹存活次數越多，則妹妹們的存活率更高。  


***  
## Reference  
Particle Swarm Optimization   
Bat Algorithm  
Grey Wolf Optimizer  

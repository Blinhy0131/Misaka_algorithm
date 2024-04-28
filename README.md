# **Misaka_algorithm**  

## **御坂美琴演算法**  
是一種基於科學超電磁炮中，御坂妹妹們的御坂網路所建立的演算法  
其構想是妹妹在對戰時，將戰鬥結果上傳至御坂網路  
雖然妹妹們會死亡，但是戰鬥每次戰鬥的結果會記錄下來  
而後續妹妹們會根據前幾次戰鬥結果判斷戰鬥應該如何更新  
進而一起擊敗敵人。  

## 演算法流程
1. 建立一群妹妹
2. 妹妹們依序上場戰鬥
3. 將戰鬥結果上傳至御坂網路
4. 判定妹妹是否死亡
5. 若沒有死亡則與下一個妹妹一起戰鬥，若死亡回到步驟二
6. 直到敵人死亡(收斂)，或妹妹們用光，則演算法結束，回報最佳結果


## 戰鬥方式
御坂妹妹手持F2000R衝鋒槍，作為其戰鬥用的武器  
御坂網路內則是有每次戰鬥的紀錄，但本演算法只記錄最好的一次戰鬥結果  
本演算法中，一次戰鬥指的是開一槍為一次戰鬥  
  
一開始，會隨機在空間內指定一點作為基礎的參照點記錄在御坂網路內  
戰鬥時朝著空間內隨機開一到五槍  
開槍時會朝著前述所提到的參照點周圍進行開槍  
每次開槍會與參照點進行比較  
如果比較接近目標，則參照點會更新成這次開槍的目標
反之參照點不便  
  
所以在每次戰鬥的過程中
都會評估這次戰鬥是否有比最佳戰鬥的結果好  
如果有的話下一次戰鬥就會參考本次戰鬥的結果進行改良  

***  
## Reference  
Particle Swarm Optimization   
Bat Algorithm  
Grey Wolf Optimizer  

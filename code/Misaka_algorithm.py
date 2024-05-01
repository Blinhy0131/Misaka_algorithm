import numpy as np


# curve function
def fun(t,x):
    y=x[0]*np.sin(2*np.pi*x[1]*t)*np.exp(t*x[2])
    return y


# this is the mean square function
# return the mse
def mse_fun(target,t,x):
    y=fun(t,x)
    mse=np.mean((target-y)**2)
    return mse



# This is a curve fitting finding the x in curve x1*sin(2*pi()*t*x2)+exp(t*x3)
# cost function using the mean square error

# input describion
# t             is the X data about the curve, or time
# target        is the y data about the curve,
# range         ub and lb is the bounary of th surching range
# sisters_nem   is the sisters number, or iter 
# gamma         is the decay speed about the sisters' died rand
# target_mse    the error is mse , if lower than end the algorithm

def Misaka_algorithm(t ,
                     target ,
                     range_ub,
                     range_lb ,
                     sisters_nem=20000,
                     gamma=0.001, 
                     target_mse=1e-3):

    
    
    #creat sisters
    
    searh_range=(range_ub-range_lb)*0.05

    fight_sister_number=1

    #first shot
    sisters_shot=np.random.uniform(range_ub,range_lb)

    mse=mse_fun(target,t,sisters_shot)

    #last order record the local best(global best) and the best value
    #last order=[best value,best position]
    last_order=[mse,sisters_shot]
    die_rand=0.99
    died_sister_nem=0
    alive_sister_nem=0
    final_die_rand=0.3
    die_diff=die_rand-final_die_rand
    


    for fight in range(sisters_nem):

        
        #battle(shot)
        #if there is more than one sister
        for i in range(fight_sister_number):

            # sister will shot random 1-5 shot
            for j in range(np.random.randint(1,6)):

                #frist shot in each iter and the 70% rand will seach the local best
                if ( i==1 and j==1 ) or (np.random.rand()<0.7):
                    sisters_shot=np.random.uniform(last_order[1]+searh_range,last_order[1]-searh_range)

                #else will random shot 
                else:
                    sisters_shot=np.random.uniform(range_ub,range_lb)
                
                #score the shot lower is better
                mse=mse_fun(target,t,sisters_shot)

                if mse<last_order[0]:
                    last_order[0]=mse
                    last_order[1]=sisters_shot

            
        #die or not
        dead_nember=0
        alive=False
        for i in range(fight_sister_number):
            randd=np.random.rand()
            if randd<die_rand:
                dead_nember+=1
                died_sister_nem+=1
                
            # die rand= 0.66*exp(-0.0001*alive sister nem)+0.3
            elif alive==False :
                alive_sister_nem+=1
                die_rand=die_diff*(np.exp(-gamma*alive_sister_nem))+final_die_rand;
                alive=True
                
        fight_sister_number-=dead_nember
        
        # print 
        print(f'第{fight+1}次戰鬥，戰鬥妹妹數:{fight_sister_number+1}，戰鬥結果為{last_order[0]}')
        
        if last_order[0]<target_mse:
            print('目標死亡，終止實驗')
            print(f'共{fight+1}次實驗，累計消耗:{died_sister_nem}個妹妹')
            break
        
        fight_sister_number+=1

    return last_order


def test():
    #we creat a test data to test the algorithm
    ans=[3,5,-0.7]
    t=np.arange(0,10.01,0.01)
    target=fun(t,ans)


    last_order=Misaka_algorithm(sisters_nem=20000,
                                 t=t,
                                 target=target,
                                 range_ub=np.array([10,10,0]),
                                 range_lb=np.array([0,0,-10]),
                                 gamma=0.001,
                                 target_mse=1e-3)


    #print the anser and the error
    print(f'預測結果為:{last_order[1]}')
    print(f'實際答案是{ans}')
    print(f'mse={last_order[0]}')



if __name__ == '__main__':
    test()

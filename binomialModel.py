from math import exp
import math
import matplotlib.pyplot as plt
import numpy as np

# Entrer les variables :
call = raw_input("Is this a call or put option? (C/P) ").upper().startswith("C")
american = raw_input("Is it an American or European option ? (A/E) ").upper().startswith("A")
T= input("Enter the Time in months : ")
dt = input("Enter the number of timesteps: ")
S = input("Enter the initial asset price: ")
r = input("Enter the risk-free discount rate: ")
K = input("Enter the option strike price: ")
w = raw_input("Do you have a given volatility ? (Y/N) ").upper().startswith("Y")
if w == True :
   v = input("Enter the value of volatility between 0 and 1: ")
   T = T + 0.00000000001
   T = T - 0.00000000001
   T = round( T /(12*dt), 20)
   u = round(math.exp(v*math.sqrt(T)),4)
   print(u)
   d = round(1/u,4)
   print(d)
   A= S
   B= S*(u)
   B= round(B,3)
   D= S*((u)**2)
   D=round(D,3)
   
   C= S*(d)
   C=round(C,3)
   F=S*(d)**2
   F=round(F,3)
   
   E= S*u*d
   E=round(E,3)
   
   print(" price per node :")
   print(A,B,C,D,E,F) 
   
   z= math.exp(r*T)
   
   p= round((z-d)/(u-d) , 4)
   print("value of p: " + str(p))
   
   # CALL
   if call == True :
    	C_value = 0
    	D_value = D - K
    	if E > K :
    		E_value = E - K 
    	else :
    		E_value = 0
    	F_value = 0
    	B_value = round(D_value * p * math.exp(-r*T) , 3)
    	A_value = round(B_value * p * math.exp(-r*T), 3)
   
   #PUT
   else :
     	
    	
    	if D > K :
    		D_value = 0
    	else : 
    		D_value = K - D
    	if E > K :
    		E_value = 0
    	else :
    		E_value = K - E 
    	F_value = K - F
    	B_value = round(((D_value*p)+(E_value*(1-p))) * math.exp(-r*T) , 3)
    	C_value = round(((E_value*p)+(F_value*(1-p))) * math.exp(-r*T) , 3)
    	A_value = round(((B_value*p)+(C_value*(1-p))) * math.exp(-r*T), 3)
     	
   
   
   
   print(A_value , B_value , C_value , D_value , E_value , F_value)
   
   print("value of option per node : ")
   print(" A : " + str(A_value))
   print(" B : " + str(B_value))
   print(" C : " + str(C_value))
   print(" D : " + str(D_value))
   print(" E : " + str(E_value))
   print(" F : " + str(F_value))
   
   #Graphs and results for the Option prices
   
   plt.figtext(0.08,0.6,"Stock price=$"+str(S))
   plt.figtext(0.08,0.56,"call value="+str(A_value))
   
   plt.figtext(0.33,0.76,"Stock price=$"+str(B))
   plt.figtext(0.33,0.70,"Option value="+str(B_value))
   
   plt.figtext(0.33,0.36,"Stock price=$"+str(C))
   plt.figtext(0.33,0.30,"Option value="+str(C_value))
   
   plt.figtext(0.75,0.91,"Stock price=$"+str(D))
   plt.figtext(0.75,0.87,"Option value="+str(D_value))
   
   plt.figtext(0.75,0.6,"Stock price=$"+str(E))
   plt.figtext(0.75,0.57,"Option value="+str(E_value))
   
   plt.figtext(0.75,0.28,"Stock price=$"+str(F))
   plt.figtext(0.75,0.24,"Option value="+str(F_value))
   n=2
   plt.show()
else :



    u = input("Enter the asset growth factor u between 0 and 1: ")
    d = input("Enter the asset down factor d between 0 and 1: ")
    
    #Price per node
    
    d = 1-d
    u = 1+u 
    
    
    T = T + 0.00000000001
    T = T - 0.00000000001
    T= round( T /(12*dt), 20)
    # WTF POURQUOI T=0 ???
    
    A= S
    B= S*(u)
    B= round(B,3)
    D= S*((u)**2)
    D=round(D,3)
    
    C= S*(d)
    C=round(C,3)
    F=S*(d)**2
    F=round(F,3)
    
    E= S*u*d
    E=round(E,3)
    
    print(" price per node :")
    print(A,B,C,D,E,F) 
    
    z= math.exp(r*T)
    
    p= round((z-d)/(u-d) , 4)
    print("value of p: " + str(p))
    
    # CALL
    if call == True :
     	C_value = 0
     	D_value = D - K
     	if E > K :
     		E_value = E - K 
     	else :
     		E_value = 0
     	F_value = 0
     	B_value = round(D_value * p * math.exp(-r*T) , 3)
     	A_value = round(B_value * p * math.exp(-r*T), 3)
    
    #PUT
    else :
      	
     	
     	if D > K :
     		D_value = 0
     	else : 
     		D_value = K - D
     	if E > K :
     		E_value = 0
     	else :
     		E_value = K - E 
     	F_value = K - F
     	B_value = round(((D_value*p)+(E_value*(1-p))) * math.exp(-r*T) , 3)
     	C_value = round(((E_value*p)+(F_value*(1-p))) * math.exp(-r*T) , 3)
     	A_value = round(((B_value*p)+(C_value*(1-p))) * math.exp(-r*T), 3)
      	
    
    
    
    print(A_value , B_value , C_value , D_value , E_value , F_value)
    
    print("value of option per node : ")
    print(" A : " + str(A_value))
    print(" B : " + str(B_value))
    print(" C : " + str(C_value))
    print(" D : " + str(D_value))
    print(" E : " + str(E_value))
    print(" F : " + str(F_value))
    
    #Graphs and results for the Option prices
    
    plt.figtext(0.08,0.6,"Stock price=$"+str(S))
    plt.figtext(0.08,0.56,"call value="+str(A_value))
    
    plt.figtext(0.33,0.76,"Stock price=$"+str(B))
    plt.figtext(0.33,0.70,"Option value="+str(B_value))
    
    plt.figtext(0.33,0.36,"Stock price=$"+str(C))
    plt.figtext(0.33,0.30,"Option value="+str(C_value))
    
    plt.figtext(0.75,0.91,"Stock price=$"+str(D))
    plt.figtext(0.75,0.87,"Option value="+str(D_value))
    
    plt.figtext(0.75,0.6,"Stock price=$"+str(E))
    plt.figtext(0.75,0.57,"Option value="+str(E_value))
    
    plt.figtext(0.75,0.28,"Stock price=$"+str(F))
    plt.figtext(0.75,0.24,"Option value="+str(F_value))
    n=2
    plt.show()

#A nine-month American put option on a non-dividend-paying stock has a strike price of $49. 
#The stock price is $50, the risk-free rate is 5% per annum, and the volatility is 30% per annum. 
#Use a three-step binomial tree to calculate the option price

#u = e^volatilty*rc(T)







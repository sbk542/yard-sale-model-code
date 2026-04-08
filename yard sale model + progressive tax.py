# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:56:38 2026

@author: user
"""
import matplotlib.pyplot as plt
import random


agents = []

#parameters

NAgents=1000;
Money0=1000;
numberGames=50000;
wagerFactor=0.2;

#give everyone money
for i in range(0,NAgents):
    agents.append(Money0)

#simulate 1000 times
for i in range(0,numberGames):
    
    #select 2 random agents
    agentAindex = random.randint(0,NAgents-1);
    
    agentBindex = random.randint(0,NAgents-1);
    
    #make sure they are not the same agent
    while(agentAindex==agentBindex):
        agentBindex = random.randint(0,NAgents-1);

    #wager is fraction of poorer agent's wealth
    if(agents[agentAindex]<agents[agentBindex]):
        wager=wagerFactor*agents[agentAindex];
    else:
        wager=wagerFactor*agents[agentBindex];
        
    #random winner   
    winner = random.randint(0,1)
    
    #give money to winner
    if(winner==0):
     agents[agentAindex] = agents[agentAindex] + wager;
     agents[agentBindex] = agents[agentBindex] - wager;
    else:
        agents[agentAindex] = agents[agentAindex] - wager;
        agents[agentBindex] = agents[agentBindex] + wager;
        
#tax
    #find median
    if i % 10==0: #every 10 rounds
        sorted_agents = sorted(agents)
        median = len(agents)//2
    
        epsilon = 0.01 #how high redistributive tax is
        #move epsilon towards median
        for j in range(len(agents)):
            agents[j] += epsilon * (median - agents[j])

     


       
#plot
plt.hist(agents, bins=100)
plt.title("Wealth Distribution")
plt.xlabel("Wealth")
plt.ylabel("Number of Agents")
plt.show()
    
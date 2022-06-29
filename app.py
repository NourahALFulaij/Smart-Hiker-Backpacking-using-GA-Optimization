from re import L, S
import re
from secrets import choice
from subprocess import list2cmdline
from typing import List 
import random  
from collections import OrderedDict
# importing the required module
import numpy as np
import matplotlib.pyplot as plt

# item class
class Item:
  def __init__(self, name, weight, priority):
    self.name = name
    self.priority = priority
    self.weight = weight

# take value from user and valdit
def input_loop(text, options=None):
    while True:
        choice = input(text + '\n').strip()
        print()

        if options is None:
            if choice:
                return choice

            print('ERROR: Invalid input!')
        else:
            for option, value in options.items():
                if choice.lower() == option.lower():
                    return value

            print('ERROR: "{}" is an invalid choice!'.format(choice))


# ask for priority from sara
print('Please enter your priority of the following items:')

# item1
priItem1 = input_loop(
        'Sleeping bag:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item1 = Item("Sleeping bag", 10,priItem1)

# item2
priItem2 = input_loop(
        'Rope:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item2 = Item("Rope", 3,priItem2)

# item3
priItem3 = input_loop(
        'Pocket Knife:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item3 = Item("Pocket Knife", 2,priItem3)

# item4
priItem4 = input_loop(
        'Torch:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item4 = Item("Torch", 5,priItem4)

# item5
priItem5 = input_loop(
        'Water Bottle:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item5 = Item("Water Bottle", 9,priItem5)

# item6
priItem6 = input_loop(
        'Glucose:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item6 = Item("Glucose", 8,priItem6)

# item7
priItem7 = input_loop(
        'First aid supplies:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item7 = Item("First aid supplies", 6,priItem7)

# item8
priItem8 = input_loop(
        'Rain jacket:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item8 = Item("Rain jacket ", 3,priItem8)

# item9
priItem9 = input_loop(
        'Personal Locator Beacon:'
        ' (L for Low, M for Medium, and H for High).',
        {'L': 5, 'M':10,'H': 15})

item9 = Item("Personal Locator Beacon", 2,priItem9)

# Search space
items = [item1, item2, item3, item4, item5, item6, item7, item8, item9]

# createChrom: ex: [1,1,0,0,1,1,0,0,1]
def createChrom(list):# list is items
    # step 1 
    weight= 0 # totul weight 
    max= 30 # max weight
    newList=[] # new chrom is empty at start
    index=[0,1] # 0: the item is not picked, 1: the item is picked
    length = len(list)# lenght of the new chrom. in our case always 9
    j= 0 # for the loop. go over the chrom one by one

    # step 2
    while(j<length):
        # choose randemly wither the item is picked  1, or not 0
        i = random.choice(index)

        # if the item is picked => i=1. make sure the weight ok
        if i==1 and weight + list[j].weight<= max:
            # update weight
            weight+= list[j].weight
        else:# the item can't be picked
            i=0
        # add to the new chrom 
        newList.append(i)
        # update j 
        j+=1
    # return the new chrom
    return newList

# Compute_Fitness() function.
def Compute_Fitness(chrom):
    
    sum = 0 #totail of priority. 
    index= 0 # postion of the item in Item list. need it to access the priority of the item
    weight= 0 #totail of weight. to make sure the chrom weight is not more then the max 
    max= 30 # max weitht

    # priority
    for x in chrom:
        #if the item was selected => x=1.
        if x==1:
            # we add their priority to the sum of the priority point
            sum+= items[index].priority
            # update the totil weight 
            weight+= items[index].weight

        # update index to go to the next item in the chrom
        index+=1
    
    # weight
    if weight > max:
        sum=0 # if the weight is > then 30. it's not allowed therefore the sun (Fitness) is 0

    return sum # sum of Priority Points

# Create_Initial_Population
def Create_Initial_Population(length):# length = size of the pop
    # population empty 
    pop = []
    popFitness = []
    h= 0
   
    # create chrom 
    while h <length:
        #index in chrom ref to the item. to access the priorty, name and weight later.
        j=0 

        # create chrom 
        newList = createChrom(items)

        #compute chrom fitness
        chromFitness = Compute_Fitness(newList)

        # check if cheom is in list of pop
        if newList in pop:
            h-=1 # because we did not add the chrom, this loop don't count.
        elif chromFitness==0:
            h-=1 # because we did not add the chrom, this loop don't count.
        else:
            # add cheom to the list 
            pop.append(newList)
            popFitness.append(chromFitness)

            # print chrom (for run only)
            # for x in newList:
            #     if x==1:
            #         print(items[j].name)
            #     j+=1
            
            # for run only
            # print('Fitness: '+str(chromFitness)+'\n')
        h+=1

    return pop,popFitness

#Crossover
def Crossover(parents):
    chrom1 = parents[0]
    chrom2 = parents[1]
    # check if the chroms have the same lenght (not gone happend)
    if len(chrom1) != len(chrom2):
        return 
    #Single point Crossover randomly generated 
    crossPoint = random.randint(1,len(chrom1)-1)# chrom1.lenght= chrom2.lenght = child lenght 
    # crossPoint in chrom2
   # print(crossPoint)

    # generated offsprings
    offspring1 = chrom1[:crossPoint] + chrom2[crossPoint:]
    offspring2 = chrom2[:crossPoint] + chrom1[crossPoint:]
    return offspring1, offspring2

# Mutation
def Mutation(chrom):
    # check if the chrom empty? (not gone happend)
    if len(chrom) ==0:
        return 
    
    # mutation Point randomly generated 
    mutationPoint = random.randint(0,len(chrom)-1)
    #print(mutationPoint)

    # generated Mutation
    chrom[mutationPoint] = 1 - chrom[mutationPoint]
    # no need to return the chrom because the change reflict oridy because we pass the refrens value 


# Selection by roulette wheel selection. 
def Selection(pop,popFitness):
    fittSum = 0
    probability = []
    wheel = []
    i = 0

    # pop not empty (not happing)
    if pop:
        # step 1: probability
        for fitt in popFitness: 
            fittSum += fitt
        
       # print("\n probability")
        for chrom in pop: 
            # step 2: probability for each individual
            fitt = popFitness[i]
            i+=1
            probability.append(fitt/fittSum)
       
        
        index = 0
      #  print("\n probability2")
        for p in probability:
            if index != 0:
                wheel.append( wheel[index-1] + p )
                
            else: 
                wheel.append(p)
                
            index+=1
            
        # fanil
        r = random.uniform(0, 1)
        #print(r)
        index = 0
        for w in wheel:
            # index = 0
            if index == 0:
                if  r < wheel[index]:
                    return pop[index]
            else:
                if wheel[index-1] < r and r < w:
                    return pop[index]
            index+=1   

 
#Make sure to not get the same chrom as parent again 
def selectingParents(pop,popFitness):
    if len(pop) < 2 : return pop 
    parent1 = Selection(pop,popFitness)
    while True:
        parent2 = Selection(pop,popFitness)
        if parent1 != parent2:
            break
    return [parent1,parent2]    


def replacement(pop,newGen):
    mergePop = pop+newGen 
    fitnessList = []
    size = len(pop)
    newFitnessList = []
    finalGen = []
    i = 0

    #store the fitness in a list 
    for chrom in mergePop:
        fitnessList.append(Compute_Fitness(chrom))
    
    #sort the chroms based on their fitness
    for fitt in fitnessList:
        if i < size:
            maxFit = max(fitnessList)
            maxIndex = fitnessList.index(maxFit)
            chromosom = mergePop.pop(maxIndex)
            fitness = fitnessList.pop(maxIndex)
            if chromosom in finalGen:
                i-=1
            else:
                newFitnessList.append(fitness)
                finalGen.append(chromosom)
            i+=1
        else:
            break  
    return finalGen,newFitnessList



def evolution(pop,popFitness,numOfGen):
    newGen = []
    x = 0
    times =[]
    avrageFitness = []
    times.append(x)
    avrageFitness.append(avrage_fitness(popFitness))

    while x<numOfGen:
        # print(pop)
        # print(popFitness)
        for i in range(int(len(pop)/2)):
            #step1: selection
            parents = selectingParents(pop,popFitness)

            #step2: crossover
            offSprings = Crossover(parents)
            
            #step3: mutation
            j = 0
            while j<2:
                rand = random.randint(1, 100)
                if rand == 1:
                    Mutation(offSprings[j])
                j+=1
            
            #step4: add them to new gen
            newGen.append(offSprings[0])
            newGen.append(offSprings[1])
            
        #step5: replacment 
        repList = replacement(pop,newGen) 
        pop = repList[0]
        popFitness = repList[1]
        times.append(x)
        avrageFitness.append(avrage_fitness(popFitness))
        newGen = []
        # Terminate?
        if len(pop) ==1: 
            break
        
        x += 1  
    printSelotions(pop)
    buildGraph(times,avrageFitness) 
    # Done


#build graph 
def buildGraph(x, y ):
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('Generation')
    # naming the y axis
    plt.ylabel('Fitness')
    
    # giving a title to my graph
    plt.title('GA Preformance')
    
    # function to show the plot
    plt.show()

      
def avrage_fitness(fitness):
    sum = 0
    for fitt in fitness:
        sum += fitt
    
    return sum/len(fitness)

def printSelotions(selotions):
    index = 0
    
    for selotion in selotions:
        index = 0
        print("\nSelotion:")
        for item in selotion: 
            if item ==1:
                if index ==0: 
                    print("Sleeping bag, ")
                elif index == 1:
                    print("Rope, ")
                elif index == 2:
                    print("Pocket Knife, ")
                elif index == 3:
                    print("Torch, ")
                elif index == 4:
                    print("Water Bottle, ")
                elif index == 5:
                    print("Glucose, ")
                elif index == 6:
                    print("First aid supplies, ")
                elif index == 7:
                    print("Rain jacket, ")
                elif index == 8:
                    print("Personal Locator Beacon.")
            index +=1





# run
#  Create_Initial_Population test
# list1 =  Create_Initial_Population(5)
# list2 =  Create_Initial_Population(5)
# pop1 = list1[0]
# popFitness1 = list1[1]
# pop2 = list2[0]
# popFitness2 = list2[1]

# print(pop1)
# print(popFitness1)

# print(pop2)
# print(popFitness2)

# pop = replacement(pop1,pop2)
# print(pop)

# Crossover test 
# c1 = [0,1,0,1,0,1,0,0,0]
# c2 = [1,0,1,0,0,1,1,0,1]
# chs = Crossover(c1,c2)
# print(chs[0])
# print(chs[1])

# Mutation
# m = Mutation(c1)
# print(c1)

# Selection
# parents = selectingParents(pop,popFitness)
# print(parents)



#run
result = Create_Initial_Population(50)
evolution(result[0],result[1],20000)


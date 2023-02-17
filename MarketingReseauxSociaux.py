#Satyam Chowdhury 20214226
#Carlos Eduardo

#Using a greedy algorithm that takes a list of influencers and population that they touch and outputs a list of influencers which combined reach every single person in the population.

import time

class Influencer:

    affects = []

    def __init__(self, n:int):
        self.n = n

    def __str__(self):
        # return f'influencer {self.n}: affects {self.affects}'
        return str(self.n)


def main():
    #starts timer

    start = time.time()

    ### read file and save relevant information ###
    with open('data_devoir1\instance_p1000_i100.txt') as file: #TODO: path as argument
        lines = file.readlines()
    
    i = 0
    influencerList = []
    
    for line in lines:
        if i > 0:
            influencer = Influencer(i)

            #list of every person affected by influencer
            affects = line.split(" p")
            #remove first entry
            affects.pop(0)
            #convert every entry into int to remove '/n'
            affects = [ int(x) for x in affects ]
            
            influencer.affects = affects
            influencerList.append(influencer)

        else: #line 0
            line = line.split(' ')
            influencers = int(line[0])
            populationCount = int(line[1])
            population = [*range(1, populationCount+1)]

        i+=1

    # print(f'{influencers}, {population}')
    
    # for influencer in influencerList:
    #     print(influencer)

    ### file reading complete ###

    #sort by how many people each influencer affects
    influencerList.sort(key= lambda influencer: len(influencer.affects))

    #list of chosen influencers
    chosen = []
    
    

    while len(population)>0:
        #last chosen influencer
        prev = influencerList.pop()
        chosen.append("i" + str(prev.n))
        

        for person in prev.affects:
            if person in population:
                population.remove(person)
    
    print(chosen)
    print(len(chosen))
    print(population)

    #end timer
    end = time.time()

    print(end - start)


if __name__ == "__main__":
    main()

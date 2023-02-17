

class Influencer:

    affects = []

    def __init__(self, n:int):
        self.n = n

    def __str__(self):
        return f'influencer {self.n}: affects {self.affects}'


def main():
    #read lines from file
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

        else:
            line = line.split(' ')
            influencers = int(line[0])
            population = int(line[1])

        i+=1

    print(f'{influencers}, {population}')
    
    for influencer in influencerList:
        print(influencer)

if __name__ == "__main__":
    main()

from SnakeGame import *
from agent import agent
from curses import wrapper as wrap
import random
import tqdm

def agents_maker(num):
    return [agent(i) for i in range(num)]

def agents_sort(agents_list):
    sorted_list= sorted(agents_list,key=lambda x: x.scores)
    for i in range(len(sorted_list)):
        sorted_list[i].index=i
    return sorted_list

def  next_gen(agents):
    index_range=round(len(agents)*0.95)-1
    for player in agents[:index_range]:
        player.update(random.choice(agents[index_range:]).evolve())
        player.scores=0
    for player in agents[index_range:]:
        player.scores=0
def play_gen(agents_list,num_of_games,gen_num):
    for _agent in agents_list:
        for i in range(num_of_games):
            game(_agent,gen_num)
           # print(str(_agent.scores)+"\n")
    print(sum([a.scores for a in agents_list])/len(agents_list))

def wrapper(num_of_agents,num_of_genarations,num_of_games_each):
   # print("first one")
    agents=agents_maker(num_of_agents)
    for i in range(num_of_genarations):
        print("starting gen {} \n".format(i))
        play_gen(agents,num_of_games_each,i+1)
        agents=agents_sort(agents)
        print("best score in gen is:{}\n ".format(agents[-1].scores))
        next_gen(agents)
    agents[-1].nn.save("best_model")

if __name__=="__main__":
    agents_num=int(input())
    gen=int(input())
    games=int(input())
    wrapper(agents_num,gen,games)            
    a=input("the end")

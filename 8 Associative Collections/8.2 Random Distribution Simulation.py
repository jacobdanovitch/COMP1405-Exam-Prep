#Random Distribution Simulation

from random import randint

def sim():
    sim_dict = {}
    for _ in range(1000):
        randkey = randint(0,100)
        if randkey in sim_dict:
            sim_dict[randkey] += 1
        else:
            sim_dict[randkey] = 1
    print(sim_dict)

sim()
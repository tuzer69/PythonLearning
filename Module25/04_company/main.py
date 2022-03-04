from personal import Manager
from personal import Agent
from personal import Worker
import random


print('-' * 10, 'Manager', '-' * 10)
for _ in range(3):
    print(Manager().get_salary())

print('-' * 10, 'Agent', '-' * 10)
for _ in range(3):
    r = random.randint(4000, 10000)
    print(Agent(r).get_salary())

print('-' * 10, 'Worker', '-' * 10)
for _ in range(3):
    r = random.randint(90, 300)
    print(Worker(r).get_salary())
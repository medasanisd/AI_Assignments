# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:22:35 2019

@author: Sai Teja
"""

game_answer=[9]
guess_answer=[6]
if (game_answer>guess_answer):
    print('The answer is too low')
else: (print('The answer is too high'))


for  i in range(1,10):
  multiply=5*i
  if(multiply<=30):
      print(multiply)



limit = 100
num = 0 
while (num +1)**2 < limit:
    num += 1
nearest_square = (num)**2


print(nearest_square)


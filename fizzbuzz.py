# -*- coding: utf-8 -*-
"""FizzBuzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v-8Wj-y1iUXYHLQd-ylsjNpZ646ItnrL

FizzBuzz is a game that has gained in popularity as a programming assignment to weed out non-programmers during job interviews. The object of the assignment is less about solving it correctly according to the below rules and more about showing the programmer understands basic, necessary tools such as if-/else-statements and loops. The rules of FizzBuzz are as follows:

For numbers 1 through 100,

if the number is divisible by 3 print Fizz;
if the number is divisible by 5 print Buzz;
if the number is divisible by 3 and 5 (15) print FizzBuzz;
else, print the number.
"""

for i in range(1,100):
  if i % 3 == 0:
    if i % 5 == 0:
      print('FizzBuzz')
    else:
      print('Fizz')
  else:
    if i % 5 == 0:
      print('Buzz')
    else:
      print(i)
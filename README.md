# fizzbuzz

The classic game fizzbuzz that now apparently is asked in many job interviews, and because soon I will have to go to one, rather go prepared.

Implemented using Keras, which is a great deep learning library. On a night that I should be worried about my thesis.

FizzBuzz game goes about if divisible by 3, then it should say fizz, if by 5, buzz, and if by both fizzbuzz.

1. run **fizzbuzz.py <nb_numbers>** to generate. This generates the normal solutions of the problem, and generates a file called 'fizzbuzz.txt' with the results of it. This file is later used in 'ml_fb.py' to train the NN.

2. run **ml_fb.py <nb_epochs>** to train. Generates a file called 'results.txt' with the Neural Net results after the training is completed. 

3300 epochs trains with 100% accuracy all the numbers up to 100.
2900 epochs trains with 100% accuracy all the numbers up to 50.

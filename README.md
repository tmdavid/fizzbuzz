# fizzbuzz

The classic game fizzbuzz that now apparently is asked in many job interviews, and because soon I will have to go to one, rather go prepared.

Implemented using Keras, which is a great deep learning library. On a night that I should be worried about my thesis.

FizzBuzz game goes about if divisible by 3, then it should say fizz, if by 5, buzz, and if by both fizzbuzz.

1. run **fizzbuzz.py nb_numbers** to generate. This generates the normal solutions of the problem, and generates a file called 'fizzbuzz.txt' with the results of it. This file is later used in 'ml_fb.py' to train the NN.

2. run **ml_fb.py nb_epochs  nb_layers** to train. Generates a file called 'results.txt' with the Neural Net results after the training is completed. nb_layers is the number of layers to stack as hidden in the network. Apparently the more layers, the faster it trains, but at the cost of not getting to 100% accuracy, but close to it, 96-98%. 

* 3300 epochs trains with 100% accuracy all the numbers up to 100.

* 2900 epochs trains with 100% accuracy all the numbers up to 50.

Be **careful if you want to train more than 100 or 150 numbers. If you go for numbers like 1000 or so, its gonna get shitty slow, and you may need to train for more than 5000 epochs. Use at own risk** 

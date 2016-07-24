import sys

f = open("fizzbuzz.txt", 'w')

if len(sys.argv)<2:
    raise ValueError('Not specified number numbers')
else:
    nb_numbers = int(sys.argv[1])

for i in range(1, nb_numbers+1):
    fizz = ""
    buzz = ""
    num = ""
    if i%3==0:
        fizz =  'fizz'
    if i%5==0:
        buzz = 'buzz'
    if fizz is "" and buzz is "":
        num = i
    to_file = str(i) + " " + str(num) + fizz + buzz + "\n"
    f.write(to_file)

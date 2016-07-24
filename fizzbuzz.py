f = open("fizzbuzz.txt", 'w')

for i in range(1, 100):
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

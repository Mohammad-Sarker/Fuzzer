import subprocess as sb
from subprocess import Popen, PIPE
import os
import random
from datetime import datetime
import string

# Generate a random string

operationList = ['+','-','*','/']

try:
    while True:
        x = ''.join(random.choice(operationList))
        random.seed(datetime.now())
        y = random.random()
        random.seed(datetime.now())
        z = random.random()

        random_input = str(x) + " " + str(y) + " " + str(z)
        #print(random_input)

        data, temp = os.pipe()

        # os.write(temp,bytes("+ 20 10\n", "utf-8"))
        os.write(temp,bytes(random_input, "utf-8"))
        os.close(temp)

        for i in range(1000):
            with open('output{}.txt'.format(i), 'w') as f:
                s = sb.run("g++ calculator.cpp -o out2;./out2;./out2", stdin = data, stdout=f, shell = True)

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

        #s = sb.check_output("g++ calculator.cpp -o out2;./out2", stdin = data, shell = True)

        #print(s.decode("utf-8"))

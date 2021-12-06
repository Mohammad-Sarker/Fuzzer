import os
from subprocess import CalledProcessError, Popen, PIPE
import sys
from random import randint


cmd = "program.exe"
loopTimes = int(sys.argv[1])


def main():
   with open('fuzzer.txt', 'w') as fw:

      for i in range(loopTimes):
         print(f'\n\nRunning the executable {i}')
         op = ['+', '-', '*', '/'][randint(0, 3)]
         num1 = randint(-1000, 1000)
         num2 = randint(-1000, 1000)
         print(f'The operator is {op}')
         print(f'The 1st operand is {num1}')
         print(f'The 2nd operand is {num2}')
      
         input_data = os.linesep.join([op, str(num1), str(num2)])
      
         p = Popen(cmd, stdin=PIPE, bufsize=0)
         p.communicate(input_data.encode('ascii'))
         if p.returncode != 0:
            fw.write(f'Operator : {op}, Operand1 : {num1}, Operand2 : {num2}, ReturnedCode : {p.returncode}')


if __name__ == "__main__":
   main()

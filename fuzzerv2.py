# Python fuzzer for Linux bc command line calculator
import os
from subprocess import CalledProcessError, Popen, PIPE
import sys
from random import randint
import string
import random
import subprocess

cmd = "bc"
loopTimes = int(sys.argv[1])


def main():
   with open('output.txt', 'w') as fw:

      for i in range(loopTimes):
         print(f'\n\nRunning the executable {i}')
         length = 21
         letters_digits = string.ascii_letters + string.digits
         input_data = ''.join(random.choice(letters_digits) for i in range(length))
         #print(input_data)
         p = subprocess.run([cmd, 'output.txt'], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
         fw.write(f'Input Data : {input_data}, ReturnedCode : {p.returncode}')


if __name__ == "__main__":
   main()

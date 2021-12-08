import os # module for interacting with the operating system's functionality
from subprocess import CalledProcessError, Popen, PIPE # module to work with passive processes and pipe errors for their return codes
import sys # module to directly interact with runtime environment 
from random import randint # module for generating random integers


cmd = "program.exe" # stores the calculator executable 
loopTimes = int(sys.argv[1]) # command line argument for number of loops through the executable 


def main():
   with open('fuzzer.txt', 'w') as fw: # An output text file with all the errors occuring when executing the script on the calculator

      for i in range(loopTimes): # loops as many times as the user inputted
         print(f'\n\nRunning the executable {i}') # standby output to the user
         op = ['+', '-', '*', '/'][randint(0, 3)] 
         num1 = randint(-1000, 1000) # gives us a random integer from -1000 to 1000
         num2 = randint(-1000, 1000) # gives us a random integer from -1000 to 1000
         
         if (op != '/' and num2 != 0):
            if randint(0, 3) == 0: # If random integer == 0
                num1 = chr(randint(65, 91)) # change num to random character A - Z

            if randint(0, 3) == 0: # If random integer == 0
                num2 = chr(randint(65, 91)) # change num to random character A - Z

         print(f'The operator is {op}')
         print(f'The 1st operand is {num1}')
         print(f'The 2nd operand is {num2}')
      
         input_data = os.linesep.join([op, str(num1), str(num2)]) # iterates through the lines of the text file and joins into a string
      
         p = Popen(cmd, stdin=PIPE, bufsize=0) # creates a pipe to the standard input device from the command line
         p.communicate(input_data.encode('ascii')) # reads and encodes data in strings until end of runtime
         if p.returncode != 0: # If the exit status is anything other than the safe 0, meaning an error, write it and the line to an output text file
            fw.write(f'Operator : {op}, Operand1 : {num1}, Operand2 : {num2}, ReturnedCode : {p.returncode}\n')


if __name__ == "__main__":
   main()

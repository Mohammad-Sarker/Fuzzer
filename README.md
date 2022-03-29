# Fuzzer

A python script that takes the final binary exucatable of our calculator.cpp and fuzzes it. fuzzer.py does the former, and fuzzerv2.py attempts the same idea on the Linux bc command line calculator. The fuzzer generates random inputs, and feeds it to our calculator.exe in a loop until there are error codes (crashing/segfault), which are saved in a text file. 

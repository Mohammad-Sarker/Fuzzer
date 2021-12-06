# Mutational-Fuzzer

A python script that takes the final binary exucatable of our calculator.cpp and fuzzes it. Our fuzzer is mutational aka generates random inputs, and feeds it to our calculator.exe in a loop until there's an error (crashing/segfault). Lastly, the error code is saved in a text file.

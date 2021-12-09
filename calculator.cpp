// Sample C++ program to test the fuzzing script

#include <iostream>
#include <stdexcept>

using namespace std;

float simpleCalculator(char operatorsign, float operand1, float operand2) {
    float result;
    if (operatorsign == '+'){
      result = operand1 + operand2;
      return result;
    }
    else if (operatorsign == '-'){
      result = operand1 - operand2;
      return result;
    }
    
    else if(operatorsign == '*') {
        result = operand1 * operand2;
        return result;
    }
    
    else if(operatorsign == '/') {
        if (operand2 == 0) {
            throw runtime_error("Math error: Attempted to divide by Zero\n");
        }        
        result = operand1 / operand2;
        return result;
    }

}

int main() {
    char op;
    string num1, num2;
    float resultnum;
    cout << "Enter an operation sign: ";
    cin >> op;
    cout << "Enter one operand: ";
    cin >> num1;
    cout << "Enter another operand: ";
    cin >> num2;
    resultnum = simpleCalculator(op, stof(num1), stof(num2));
    cout << resultnum;
}

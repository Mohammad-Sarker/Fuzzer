//Sample C++ program to test the fuzzing script

#include <iostream>

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
        if(operand2 == 0) {
            cout << "Error, cannot divide by 0";
           }
        else {
        result = operand1 / operand2;
        return result;
        }
    }

}

int main() {
    char op;
    float num1, num2, resultnum;
    cout << "Enter an operation sign: ";
    cin >> op;
    cout << "Enter one operand: ";
    cin >> num1;
    cout << "Enter another operand: ";
    cin >> num2;
    resultnum = simpleCalculator(op, num1, num2);
    cout << resultnum;
    
}

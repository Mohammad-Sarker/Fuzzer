//Sample C++ program to test the fuzzing script

# include <iostream>
using namespace std;

int main() {
    char operatorsign;
    float operand1, operand2, result;

    cout << "Enter one operation here: +, -, *, /: ";
    cin >> operatorsign;

    cout << "Enter two operands here: ";
    cin >> operand1 >> operand2;

    if (operatorsign == '+'){
      result = operand1 + operand2;
      cout<< result;
    }
    else if (operatorsign == '-'){
      result = operand1 - operand2;
      cout<< result;
    }

}

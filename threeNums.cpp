// threeNums.cpp : Defines the entry point for the console application.
//

#include <string>
#include <iostream>
using namespace std;
int main()
{
	int cont;
	double num1;
	double num2;
	double num3;
	double smallest;
	double largest;
	cout << "enter three diffrent numbers. (press enter after each one ) " << endl;
	cin >> num1;
	cin >> num2;
	cin >> num3;
	double sum = num1 + num2 + num3;
	double average = (num1 + num2 + num3) / 3;
	double product = num1 * num2 * num3;
	if (num1 < num2 && num1 < num3) {
		smallest = num1;
	}
	else if (num2 < num3 && num2 < num1) {
		smallest = num2;
	}
	else if (num3 < num2 && num3 < num1) {
		smallest = num3;
	}

	if (num1 > num2 && num1 > num3) {
		largest = num1;
	}
	else if (num2 > num3 && num2 > num1) {
		largest = num2;
	}
	else if (num3 > num2 && num3 > num1) {
		largest = num3;
	}
	cout << "Sum: " << sum << endl;
	cout << "Average: " << average << endl;
	cout << "Product: " << product << endl;
	cout << "Smallest: " << smallest << endl;
	cout << "Largest: "<< largest << endl;
	cin >> cont;
	return 0;
}

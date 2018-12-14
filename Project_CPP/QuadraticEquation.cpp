#include<iostream>
#include<stdlib.h>
#include<cmath> 
#include <string> 
#include <sstream> 

using namespace std;

void findRoots(int a, int b, int c) 
{ 
	// If a is 0, then equation is not quadratic, but 
	// linear 
	if (a == 0) 
	{ 
		cout << "Invalid"; 
		return; 
	} 

	int d = b*b - 4*a*c; 
	double sqrt_val = sqrt(abs(d)); 
	double root1, root2;

	if (d > 0) 
	{ 
		cout << "This program is used to calculate the roots of the quadratic equation: Ax ^ 2 + bx + c = 0" << endl; 
		cout << "The root X1 = " << (double)(-b + sqrt_val)/(2*a) << endl
			<< "The root X2 = " << (double)(-b - sqrt_val)/(2*a) << endl; 
	} 
	else if (d == 0) 
	{ 
		cout << "This program is used to calculate the roots of the quadratic equation: ax2 bx CE" << endl;
        cout << "The Discriminant, B2-4ac, is E, then there is only one root" << endl; 
		cout << "The root x1 = " << -(double)b / (2*a); 
	} 
	else // d < 0 
	{ 
		cout << "This program is used to calculate the roots of the quadratic equation: axA2 bxc0" << endl;
        cout << "The discriminant, b ^2 – 4AC, is inferior to 0, then the roots are imaginary" << endl; 
		cout << "The root x1 = " << -(double)b / (2*a) << " + i" << sqrt_val 
			<< endl << "The root x2 = " << -(double)b / (2*a) << " - i"
			<< sqrt_val << endl; 
	} 
} 

// Driver code 
int main() 
{ 
	int a, b, c;
    cout << "Enter the value of ' a ': ";
    cin >> a;

    cout << endl;
    cout << "Enter the value of ' b ': ";
    cin >> b;
    cout << endl;
    cout << "Enter the value of ' c ': ";
    cin >> c;
    cout << endl;
 
	findRoots(a, b, c); 
	
	getchar();
	return 0; 
} 

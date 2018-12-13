#include<iostream>
#include<stdlib.h>
#include<cmath> 

using namespace std;

double getDistance(double x1, double y1, double x2, double y2)
{
     // Calculating distance 
    return sqrt(pow(x2 - x1, 2) +  
                pow(y2 - y1, 2) * 1.0);  
}


int main()
{
    int x1, y1, x2, y2;
    double distance;
    cout << "This program calculates the distance between two points" << endl;
    
    cout << "Enter the coordinates of the first point" << endl;
    cout << "X: ";
    cin >> x1;
    cout << "Y: ";
    cin >> y1;
    
    cout << endl;
    
    cout << "Enter the coordinates of the second point" << endl;
    cout << "X: ";
    cin >> x2;
    cout << "Y: ";
    cin >> y2;
    
    cout << endl;
    
    distance = getDistance(x1, y1, x2, y2);
    
    cout << "The distance between these two points is: " << distance;

    return 0; 
}

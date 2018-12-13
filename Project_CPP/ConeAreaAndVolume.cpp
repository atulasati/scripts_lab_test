#include<iostream>
#include<stdlib.h>
#include<cmath> 

using namespace std;

double getConeSurfaceArea(double radius, double height)
{
    double surfaceArea = -1;
    if(radius !=0 && height !=0)
    {
        surfaceArea = 3.14 * radius * (radius + sqrt(radius * radius + height * height));
    }
    
    return surfaceArea;
}

double getConeVolume(double radius, double height)
{
    double volume = -1;
    if(radius !=0 && height !=0)
    {
        volume = (1.0/3) * 3.14 * radius * radius * height;       
    }
    
    return volume;
}


int main()
{
    double radius, height, surfaceArea, volume;
    cout << "This program calculates the area and volume of a cone" << endl;
    cout << "Enter the radius of the cone: ";
    cin >> radius;
    cout << endl;
    
    cout << "Enter the height of the cone: ";
    cin >> height;
    cout << endl;
    
    surfaceArea = getConeSurfaceArea(radius, height);
    volume = getConeVolume(radius, height);
    
    cout << "The total area of the cone is: " << surfaceArea << endl;
    cout << "The volume of the cone is: " << volume << endl;
    
    return 0;
}

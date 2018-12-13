#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

void matchGuessNoWithRandomNumber()
{
     int guessedNumber, generatedNumber, noOfTries;
     cout << "I chose a number between 1 and 100" << endl;
     cout << "Can you guess that number: " << endl;
     generatedNumber = rand()%100 + 1;
     noOfTries = 0;
     
     do
     {
          noOfTries++;
          cin >> guessedNumber;
          cout << endl;
          
          if (guessedNumber < generatedNumber)
          {
              cout << "Too low, the number I have chosen is greater than " << guessedNumber << endl;
          }
          else if(guessedNumber > generatedNumber)
          {
              cout << "Too high, the number I chose is smaller than " << guessedNumber << endl;
          }
          cout << "To try a NEW: "; 
     }while(guessedNumber != generatedNumber);
     
     cout << "==================================" << endl;
     cout << "Bravo! You have Guess The number after " << noOfTries << " tries" << endl;
}
 

int main()
{
    // This program will create different sequence of  
    // random numbers on every program run  
  
    // Use current time as seed for random generator 
    srand(time(0));
    
    cout << "Game-Guess my number Version 1.0" << endl;
    cout << "==================================" << endl;
    
    matchGuessNoWithRandomNumber();
    getchar();
    
    return 0;
}

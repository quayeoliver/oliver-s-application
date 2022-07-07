#include <iostream>

using namespace std;

int main()
{
    cout << "Enter your first name" << endl;
    string firstName;
    string surname;
    cin>>firstName;
    cout<<"Enter your surname"<< endl;
    cin>>surname;
    cout<<"welcome" + firstName + surname << endl;


    return 0;
}

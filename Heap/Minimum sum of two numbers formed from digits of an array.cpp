#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

// Function to find the minimum possible sum
string minimumSum(vector<int>& arr) {
    // Sort the array in ascending order
    sort(arr.begin(), arr.end());

    string num1 = "", num2 = "";

    // Distribute digits between num1 and num2 alternately
    for (int i = 0; i < arr.size(); i++) {
        if (i % 2 == 0) {
            num1 += to_string(arr[i]);
        } else {
            num2 += to_string(arr[i]);
        }
    }

    // Convert the two numbers into integers and return the sum as a string
    int sum = stoi(num1) + stoi(num2);
    
    return to_string(sum);
}

int main() {
    vector<int> arr = {6, 8, 4, 5, 2, 3};
    
    // Call the function and output the result
    cout << "Minimum sum: " << minimumSum(arr) << endl;

    return 0;
}

// some func reference
/*
 // Integer to string using to_string
    int num = 12345;
    string strNum = to_string(num);
    cout << "Integer to string: " << strNum << endl;

    // Float to string using to_string
    float floatNum = 123.45f;
    string strFloat = to_string(floatNum);
    cout << "Float to string: " << strFloat << endl;

    // Convert string to integer using stoi
    string strInt = "6789";
    int numFromStr = stoi(strInt);
    cout << "String to integer: " << numFromStr << endl;

    // Convert string to float using stof
    string strFloat2 = "456.78";
    float numFromStrFloat = stof(strFloat2);
    cout << "String to float: " << numFromStrFloat << endl;
*/
#include <iostream>
#include <string>

using namespace std;

// Function to return the integer value of a Roman numeral character
int val(char str) {
    switch (str) {
        case 'I': return 1;    // Value for 'I' is 1
        case 'V': return 5;    // Value for 'V' is 5
        case 'X': return 10;   // Value for 'X' is 10
        case 'L': return 50;   // Value for 'L' is 50
        case 'C': return 100;  // Value for 'C' is 100
        case 'D': return 500;  // Value for 'D' is 500
        case 'M': return 1000; // Value for 'M' is 1000
        default: return 0;     // Return 0 for invalid characters
    }
}

// Function to convert a Roman numeral string to its decimal equivalent
int romanToDecimal(string &str) {
    int sum = val(str[0]); // Initialize sum with the value of the first character

    // Iterate through the Roman numeral string starting from the second character
    for (int i = 1; i < str.length(); i++) {
        // If the current character's value is less than or equal to the previous character's value
        if (val(str[i]) <= val(str[i - 1])) {
            sum += val(str[i]); // Add the current value to the sum
        } else {
            // If the current character's value is greater than the previous character's value,
            // it indicates a subtraction scenario (e.g., IV = 4, IX = 9)
            sum += val(str[i]) - (2 * val(str[i - 1])); // Adjust the sum for the subtraction
        }
    }
    
    return sum; // Return the final computed decimal value
}

int main() {
    string romanNumeral = "MCMXCIV"; // Example Roman numeral
    cout << "The decimal value of " << romanNumeral << " is " << romanToDecimal(romanNumeral) << endl;
    
    return 0;
}

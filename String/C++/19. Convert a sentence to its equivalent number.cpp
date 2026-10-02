#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

// Function to initialize the mapping of each character to its corresponding numeric keypad sequence
unordered_map<char, string> initializeKeypadMapping() {
    unordered_map<char, string> keypad;
    keypad['A'] = "2";       keypad['B'] = "22";      keypad['C'] = "222";
    keypad['D'] = "3";       keypad['E'] = "33";      keypad['F'] = "333";
    keypad['G'] = "4";       keypad['H'] = "44";      keypad['I'] = "444";
    keypad['J'] = "5";       keypad['K'] = "55";      keypad['L'] = "555";
    keypad['M'] = "6";       keypad['N'] = "66";      keypad['O'] = "666";
    keypad['P'] = "7";       keypad['Q'] = "77";      keypad['R'] = "777";      keypad['S'] = "7777";
    keypad['T'] = "8";       keypad['U'] = "88";      keypad['V'] = "888";
    keypad['W'] = "9";       keypad['X'] = "99";      keypad['Y'] = "999";      keypad['Z'] = "9999";
    keypad[' '] = "0";  // Space maps to 0
    return keypad;
}

// Function to convert a sentence to its equivalent mobile numeric keypad sequence
string convertToKeypadSequence(const string& sentence) {
    unordered_map<char, string> keypad = initializeKeypadMapping();
    string result;

    // Traverse each character in the sentence
    for (char c : sentence) {
        // Convert character to uppercase if it's lowercase
        char upperChar = toupper(c);
        
        // Append the keypad sequence corresponding to the character
        result += keypad[upperChar];
    }

    return result;
}

int main() {
    string input = "HELLO WORLD";
    cout << "Input: " << input << endl;
    cout << "Output: " << convertToKeypadSequence(input) << endl;
    
    input = "GEEKSFORGEEKS";
    cout << "\nInput: " << input << endl;
    cout << "Output: " << convertToKeypadSequence(input) << endl;

    return 0;
}

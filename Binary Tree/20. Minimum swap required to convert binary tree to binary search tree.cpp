 .#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to perform in-order traversal of the binary tree
void inOrderTraversal(const vector<int>& tree, vector<int>& inOrder, int index) {
    if (index >= tree.size()) return;

    // Left child
    inOrderTraversal(tree, inOrder, 2 * index + 1);

    // Node itself
    inOrder.push_back(tree[index]);

    // Right child
    inOrderTraversal(tree, inOrder, 2 * index + 2);
}

// Function to calculate minimum swaps to sort an array
int minSwaps(vector<int>& nums) {
    int N = nums.size();
    vector<pair<int, int>> v(N);

    for (int i = 0; i < N; i++)
        v[i] = {nums[i], i};

    sort(v.begin(), v.end());

    int c = 0;

    for (int i = 0; i < N;) {
        if (v[i].second == i) {
            i++;
        } else {
            c++;
            swap(v[i], v[v[i].second]);
        }
    }

    return c;
}

// Function to find the minimum swaps to convert binary tree to BST
int minSwapsToConvertToBST(vector<int>& tree) {
    vector<int> inOrder;
    inOrderTraversal(tree, inOrder, 0);
    return minSwaps(inOrder);
}

int main() {
    vector<int> tree = {5, 3, 8, 2, 4, 6, 9}; // Example binary tree
    cout << "Minimum swaps required to convert binary tree to BST: " << minSwapsToConvertToBST(tree) << endl;
    return 0;
}

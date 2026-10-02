#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to check adjacent cells and rot the fresh oranges
void issafe(vector<vector<int>>& grid, queue<pair<int,int>> &q, pair<int,int> &p){
    int n = grid.size();  // Number of rows in the grid
    int m = grid[0].size();  // Number of columns in the grid
    int x = p.first;  // Current row index
    int y = p.second;  // Current column index
    
    // Directions for adjacent cells: up, down, left, right
    vector<pair<int,int>> v = { {-1,0}, {1,0}, {0,-1}, {0,1} };

    // Check each direction
    for(auto temp : v){
        // Calculate the new position
        int newX = x + temp.first;
        int newY = y + temp.second;
        
        // Check if the new position is within the grid boundaries
        if( (newX >= 0 && newX < n) && (newY >= 0 && newY < m) ){
            // If the adjacent cell is empty (0) or already rotten (2), continue to the next direction
            if(grid[newX][newY] == 0 || grid[newX][newY] == 2) continue;
            else {
                // Push the position of the fresh orange (1) into the queue
                q.push({newX, newY});
                // Mark this orange as rotten (2)
                grid[newX][newY] = 2;
            }
        }
    }
}

// Main function to determine the time required for all oranges to rot
int orangesRotting(vector<vector<int>>& grid) {
    int timer = 0;  // Timer to count the minutes taken for all oranges to rot
    int count = 0;  // Count of rotten oranges at the current level
    queue<pair<int,int>> q;  // Queue to hold positions of rotten oranges
    
    // Initialize the queue with positions of all rotten oranges
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[i].size(); j++){
            if(grid[i][j] == 2){  // If the orange is rotten
                q.push({i, j});  // Push its position into the queue
            }
        }
    }
    
    count = q.size();  // Count of rotten oranges in the queue

    // Process the queue until it is empty
    while(!q.empty()){
        // Process all oranges at the current level (current time step)
        for(int i = 0; i < count; i++){
            pair<int,int> p = q.front();  // Get the position of the current rotten orange
            q.pop();  // Remove the processed orange from the queue
            issafe(grid, q, p);  // Check and rot adjacent fresh oranges
        }

        // If there are any newly rotten oranges in the queue
        if(q.size() > 0){
            count = q.size();  // Update the count to the number of newly rotten oranges
            timer++;  // Increment the timer as one minute has passed
        }
    }
    
    // After processing, check if there are any fresh oranges left
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[i].size(); j++){
            if(grid[i][j] == 1) return -1;  // If there is a fresh orange left, return -1
        }
    }
    
    // Return the total time taken for all oranges to rot
    return timer;
}

// Example usage
int main() {
    vector<vector<int>> grid = { {2,1,1}, {1,1,0}, {0,1,1} };  // Example grid
    int result = orangesRotting(grid);  // Call the function
    cout << "Time taken for all oranges to rot: " << result << " minutes." << endl;  // Output the result
    return 0;
}

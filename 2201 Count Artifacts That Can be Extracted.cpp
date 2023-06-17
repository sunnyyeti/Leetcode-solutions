// There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:

// (r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
// (r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
// You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

// Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.

// The test cases are generated such that:

// No two artifacts overlap.
// Each artifact only covers at most 4 cells.
// The entries of dig are unique.
 

// Example 1:


// Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
// Output: 1
// Explanation: 
// The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
// There is 1 artifact that can be extracted, namely the red artifact.
// The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
// Thus, we return 1.
// Example 2:


// Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
// Output: 2
// Explanation: Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2. 
 

// Constraints:

// 1 <= n <= 1000
// 1 <= artifacts.length, dig.length <= min(n2, 105)
// artifacts[i].length == 4
// dig[i].length == 2
// 0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1
// r1i <= r2i
// c1i <= c2i
// No two artifacts will overlap.
// The number of cells covered by an artifact is at most 4.
// The entries of dig are unique.
class Solution {
public:
    int get_key(int row, int col, int n){
        return row*n+col;
    }
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
        unordered_map<int,int> pos2artifacts;
        unordered_map<int,int> size;
        for (vector<int> & vec: artifacts){
            int r1 = vec[0];
            int c1 = vec[1];
            int r2   = vec[2];
            int c2 = vec[3];
            int grids = (r2-r1+1)*(c2-c1+1);
            for (int r=r1;r<=r2;r++){
                for (int c=c1;c<=c2;c++){
                    pos2artifacts[get_key(r,c,n)] = size.size();
                }
            }
            size[size.size()] = grids;
        }
        int ans = 0;
        for (auto& d: dig){
            int r = d[0];
            int c=d[1];
            int key = get_key(r,c,n);
            if (pos2artifacts.find(key)!=pos2artifacts.end()){
                int index = pos2artifacts[key];
                size[index]-=1;
                if (size[index]==0){
                    ans++;
                }
            }
        }
        return ans;
    }
};
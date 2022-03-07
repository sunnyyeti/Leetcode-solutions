// class Solution {
public:
    int minMoves(int target, int maxDoubles) {
        int ans = 0;
        while (target>1){
            if (target&1 && maxDoubles){
                target--;
            }else if(target&1 && !maxDoubles){
                ans += target-1;
                break;
            }else if (maxDoubles){
                target>>=1;
                maxDoubles--;
            }else{
                ans += target-1;
                break;
            }
            ans++;
        }
        return ans;
    }
};
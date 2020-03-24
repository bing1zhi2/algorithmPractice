#include<iostream>
#include<vector>
using namespace std;
class Solution
{
public:
    int massage(vector<int> &nums)
    {
        int n = nums.size();
        if(n<=0){
            return 0;
        }

        int nochose = 0;
        int chose = nums[0];
        for (int i = 1; i < n;i++){
            int t_nochose = max(nochose, chose);
            int t_chose = nochose + nums[i];

            nochose = t_nochose;
            chose = t_chose;
        }
        return max(nochose, chose);
    }
};
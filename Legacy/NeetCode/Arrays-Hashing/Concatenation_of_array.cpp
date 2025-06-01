// Date: 28 April 2025
// Link: https://leetcode.com/problems/concatenation-of-array/
// Name: 1929. Concatenation of Array

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> getConcatenation(const vector<int> &nums)
    {
        vector<int> result = nums;
        result.insert(result.end(), nums.begin(), nums.end());
        return result;
    }
};

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums)
        cin >> x;

    Solution obj;
    vector<int> ans = obj.getConcatenation(nums);
    for (int x : ans)
        cout << x << " ";

    return 0;
}
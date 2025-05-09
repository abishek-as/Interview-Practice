#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int largest(vector<int> &nums)
    {
        int largest = nums[0];
        for (size_t i = 1; i < nums.size(); i++)
            if (nums[i] > largest)
                largest = nums[i];
        return largest;
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
    cout << obj.largest(nums);
    return 0;
}
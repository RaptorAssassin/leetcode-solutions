class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> original = nums;

        for (int i = 0, l = nums.size(); i < l; i++) {
            int new_index = (i + k) % l;
            nums[new_index] = original[i];
        }
    }
};

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> lastSeen(256, -1);
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); ++right) {
            if (lastSeen[s[right]] >= left) {
                left = lastSeen[s[right]] + 1;
            }
            lastSeen[s[right]] = right;
            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
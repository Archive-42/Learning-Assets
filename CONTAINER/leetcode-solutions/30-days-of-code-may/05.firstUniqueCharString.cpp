class Solution {
public:
    int firstUniqChar(string s) {
        
        if(s.size() == 0) return -1;
        
        map<char, int> mp;
        for(auto ch : s)
            mp[ch]++;
        
        for(int i=0; i<s.size(); i++){
                if(mp[s[i]] == 1){
                    return i;
                }
        }
        return -1;
    }
};
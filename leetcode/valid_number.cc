class Solution {
public:
    bool isNumber(string s) {
        unsigned int i = 0;
        while (i < s.size()) {
            if (s[i] != ' ') break;
            ++i;
        }
        if (i < s.size() && (s[i] == '-' || s[i] == '+')) ++i;
        if (i == s.size()) return false;
        int end = s.size();
        while (end > 0 && s[end - 1] == ' ') --end;
        bool isfloat = false;
        bool isexpo = false;
        bool hasnum = false;
        while (i < end) {
            if ('0' <= s[i] && s[i] <= '9') {
                hasnum = true;
                ++i;
            } else if(s[i] == 'e' || s[i] == 'E') {
                if (isexpo || !hasnum) return false;
                if (i + 1 == end) return false;
                if (s[i + 1] == '-' || s[i + 1] == '+') ++i;
                isexpo = true;
                isfloat = false;
                hasnum = false;
                ++i;
            } else if (s[i] == '.') {
                if (isfloat || isexpo) return false;
                isfloat = true;
                ++i;
            } else {
                return false;
            }
        }
        return hasnum;
    }
};

class Solution {
public:
    int myAtoi(string str) {
        const char *p = str.c_str();
        while (*p == ' ') ++p;
        if (*p == 0) return 0;
        bool neg = false;
        if (*p == '-') neg = true, ++p;
        else if (*p == '+') ++p;
        long lad = 0;
        int digits = 0;
        while (*p == '0') ++p;
        while ('0' <= *p && *p <= '9' && ++digits < 12) {
            lad *= 10;
            lad += *p - '0';
            ++p;
        }
        if (neg && lad > 2147483648) return -2147483648;
        else if (!neg && lad > 2147483647) return 2147483647;
        if (neg) return (int)-lad;
        return (int)lad;
    }
};

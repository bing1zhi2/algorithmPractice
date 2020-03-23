#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        if( s.size()<2 )
        {
            return;
        }
        int left = -1;
        int right = s.size();
        cout << "reverseString " << right << endl;

        while (++left < --right)
        {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
        }
        return;
    }
};

int main()
{
    Solution s;
    vector<char> obj; // ["h","e","l","l","o"]
    obj.push_back('h');
    obj.push_back('e');
    obj.push_back('l');
    obj.push_back('l');
    obj.push_back('o');

    s.reverseString(obj);
    cout << "after reverse : " << endl;

    for (int i = 0; i < 5;i++){
        cout << obj[i] << endl;

    }

    return 0;
}
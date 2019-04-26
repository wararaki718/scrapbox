#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main()
{
    vector<int> v;
    for(int i=1;i<=5;i++) {
        v.push_back(i);
    }

    cout << accumulate(v.begin(), v.end(), 0) << endl;
    cout << accumulate(v.begin()+2, v.end(), 0) << endl;
    cout << accumulate(v.begin(), v.end()-2, 0) << endl;

    return 0;
}

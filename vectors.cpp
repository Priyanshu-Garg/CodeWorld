#include<bits/stdc++.h>
using namespace std;
void display(vector<int>&v)
{
  vector<int>::iterator i=v.begin();
    for(int i;i!=v.size();i++)
    {
        cout<<v[i]<<endl;
    }
}
int main()
{

        vector <int> vec1;
        vec1.push_back(69);
        vec1.push_back(9);
        vec1.push_back(609);
        vec1.push_back(690);
        vec1.pop_back();
        vector<int>::iterator iter =vec1.end();
        vec1.insert(iter-2,4);
        display(vec1);

}

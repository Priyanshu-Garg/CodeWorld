#include<bits/stdc++.h>
using namespace std;
void linear_searc(int key, vector<int>&v)
{

    for(int iter=0;iter!=v.size();iter++)
    {
        if(v[iter]==key)
        {
            cout<<iter;
        }
    }
}
int main()
{
    vector<int> vec1;int Size,key,elem;
    cout<<"Enter the size of your vector"<<endl;
    cin>>Size;
    cout<<"Enter the elements your vector"<<endl;
    for(int i=0;i<Size;i++)
    {
        cin>>elem;
        vec1.push_back(elem);
    }
    cout<<"Enter the key"<<endl;
    cin>>key;
    linear_searc(key,vec1);

}

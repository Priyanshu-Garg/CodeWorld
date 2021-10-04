#include<bits/stdc++.h>
using namespace std;
int main()
{
    cout << "Enter number of elements in array\n";
    int n;
    cin >> n;
    int arr[n];
    cout << "Enter the array elements\n";
    for (int i = 0; i < n;i++)
    {
        cin >> arr[i];
    }
        
    int x = sizeof(arr)/4;
    ;
    for (int gap = x / 2; gap >= 1; gap /= 2)
    {
        for (int j = gap; j < x;j++)
        {
            for (int i = j - gap; i >= 0;i-=gap)
            {
                if(arr[i+gap]>arr[i])
                {
                    break;
                }    
                else
                {
                    swap(arr[i + gap], arr[i]);
                }
            }
        }
    }

    for(auto e:arr)
    {
        cout << e << " ";
    }
        return 0;
}
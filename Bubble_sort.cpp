#include<bits/stdc++.h>
using namespace std;

void print(int arr[],int n){
	for(int i=0;i<n;i++){
		cout<<arr[i]<<' ';
	}
}

void Bubble(int arr[],int n)
{
	for(int i=0;i<n-1;i++)
	{
		bool swapped=false;
		for(int j=0;j<n-i-1;j++)
		{
			if(arr[j]>arr[j+1]) 
			{
				swap(arr[j],arr[j+1]);
				swapped=true;
			}
		}
		if(swapped==false) break;
	}
	print(arr,n);
}

int main(){
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	Bubble(arr,n);
	return 0;
}
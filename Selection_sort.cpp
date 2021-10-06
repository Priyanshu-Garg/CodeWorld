#include<bits/stdc++.h>
using namespace std;


void Selection(int arr[],int n)
{
	for(int i=0;i<n;i++)
	{
		int min=i;
		for(int j=i+1;j<n;j++)
		{
			if(arr[j]<arr[min]){
				min=j;
			}
		swap(arr[i],arr[min]);
		}
	}
//	print(arr,n);
	for(int i=0;i<n;i++){
		cout<<arr[i]<<' ';
	}
}

int main(){
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	Selection(arr,n);
	return 0;
}

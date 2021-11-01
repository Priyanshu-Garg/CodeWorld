#include <iostream>
using namespace std;
int main()
{ int high,low,n,ele,mid;
  int arr[20],i;
  cout<<"Enter the number of elements"<<endl;
  cin>>n;
  low =0;
  high = n-1;
  cout<<"Enter the elements"<<endl;
  for(i=0;i<n;i++)
  {cin>>arr[i];
  }
   printf("Enter the element you want to search in the series");
   cin>>ele;
   do
   { mid=(high+low)/2;
     if(ele>arr[mid])
       {
           low=mid+1;
       }
    else if(ele<arr[mid])
       {
           high=mid-1;
       }
     
   } while ((ele!=arr[mid])&&(low<=high));
   if (ele==arr[mid])
      { cout<<"The element "<<ele<<" is found in the series"<<endl;
      }
    else
      { cout<<"The element "<<ele<<" is not found in the series"<<endl;
      }

}

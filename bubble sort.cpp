#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n){
    for(int i = 0; i < n; i++){
        for (int j = 0; j < n-i-1; j++){
            if(arr[j]> arr[j+1] ){
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void printarray(int arr[], int n){
    for (int  i = 0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){
    int arr[] = {3,5,7,6,47,5,4,2,45,6,7,87,6,54,76};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "Before sorting: " << endl;

    printarray(arr, n);
    bubbleSort(arr, n); 
    cout << "After sorting: " << endl;
    }
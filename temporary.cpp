#include <iostream>
#include <climits>
using namespace std ;





int main(){
 

  int num[] = {9,6,-9,7,-87,-45,23,-76,65,98,123};
  int a = sizeof(num);
  int smallest = INT_MAX;
  int largest = INT_MIN;
    for(int i = 0; i < a; i++){

        // if(num[i] < smallest){
        //   smallest = num[i];
        smallest = min( num[i],smallest);
        // largest = max(num[i],largest);
        }
        cout << "The smallest number is: " << smallest << endl;
        // cout << "The largest number is: " << largest << endl;
        return 0;
    }
 







  
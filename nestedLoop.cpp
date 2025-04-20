#include<iostream>
using namespace std;

int main(){

// Q1 : WAP to print a squre pattern using nested loop 
//pattern 1
  int n;
  int num = 1;
  char ch = 'd';
     cout<<"Enter a number"<<endl;
     cin>>n;

     cout << endl;
     cout << endl;


//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= n; j++){
//             cout <<"*"<<" ";
//         }
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;
    

//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= n; j++){
//             cout << j<<" ";
//         }
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;
    
//   // pattern 2
//     for(int i = 0; i <= n; i++){
//         char ch = 'A';
//         for(int j = 1; j <= n; j++){
//             cout <<ch<<" ";
//             ch+=1;
//         }
//         cout << endl;
//     }

//     cout << endl;
//     cout << endl;
//   //pattern 3 pattern for extra code not same
//     for(int i = 1; i <= n; i++){

//         for(int j = 1; j <= n; j++){
//             cout << num<<"    ";
//             num++;
//         }
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;

//  // pattern 4
    
//     for(int i = 1; i <= n; i++){
    
//         for(int j = 1; j <= n; j++){
//             cout << ch<<" ";
//             ch+=1;
//         }
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;


// // pattern 5 triangle pattern
//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= i; j++){
//             cout << "* ";
//         }
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;

// // pattern 6 triangle pattern
//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= i; j++){
//             cout<< i <<" ";
//         } 
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;

// // pattern 7 triangle pattern
//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= i; j++){
//             cout<< j <<" ";
//         } 
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;

// // pattern 8 triangle pattern
//     for(int i = 1; i <= n; i++){
//         for(int j = 1; j <= i; j++){
//             cout<<ch<<" ";
            
//         }
//         ch+=1;
//         cout << endl;
//     }
//     cout << endl;
//     cout << endl;
// pattern 9 triangle pattern revrse
    for(int i = n; i>=1; i--){
        for(int j = i; j>=1; j--){
            cout<<ch<<" ";
            
        }
        ch-=1;
        
        cout << endl;
  }
        cout << endl;
        cout << endl;
}
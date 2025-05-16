# include<iostream>
#include<vector>
using namespace std;
int main(){
//    double age = 23.5;
//    bool isTrue = true;
//    char initial = 'G';//type conversion / implicit conversion from char to int    
//    int number = initial;// ASCII value of G
//     cout<<number<<endl;
//    cout<<sizeof(isTrue)<<endl;

//    cout<<isTrue<<endl;
//     cout<<sizeof(age)<<endl;
//     cout<<age<<endl;

//     int newage = int(age); // type cacsting / explicit conversion from double to int
//     cout<<newage<<endl;
//     cout<<"gaurav chauhan\n ji"<<endl;

    //take input from user
    // int a, b;
    // cout<<a<<endl; // garbage value
    // cout<<b<<endl; // garbage value
    // cout<<"Enter two numbers"<<endl;
    // cin>>a>>b;
    // cout<<"The sum of "<<a<<" and "<<b<<" is "<<a+b<<endl;
    // cout<<"The difference of "<<a<<" and "<<b<<" is "<<a-b<<endl;
    // cout<<"The product of "<<a<<" and "<<b<<" is "<<a*b<<endl;


    // return 0;
    //arithmatic operator
    // +, -, *, /, %
    // use
    // int a = 10, b = 3;
    // cout<<a+b<<endl; // addition
    // cout<<a-b<<endl; // subtraction
    // cout<<a*b<<endl; // multiplication
    // cout<<a/b<<endl; // division
    // cout<<a%b<<endl; // modulus
    
    // cout<<(float)a/b<<endl; // type casting / explicit conversion from int to float
    // cout<<a/b<<endl; // integer division
    // cout<<(float)a/b<<endl; // float division

    //relationol operators
    // ==, !=, >, <, >=, <=
    // use  
//     int a = 10, b = 3;
//     cout<<(a<=b)<<endl; // less than or equal to true->1, false->0
//     cout<<(a>=b)<<endl; // greater than or equal to
//     cout<<(a==b)<<endl; // equal to
//     cout<<(a!=b)<<endl; // not equal to
//     cout<<(a>b)<<endl; // greater than
//     cout<<(a<b)<<endl; // less than

//     //logical operators
//     // && and, || or, ! not
//     // use
//     int a = 10, b = 3;
//     cout<<(a<=b && a>=b)<<endl; // and
//     cout<<(a<=b || a>=b)<<endl; // or
//     cout<<!(a<=b)<<endl; // not

// int a = 10;
// int b = a++;// post increment

// cout<<a<<endl; // 11
// cout<<b<<endl; // 10

// int c = 9;// pre increment
// int d = ++c;// pre increment    

// cout<<c<<endl; // 10
// cout<<d<<endl; // 10

// int e = 10;
// int f = e--;// post decrement

//  cout<<e<<endl; // 9
//  cout<<f<<endl; // 10

//  int g = 9;// pre decrement
//  int h = --g;// pre decrement

//     cout<<g<<endl; // 8
//     cout<<h<<endl; // 8



//if-else statement
    // int n =45;
    // if(n>=0){
    //    cout<<"Positive"<<endl;
    // }else {
    //    cout<<"Negative"<<endl;
    // } 
    //vote - programm if elseif-else
    // int age ;
    // cout<<"Enter your age"<<endl;
    // cin>>age;
    // if(age>=18){
    //     cout<<"You are eligible to vote"<<endl;
    // }else if(age>=16 && age<18){
    //     cout<<"You are eligible to vote in some states"<<endl;
    // }else{
    //     cout<<"You are not eligible to vote"<<endl;
    // }

   // even - odd check
//    int n;
//     cout<<"Enter a number"<<endl;
//     cin>>n;
//    if(n%2==0){
//          cout<<n<<" is even"<<endl;
//     }else{
//          cout<<n<<" is odd"<<endl;
//     }   
// 
// grade check

//    int marks;
//    cout<<"Enter your marks"<<endl;
//    cin>>marks;
//    if(marks>=90 && marks<=100){
//         cout<<"A+"<<endl;
//    }else if(marks>=80 && marks<90){
//         cout<<"A"<<endl;
//    }else if(marks>=70 && marks<80){
//         cout<<"B"<<endl;
//    }else if(marks>=60 && marks<70){
//         cout<<"C"<<endl;
//    }else if(marks>=50 && marks<60){
//         cout<<"D"<<endl;
//    }else if(marks>=40 && marks<50){
//         cout<<"E"<<endl;
//    }else {
//         cout<<"you are fail"<<endl;}


// find character is lowercase or uppercase
//    char ch;
//    cout<<"Enter a character"<<endl;
//    cin>>ch;
//    if(ch>='a' && ch<='z'){
//         cout<<ch<<" is lowercase"<<endl;
//    }else if(ch>='A' && ch<='Z'){
//         cout<<ch<<" is uppercase"<<endl;
//    }else{
//         cout<<ch<<" is not an alphabet"<<endl;
//    }


//find the charcter is uppercase or lowercase using ascii value
//     char ch;
//   cout<<"Enter a character"<<endl;
//     cin>>ch;
//     if(ch>=65 && ch<=90){
//          cout<<ch<<" is uppercase"<<endl;
//     }else if(ch>=97 && ch<=122){
//          cout<<ch<<" is lowercase"<<endl;
//     }else{
//          cout<<ch<<" is not an alphabet"<<endl;
//     }
   // ternary statement
    //  int a = 10, b = 20 , c = 30, d = 40;
    //  int max = (a>b)? a:b;

    //  cout<<max<<endl;
    //  cout<<(c>d? "higher" : "lower")<<endl;

    //loops

       //print table using while loop
    //    int n, i=1;
    //      cout<<"Enter a number"<<endl;
    //         cin>>n;
    //    while(i<=10){
    //       cout<<n*i<<endl;
    //       i++;
    //  }
    
    // int n, i=1;
    // cout<<"Enter a number"<<endl;
    // cin>>n;
//infinite loop
    // while(i<=n){
    //     cout<<"I LOVE U GAURAV"<<endl;
           
    // }   
    
    
     //for loop
    //  int n;
    //  cout<<"Enter a number"<<endl;
    //  cin>>n;
    //  for(int i=1; i<=10; i++){
    //      cout<<n*i<<endl;
    //  }

   
    // int n;
    // cout<<"Enter a number"<<endl;
    // cin>>n;
    // for(int i=2; i<(n-1); i++){
    //     if(n%i==0){
    //         cout<<n<<" is not prime"<<endl;
    //         break;
    //     }else{  
    //         cout<<n<<" is prime"<<endl;
    //         break;
    //     }
    // }    
    //    int n,i=1,sum = 0;
    //       cout<<"Enter a number"<<endl;
    //       cin>>n;

        //   while(i<=n){
        //     sum += i;

        //     i++;
        
        // }
        // cout<<sum<<endl;
      //for(int i=1; i<=n; i+=2)
    //    for(int i=1; i<=n; i++){
    //         if(i% 2 == 0){
    //            sum += i; 

    //         }

          
    //     }
    //     cout<<sum<<endl;

    // int n, i = 1, sum = 0;
    // cout << "Enter a number" << endl;
    // cin >> n;
    // do{
       
    //     sum += i;
    //     i++;
    // } while (i <= n);
    // cout << sum << endl;
    
    // return 0;

    // int n,i = 2;
    // cout<<"enter a number :"<<endl;
    // cin>>n;
    // write a program to find prime number using do while loop
    // do{
    //     if(n%i==0){
    //         cout<<n<<" is not prime"<<endl;
    //         break;
    //     }else{
    //         cout<<n<<" is prime"<<endl;
    //         break;
    //     }
    //     i++;
    // }while(i<n);
    // return 0;

    //using boolen function to find prime number

    // bool isPrime = true;
    // for(int i = 2; i*i <= n; i++){
    //     if(n % i == 0){
    //         isPrime = false;
    //         break;
    //     }
    // }

    // if(isPrime){
    //     cout << n << " is prime" << endl;   
    // }else{
    //     cout << n << " is not prime" << endl;   
    // }
    // return 0;

    //nested loop

    //  for(int i = 1; i <= 5; i++){
    //     for(int j = 1; j <= 5; j++){ 
    //         cout << "* ";
    //     }
    //     cout << endl;
    //  }

//factorial of a number using loop

// double n;
// cout<<"Enter a number"<<endl;
// cin>>n;
// double fact = 1;
// for(int i = 1; i <= n; i++){
//     fact *= i;
// }
// cout << "Factorial of " << n << " is " << fact << endl;
// return 0;


// vector
 int n =5;
 int arr[5]= {1,2,3,4,5};
 for(int st =0; st<n; st++){
    for(int end= st; end<n; end++){
        for(int i = st; i<=end; i++){
            cout<<arr[i];

           }
           cout<<" ";

       }
       cout<<endl;
    
 }
 return 0;
}
/* Problem:
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

Given a number n, print n-th Fibonacci Number.
*/


import java.util.Scanner;

class Fibonacci{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of Fibonacci");
        int num = sc.nextInt();
        int result = getFibonacciNumber(num);
        System.out.println("The nth fibonacci number is: "+result);
    }

    //recursive solution
    public static int getFibonacciNumber(int num){
        if(num==0 || num==1) 
            return num;
        return getFibonacciNumber(num-1) + getFibonacciNumber(num-2);

    }
    
    //iterative solution
    public static long getFibonacciNumberIteratively(int num){
        long a = 0, b=1, c;
        if (num == 0)
          return a;
        for(long i=2; i<=num; i++){
          c = a + b;
          a=b;
          b=c;
     }
     return b;
    }
}
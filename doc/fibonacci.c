#include <stdio.h>
/*Auteur: Emmanuel Malan
date : 09-09-19 ; langage : c
objet :Fibonacci */

//fonction recursive
int fibonacci_1(int n){
    if(n<0) 
        printf("nombre incorrect") ;
    else if (n==1)
        return 0 ;
    else if (n==2 )
        return 1 ;
    else
        return fibonacci_1(n-1)+fibonacci_1(n-2) ;
}

//fonction non recursive
int fibonacci_2(int n){
    int a = 0 ; int b = 1 ;
    int i ; int c;
    if (n < 0)
        printf("nombre incorrect") ;
    else if (n == 0)
        return a ;
    else if (n == 1 )
        return b ;
    else{
        for (i=2;i<n;i++){
            c = a + b ;
            a = b ;
            b = c ;
        }
        return b ;
    }
}
// Programme principale
main(){
	printf("fibonacci(9)=%d \n",fibonacci_1(9));
	printf("fibonacci(0)=%d \n",fibonacci_2(0));
}

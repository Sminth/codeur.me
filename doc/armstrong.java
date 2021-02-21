public class Armstrong{  
  public static void main(String[] args)  {  
    int c=0,a,temp;  
    int n=153;//nombre à verifier  
    temp=n;  
    while(n>0)  
    {  
    a=n%10;  
    n=n/10;  
    c=c+(a*a*a);  
    }  
    if(temp==c)  
    System.out.println(temp+" est un nombre d'armstrong");   
    else  
        System.out.println(temp+" n'est pas un nombre d'armstrong");   
   }  
}  
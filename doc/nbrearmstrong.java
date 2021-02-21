package daniequation;

public class nbrearmstrong {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b,n,i;

		for(i=100;i<=500;i++) {
			n=i;
			b=0;
			while(n>0){
			a=n%10;
			b=b+(a*a*a);
			n=n/10;
			}
		if(b==i)	{
			System.out.println(i+"est un nombre d'Armstrong");
		}
	   }
	}
}

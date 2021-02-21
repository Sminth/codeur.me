public class Dichotomie{
  /*
  tab[] : le tableau dans lequel on va chercher la valeur
  l : dernier élément
  f : premier élément
  val : valeur à trouver
  */
  public static void Dichotomie(int tab[], int f, int l, int val){
    int mid = (f + l)/2;
    while(f <= l){
      if (tab[mid] < val){
        f = mid + 1;   
      }else if(tab[mid] == val){
        System.out.println("L'élément se trouve à l'index: " + mid);
        break;
      }else{
         l = mid - 1;
      }
      mid = (f + l)/2;
   }
    if (f > l){
      System.out.println("L'élément n'existe pas!");
    }
   }
 
  public static void main(String args[]){
    int tab[] = {1, 2, 3, 4, 5, 6, 7};
    int val = 4;
    int l = tab.length-1;
    Dichotomie(tab,0,l,val);  
  }
}
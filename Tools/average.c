#include <stdio.h>
int main()
{    
  int num1, num2;    
  float avg; 
  printf("Enter first number: ");  
  scanf("%d",&num1); 
  printf("Enter second number: "); 
  scanf("%d",&num2);   
  avg= (float)(num1+num2)/2;  
  //%.2f is used for displaying output upto two decimal places    
  printf("Average of %d and %d is: %.2f",num1,num2,avg); 
  return 0;
}

#include <stdio.h>
int main()
{
    int r,c,a[50][50],tran[50][50];        
    printf("enter number of rows\n");       
    scanf("%d",&r);
    printf("enter number of columns\n");    
    scanf("%d",&c);
    printf("matrix a elements\n");        
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            printf("matrix a[%d][%d]:",i,j);
            scanf("%d",&a[i][j]);
        }
    }
    // transpose of matrix
    printf("transpose of matrix a\n");
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            tran[j][i]=a[i][j];     
        }
    }
    for(int i=0;i<c;i++)        
    {
        for(int j=0;j<r;j++)
        {
              printf("%d ", tran[i][j]);
        }
        printf("\n");
    }
 return 0;
}

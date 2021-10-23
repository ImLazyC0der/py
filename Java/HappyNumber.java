class Solution {
public boolean isHappy(int n) {
int sum=0,r;
a: while(true)
{while(n!=0)
{r=n%10;
sum+=r*r;
n=n/10;}
n=sum;
if(sum!=1&&sum>9)
{sum=0;
continue a;}
if(sum==1||sum==7)
return true;
else
return false;
}
}
}

#code java
class Solution {
public int countPrimeSetBits(int left, int right) {
int result=0;
for (int i = left; i <= right; i++){
int tam = i, dem=0;


while (tam > 0){
if (tam % 2 == 1) dem++;
tam=tam / 2;
}

if (dem != 1){
if (dem == 2 | | dem == 3) result++;
else {
for (int j=2;j < dem;j++){
if (dem % j == 0)
break;
if (j == dem - 1) result++;
}
}
}

}
return result;
}
}
#code java

class Solution {
public List < Integer > selfDividingNumbers(int left, int right) {
int check, i, k;
List < Integer > result = new ArrayList <> ();
for (i=left; i <= right; i++){
k = i;


while (k > 0){
check = k % 10;
if ((check == 0) | | (i % check != 0) ){
break;
}
if (k < 10){
result.add(i);
}
k = k / 10;
}

}

return result;
}
}
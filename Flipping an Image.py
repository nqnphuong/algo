#code java

class Solution {
public int[][] flipAndInvertImage(int[][] image) {
int t;
for (int[] row: image

){
for (int i = 0; i < row.length / 2; i++){
    t = row[i];
row[i] = row[row.length - i-1];
row[row.length - i-1] = t;
}
}

for (int[] row: image){
for (int i = 0; i < row.length; i++){
if (row[i] == 0) row[i] = 1;
else row[i] = 0;
}
}

return image;
}
}
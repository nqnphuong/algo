#code java
class Solution {
    public List < Boolean > kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        int n = candies.length;
        List < Boolean > result = new ArrayList <> ();
        for (int i=0; i < n;i++){
        if (max < candies[i]) max = candies[i];
        }

        for (int i = 0; i < n; i++) {
        result.add((candies[i] + extraCandies) >= max);
        }


        return result;
    }
}
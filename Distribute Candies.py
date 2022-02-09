#code java
class Solution {
    public int distributeCandies(int[] candyType) {
        int result = 0;
        int test = candyType.length/2;
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int candy : candyType) list.add(candy);
        list = new ArrayList<Integer>(new LinkedHashSet<Integer>(list));
        int size = list.size();
        if (test <= size) return test;
        else return size;
    }
}
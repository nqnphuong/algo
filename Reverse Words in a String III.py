#code java

class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        String result = null;
        for (String word : words){
            StringBuilder str = new StringBuilder(word);
            word = str.reverse().toString();
            result = result + " " + word;
        }
        return result.substring(5);
    }
}
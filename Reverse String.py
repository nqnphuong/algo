#code java
class Solution {
    public void reverseString(char[] s) {
        char t = 'a';
        for (int i=(s.length - 1 )/2 ; i >= 0 ; i--){
            t = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i - 1] = t;
        }
    }
}
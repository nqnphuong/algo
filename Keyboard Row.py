#code java

class Solution {
public String[] findWords(String[] words) {
char[] row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'};
char[] row2 = {'a', 'A', 's', 'S', 'd', 'D', 'F', 'f', 'G', 'g', 'h', 'H', 'J', 'j', 'K', 'k', 'l', 'L'};
char[] row3 = {'z', 'Z', 'x', 'X', 'C', 'c', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M'};
ArrayList < Character > map1 = new ArrayList < Character > ();
ArrayList < Character > map2 = new ArrayList < Character > ();
ArrayList < Character > map3 = new ArrayList < Character > ();
ArrayList < String > result = new ArrayList < String > ();

for (char c: row1

) map1.add(c);
for (char c: row2)
map2.add(c);
for (char c: row3)
map3.add(c);

for (String word: words)
{
    boolean
b = true;
if (map1.contains(word.charAt(0)))
{
for (int i = 0; i < word.length(); i++){
if (!map1.contains(word.charAt(i))){
b = false;
break;
}
}
} else if (map2.contains(word.charAt(0))){
for ( int i = 0; i < word.length(); i++){
if (!map2.contains(word.charAt(i))){
b = false;
break;
}
}
} else if (map3.contains(word.charAt(0))){
for ( int i = 0; i < word.length(); i++){
if (!map3.contains(word.charAt(i))){
b = false;
break;
}
}
}
if (b == true){
result.add(word);
}
}

String res[] = new String[result.size()];
for (int i = 0; i < res.length; i++)
res[i] = result.get(i);

return res;
}
}
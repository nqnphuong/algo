#code java

class Solution {
public String toGoatLatin(String sentence) {
String result = null;
int j=1;
String[] words = sentence.split(" ");
for (String word: words

){
    String
end = "";
for (int i=0; i < j;i++)
{
    end = end + "a";
}
j + +;
char
begin = word.charAt(0);
if (
            begin == 'a' | | begin == 'e' | | begin == 'i' | | begin == 'o' | | begin == 'u' | | begin == 'A' | | begin == 'E' | | begin == 'I' | | begin == 'O' | | begin == 'U')
{
    word = word + "ma" + end;
} else {
    word = word.substring(1);
word = word + begin + "ma" + end;
}

result = result + " " + word;

}

return result.substring(5);
}
}
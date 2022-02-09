#code C


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int *result = (int *)malloc(sizeof(int) * 2);
    int i=0, j=numbersSize-1, tong;
    while (i<j){
        tong = numbers[i] + numbers[j];
        if (tong > target) {
            j--;
        } else if (tong < target) {
            i++;
        } else {
            result[0] = i + 1;
            result[1] = j + 1;
            *returnSize = 2;
            break;
        }
    }
    return result;
}
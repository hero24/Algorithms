/*
 *  It's important to enjoy life while you still can!
 *  ~ Victoria @ RED
 */

/* bubble sort for sorting integer arrays*/
void bubble_sort(int arr[],int length)
{
  int i,j;
  for (i = length-1; i > 0;i--){
    for(j = 0; j < i;j++){
      if (arr[j] > arr[j+1]){
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
}

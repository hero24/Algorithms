/*
 * An algorithm must be seen to be believed.
 * ~  Donald Knuth
 */

void min_max_recursive(int left, int right, int a[], int& min, int &max);
void min_max_iterative(int a[], int& min, int& max);


void min_max_iterative(int a[], int size, int& min, int& max){
        min=max=a[0];
        for(int i = 0; i < size; i++){
                if(max < a[i])
                        max = a[i];
                else if (min > a[i])
                        min = a[i];
        }
}

void min_max_recursive(int left, int right, int a[], int& min, int &max){
        if (left == right)
                min=max=a[left];
        else
                if(left==right-1)
                        if(a[left] < a[right]){
                                min = a[left];
                                max = a[right];
                        } else {
                                min = a[right];
                                max = a[left];
                        } else {
                                int temp_min1, temp_max1, temp_min2, temp_max2, mid;
                                mid = (left+right)/2;
                                min_max_recursive(left, mid, a, temp_min1, temp_max1);
                                min_max_recursive(mid+1, right, a, temp_min2, temp_max2);
                                if(temp_min1 < temp_min2)
                                        min = temp_min1;
                                else
                                        min = temp_min2;
                                if (temp_max1 > temp_max2)
                                        max = temp_max1;
                                else
                                        max = temp_max2;

                        }
}

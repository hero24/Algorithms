// The best or nothing at all. ~ Gottlieb Daimler
#include <stdlib.h>

int containsDuplicate(int* arr, int arrsz)
{
        unsigned char* bloom = calloc(arrsz*2, sizeof(unsigned char));
        int sz = arrsz*2;
        int i,j, val, bloom_check;
        for(i = 0; i < arrsz; i++){
                val = arr[i];
                bloom_check = (val ^ ((val<<5) + val + (val >> 2))) % sz;
                if (bloom[bloom_check]){
                        for(j=0; j< i;j++){
                                if(val == arr[j])
                                        return 1;
                        }
                }
                bloom[bloom_check] = 1;
        }
        free(bloom);
        return 0;
}

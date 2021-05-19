#include <string.h>
#define SHIFT_SZ 26*2+1

/*
* "You know...my flower...I'm responsible for her. 
*  And she's so weak! And so naive. 
*  She has four ridiculous thorns to defend her against the world."
* ~ Antoine de Saint-Exupery
*/

static int index_sh(char c){
        switch(c){
                case ' ': return 0;
                default:
                          if (c >= 'a' && c <= 'z')
                                  return c - 'a' + 1;
                          else
                                  return c - 'A' + 27;
        }
}

static void init_shifts(char sample[], int shift[]){
        int i, M = strlen(sample);
        for(i = 0; i < SHIFT_SZ; i++)
                shift[i] = M;
        for(i = 0; i < M; i++){
                shift[index_sh(sample[i])] = M-i-1;
        }
}

/* Boyer-Moore text searching algorithm */
int bm(char sample[], char test[]){
        int shift[SHIFT_SZ];
        init_shifts(sample, shift);
        int i, j, N = strlen(test), M = strlen(sample);

        for(i = M-1, j = M-1; j > 0; i--, j--){
                while(test[i] != sample[j]){
                        int x = shift[index_sh(test[i])];
                        if(M-j > x)
                                i += M-j;
                        else
                                i += x;
                        if (i >= N)
                                return -1;
                        j = M - 1;
                }
        }
        return i;
}

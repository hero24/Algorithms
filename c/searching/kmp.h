#include <string.h>
/*
 * "A coward is incapable of exhibiting love; it is the prerogative of the brave" ~ Ghandi
 */

// Helper function for initiating shifts
static void init_shifts(char sample[], int shift[], int size)
{
        int i,j;
        shift[0] = -1;
        for(i = 0, j = -1; i < size-1; i++, j++, shift[i]=j)
                while ((j >= 0) && (sample[i] != sample[j]))
        j = shift[j];
}

/*
 * Knuth-Morris-Pratt text searching algorithm
 */
int kmp(char sample[], char test[])
{
        int i,j, N=strlen(test), M=strlen(sample);
        int shift[M];
        init_shifts(sample, shift, M);
        for(i = 0, j = 0; (i < N) && (j < M); i++, j++){
                while((j >= 0) && (test[i] != sample[j]))
                        j = shift[j];
        }
        if (j == M)
                return i - M;
        else
                return -1;

}

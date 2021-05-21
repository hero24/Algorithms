#include <string.h>
#define PRIME_N 33554393
#define B_N 64
#define B_SH 6

/*
* "Rough diamonds may sometimes be mistaken for worthless pebbles."
*  ~ Thomas Browne
*/

static int index_s(char c){
        switch(c){
                case ' ': return 0;
                default:
                          if (c >= 'a' && c <= 'z')
                                  return c - 'a' + 1;
                          else
                                  return c - 'A' + 27;
        }
}

/* Rabin-Karp searching algorithm */
int rk(char sample[], char test[]){
        int i, M = strlen(sample), N = strlen(test);
        unsigned long bM_1 = 1, Hs = 0, Ht = 0;
        for(i = 0; i < M; i++){
                Hs = (Hs * B_N + index_s(sample[i])) % PRIME_N;
                Ht = (Ht * B_N + index_s(test[i])) % PRIME_N;
        }
        for(i = 1; i < M; i++){
                bM_1 = (B_N * bM_1) % PRIME_N;
        }
        for(i = 0; Hs != Ht; i++){
                // All the prime number multupilications could be optimized away using shifts
                // and as we know shifts are much faster operations than multiplications.
                //Ht = (Ht + (PRIME_N << B_SH) - index_s(test[i]) * bM_1) % PRIME_N; ...
                Ht = (Ht + B_N * PRIME_N - index_s(test[i]) * bM_1) % PRIME_N;
                //Ht = ((Ht << B_SH) + index_s(test[i+M])) % PRIME_N;
                Ht = (Ht * B_N + index_s(test[i+M])) % PRIME_N;
                if (i > N-M)
                        return -1;
        }
        return i;
}

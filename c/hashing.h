/*
*   "In pursuit of knowledge, every day something is acquired. 
*    In pursuit of wisdom, every day something is dropped."  
*    ~ Lao Tzu
*/

#define CODE_OFFSET 64

int sum_modulo_2(char* str){
        int hash = 0;
        char c;
        while((c=*(str++)) != '\0'){
                hash += (c-CODE_OFFSET) % 2;
        }
        return hash;
}

int sum_modulo_2_rshift(char* str){
        int i, hash = 0;
        char c;
        for(i=0; (c=*(str++)) != '\0'; i++){
                hash += ((c-CODE_OFFSET)>>i) % 2;
        }
        return hash;
}

int Rmax(char* str, int rmax){
        int tmp;
        for(tmp = 0; *str != '\0'; str++)
                tmp = (CODE_OFFSET*tmp+(*str)) % rmax;
        return tmp;
}

unsigned long djb2(unsigned char* str){
        unsigned long hash = 5381;
        int c;
        while (c = *str++)
                hash = ((hash << 5) + hash) + c;
        return hash;
}

unsigned long sdbm_hash(unsigned char* str){
        unsigned long hash = 0;
        int c;
        while (c = *str++)
                hash = c + (hash << 6) + (hash << 16) - hash;
        return hash;
}

unsigned long k_n_r(unsigned char* str){
        unsigned long hash = 0;
        int c;
        while (c = *str++)
                hash += c;
        return hash;
}

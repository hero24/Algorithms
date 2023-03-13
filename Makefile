.PHONY : python c
all:
        @echo "make: [python|c]"
python:
        cd python && python3 __init__.py capi  && cd ..

c:
        mkdir build
        mkdir tmp
        cp c/hashing.h tmp/hashing.c
        cp c/searching/bm.h tmp/bm.c
        cp c/searching/kmp.h tmp/kmp.c
        cp c/searching/rk.h tmp/rk.c
        cp c/sorting/bubble_sort.h tmp/bubble_sort.c
        gcc -c -fpic tmp/hashing.c -o tmp/hashing.o
        gcc -c -fpic tmp/bm.c -o tmp/bm.o
        gcc -c -fpic tmp/kmp.c -o tmp/kmp.o
        gcc -c -fpic tmp/rk.c -o tmp/rk.o
        gcc -c -fpic tmp/bubble_sort.c -o tmp/bubble_sort.o
        gcc -shared -o build/hasing_h24.so tmp/hashing.o
        gcc -shared -o build/bm_h24.so tmp/bm.o
        gcc -shared -o build/kmp_h24.so tmp/kmp.o
        gcc -shared -o build/rk_h24.so tmp/rk.o
        gcc -shared -o build/bubble_sort_h24 tmp/bubble_sort.o
        rm -rf tmp

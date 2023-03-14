.PHONY : python c cpp
all:
        @echo "make: [python|c]"
python:
        cd python && python3 __init__.py capi  && cd ..

define c_files
        cp c/hashing.h tmp/hashing.c
        cp c/searching/bm.h tmp/bm.c
        cp c/searching/kmp.h tmp/kmp.c
        cp c/searching/rk.h tmp/rk.c
        cp c/sorting/bubble_sort.h tmp/bubble_sort.c
endef

define cpp_files
        cp cpp/min_max.hpp tmp/min_max.cpp
endef

c:
        mkdir build
        mkdir tmp
        $(c_files)
        gcc -c -fpic tmp/hashing.c -o tmp/hashing.o
        gcc -c -fpic tmp/bm.c -o tmp/bm.o
        gcc -c -fpic tmp/kmp.c -o tmp/kmp.o
        gcc -c -fpic tmp/rk.c -o tmp/rk.o
        gcc -c -fpic tmp/bubble_sort.c -o tmp/bubble_sort.o
        gcc -shared -o build/h24_hasing.so tmp/hashing.o
        gcc -shared -o build/h24_bm.so tmp/bm.o
        gcc -shared -o build/h24_kmp.so tmp/kmp.o
        gcc -shared -o build/h24_rk.so tmp/rk.o
        gcc -shared -o build/h24_bubble_sort.so tmp/bubble_sort.o
        rm -rf tmp

cpp:
        mkdir build
        mkdir tmp
        $(cpp_files)
        g++ -c tmp/min_max.cpp -o tmp/min_max.o
        g++ -shared -o build/h24_min_max.so tmp/min_max.o
        $(c_files)
        g++ -c tmp/hashing.c -o tmp/hashing.o
        g++ -c tmp/bm.c -o tmp/bm.o
        g++ -c tmp/kmp.c -o tmp/kmp.o
        g++ -c tmp/rk.c -o tmp/rk.o
        g++ -c tmp/bubble_sort.c -o tmp/bubble_sort.o
        g++ -shared -o build/h24_hasing.so tmp/hashing.o
        g++ -shared -o build/h24_bm.so tmp/bm.o
        g++ -shared -o build/h24_kmp.so tmp/kmp.o
        g++ -shared -o build/h24_rk.so tmp/rk.o
        g++ -shared -o build/h24_bubble_sort.so tmp/bubble_sort.o
        rm -rf tmp

# Algorithms

## Introduction
A repository containing implementation of different algorithms in various langugages. This has been created as container for code I have wrote for either certain purpose or learning of language or algorithm and is updated as I have time or need.

## Contents

### Languages

|Language|Make support|
|--------|------------|
|AutoIt|No|
|C|Yes|
|C++|Yes|
|Erlang|No|
|io|No|
|Lua|No|
|Python|Yes|
|Python C API|Yes (included in Python)|
|Scala|Yes|

### Algorithms

|Algorithm|Languages|Category|
|---------|---------|--------|
|`add_polynomials`|`Python`|Math|
|`Adfgx`|`Python`|Cryptography|
|`Alberti_disc`|`Python`|Cryptography|
|`ascii`|`Python`|Cryptography|
|`BFS`|`Python`|Graphs|
|`bellman_ford`|`Python`|Graphs|
|`Boyer-Moore`|`C`,`Python C API`|Searching|
|`BubbleSort`|`AutoIT`, `C`, `Python`|Sorting|
|`Caesar_cipher`|`Python`|Cryptography|i
|`DFS`|`Python`|Graphs|
|`dijkstra`|`Python`|Graphs|
|`Djb2`|`C`, `Python C API`|Hashing|
|`Duplicate`|`C`|Searching|
|`Enigma`|`Python`|Cryptography|
|`Factorial`|`AutoIT`, `Erlang`|Math|
|`Fibonacci`|`C++`,`Erlang`,`Python`|Math|
|`floyd_warshall`|`Python`|Graphs`|
|`GaussianSum`|`Scala`|Math|
|`gauss`|`Python`|Math|
|`HeapSort`|`AutoIT`|Sorting|
|`horner`|`Python`|Math|
|`InsertionSort`|`AutoIT`,`Python`|Sorting|
|`is_prime`|`Lua`|Math|
|`Knuth-Morris-Pratt`|`C`,`Python C API`|Searching|
|`K-n-r`|`C`, `Python C API`|Hashing|
|`KruskalMST`|`Python`|Graphs|
|`lagrange_interpolation`|`Python`|Math|
|`LZW`|`io`, `Python`|Compression|
|`linear_function_result`|`Python`|Math|
|`MergeSort`|`AutoIT`, `Python`|Sorting|
|`Min-max`|`C++`|Searching|
|`multiply_polynomials`|`Python`|Math|
|`newton`|`Python`|Math|
|`polynomial_std`|`Python`|Maths|
|`Playfair_cipher`|`Python`|Cryptography|
|`PrimMST`|`Python`|Graphs|
|`QuickSort`|`AutoIT`|Sorting|
|`Rabin-Karp`|`C`,`Python C API`|Searching|
|`RLE`|`Python`|Compression|
|`roy_warshall`|`Python`|Graphs|
|`Rmax`|`C`,`Python C API`|Hashing|
|`Sdmb_hash`|`C`,`Python C API`|Hashing|
|`simpson_integration`|`Python`|Math|
|`SelectionSort`|`Python`|Sorting|
|`Sequential_search`|`Python`|Searching|
|`SheakerSort`|`AutoIT`|Sorting|
|`Sieve_eratosthenes`|`Python`|Math|
|`Sieve_sundaram`|`Python`|Math|
|`sum_modulo_2`|`C`,`Python C API`|Hashing|
|`sum_modulo_2_rshift`,`Python C API`|`C`|Hashing|
|`Tabula_recta`|`Python`|Cryptography|
|`Vigenere`|`Python`|Cryptography|
|`xor`|`Python`|Cryptography|

## Building

Make build system currently supports C, C++ Python including the C API (if enabled by defining `PYCAPI=Y`) and Scala. Building is as simple as running make and providing langauge:

For C:
`make c`

For C++
`make cpp`

For Python:
`make python`

For Python with C API:
`PYCAPI=Y make python`

For Scala:
`make scala`



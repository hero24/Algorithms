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
|`Adfgx`|`Python`|Cryptography|
|'Alberti_disc`|`Python`|Cryptography|
|`Boyer-Moore`|`C`,`Python C API`|Searching|
|`BubbleSort`|`AutoIT`, `C`, `Python`|Sorting|
|`Caesar_cipher`|`Python`|Cryptography|
|`Djb2`|`C`, `Python C API`|Hashing|
|`Duplicate`|`C`|Searching|
|`Enigma`|`Python`|Cryptography|
|`Factorial`|`AutoIT`, `Erlang`|Math|
|`Fibonacci`|`C++`,`Erlang`,`Python`|Math|
|`GaussianSum`|`Scala`|Math|
|`HeapSort`|`AutoIT`|Sorting|
|`InsertionSort`|`AutoIT`,`Python`|Sorting|
|`is_prime`|`Lua`|Math|
|`Knuth-Morris-Pratt`|`C`,`Python C API`|Searching|
|`K-n-r`|`C`, `Python C API`|Hashing|
|`LZW`|`io`, `Python`|Compression|
|`MergeSort`|`AutoIT`, `Python`|Sorting|
|`Min-max`|`C++`|Searching|
|`Playfair_cipher`|`Python`|Cryptography|
|`QuickSort`|`AutoIT`|Sorting|
|`Rabin-Karp`|`C`,`Python C API`|Searching|
|`Rmax`|`C`,`Python C API`|Hashing|
|`Sdmb_hash`|`C`,`Python C API`|Hashing|
|`SelectionSort`|`Python`|Sorting|
|`Sequential_search`|`Python`|Searching|
|`SheakerSort`|`AutoIT`|Sorting|
|`Sieve_eratosthenes`|`Python`|Math|
|`Sieve_sundaram`|`Python`|Math|
|`sum_modulo_2`|`C`,`Python C API`|Hashing|
|`sum_modulo_2_rshift`,`Python C API`|`C`|Hashing|
|`Tabula_recta`|`Python`|Cryptography|
|`Vigenere`|`Python`|Cryptography|

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



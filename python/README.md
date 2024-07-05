# Algorithms

## Introduction
A repository containing implementation of different algorithms. This has been created as container for code I have wrote for either certain purpose or learning of language or algorithm and is updated as I have time or need.

## Contents

### Algorithms

|Algorithm|Language|Category|
|---------|---------|--------|
|`Adfgx`|`Python`|Cryptography|
|`Alberti_disc`|`Python`|Cryptography|
|`Boyer-Moore`|`Python C API`|Searching|
|`BubbleSort`|`Python`|Sorting|
|`Caesar_cipher`|`Python`|Cryptography|
|`Djb2`|`Python C API`|Hashing|
|`Enigma`|`Python`|Cryptography|
|`Fibonacci`|`Python`|Math|
|`InsertionSort`|`Python`|Sorting|
|`Knuth-Morris-Pratt`|`Python C API`|Searching|
|`K-n-r`|`Python C API`|Hashing|
|`LZW`|`Python`|Compression|
|`MergeSort`|`Python`|Sorting|
|`Playfair_cipher`|`Python`|Cryptography|
|`Rabin-Karp`|`Python C API`|Searching|
|`Rmax`|`Python C API`|Hashing|
|`Sdmb_hash`|`Python C API`|Hashing|
|`SelectionSort`|`Python`|Sorting|
|`Sequential_search`|`Python`|Searching|
|`Sieve_eratosthenes`|`Python`|Math|
|`Sieve_sundaram`|`Python`|Math|
|`sum_modulo_2`|`Python C API`|Hashing|
|`sum_modulo_2_rshift`|`Python C API`|Hashing|
|`Tabula_recta`|`Python`|Cryptography|
|`Vigenere`|`Python`|Cryptography|

## Building

Make build system currently supports C, C++ Python including the C API (if enabled by defining `PYCAPI=Y`) and Scala. Building is as simple as running make and providing langauge:

For Python:
`make python`

For Python with C API:
`PYCAPI=Y make python`

## PIP

Package can be installed via pip.
`pip install hero24.algorithms`

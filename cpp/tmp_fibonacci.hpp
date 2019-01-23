/*
 * Fibonacci sequence generator written using C++ template metaprogramming.
 */
 
// "There is no great genius without a mixture of madness." ~ Aristotle
template <int x>
struct fibonacci{
    enum{
        value = fibonacci<x-1>::value + fibonacci<x-2>::value
    };
};
template<>
struct fibonacci<0>{
    enum{
        value = 0
    };
};
template<>
struct fibonacci<1>{
    enum{
        value = 1
    };
};

/*
 * Sample use:
 * int fib_val = Fibonacci<0>::value;
 */

-module(factorial).
-export([factorial/1]).

% factorial using pattern matching and tail recursion
factorial(0) -> 1;
factorial(N) -> N * factorial(N-1).



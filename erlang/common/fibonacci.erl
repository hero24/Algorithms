-module(fibonacci).
-export([fibonacci/1]).

% fibonacci sequence using pattern matching.
fibonacci(0) -> 1;
fibonacci(1) -> 1;
fibonacci(N) -> fibonacci(N-1) + fibonacci(N-2).

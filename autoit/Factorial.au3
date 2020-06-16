#comments-start
Factorial implemented using recursive and iterative
approach.
#comments-end

Func FactorialRecursive($iX)
   If $iX = 0 Then
	  Return 1
   EndIF
Return $iX * FactorialRecursive($iX-1)
EndFunc

Func FactorialIterative($ix)
   Local $iResult = 1
   While $ix > 0
	  $iResult *= $ix
	  $ix -= 1
   WEnd
   Return $iResult
EndFunc

#comments-start
In place implementation of QuickSort algorithm.
#comments-end

Func swap(ByRef $arr, $pos_a, $pos_b)
   Local $temp = $arr[$pos_a]
   $arr[$pos_a] = $arr[$pos_b]
   $arr[$pos_b] = $temp
EndFunc

Func QuickSort(ByRef $arr, $left=0, $right=UBound($arr))
   If $left < $right Then
	  Local $m = $left
	  For $i = $left+1 To $right-1
		 If $arr[$i] < $arr[$left] Then
			$m += 1
			swap($arr, $m, $i)
		 EndIf
	  Next
	  swap($arr, $left, $m)
	  QuickSort($arr, $left, $m-1)
	  QuickSort($arr, $m+1, $right)
   EndIf
EndFunc
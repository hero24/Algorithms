#cs
Inplace implementation of HeapSort
#ce
Func Recover(ByRef $arr, $k, $n)
   Local $i, $j
   $i = $arr[$k-1]
   While $k <= $n/2
	  $j = 2 * $k
	  If $j < $n And $arr[$j-1]<$arr[$j] Then
		 $j += 1
	  EndIf
	  If $i >= $arr[$j-1] Then
		 ExitLoop
	  EndIf
	  $arr[$k-1] = $arr[$j-1]
	  $k = $j
   WEnd
   $arr[$k-1] = $i
EndFunc

Func HeapSort(ByRef $arr)
   Local $swap
   Local $n = UBound($arr)
   For $k = $n/2 To 0 Step -1
	  Recover($arr, $k,  $n)
   Next
   Do
	  $swap = $arr[0]
	  $arr[0] = $arr[$n-1]
	  $arr[$n-1] = $swap
	  $n -= 1
	  Recover($arr, 1, $n)
   Until $n <= 0
EndFunc
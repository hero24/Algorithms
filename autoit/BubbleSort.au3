#comments-start
In place implementation of BubbleSort
#comments-end

Func BubbleSort(ByRef $arr)
   Local $arr_sz = UBound($arr)-1
   For $i = 1 To $arr_sz
	  For $j = $arr_sz To $i Step -1
		 If $arr[$j] < $arr[$j-1] Then
			Local $tmp = $arr[$j-1]
			$arr[$j-1] = $arr[$j]
			$arr[$j] = $tmp
		 EndIf
	  Next
   Next
   Return $arr
EndFunc

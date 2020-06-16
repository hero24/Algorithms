#comments-start
InsertionSort implementation.
#comments-end

Func InsertionSort($arr)
   For $i = 0 To UBound($arr)-1
	  Local $j = $i
	  Local $temp = $arr[$j]
	  While ($j > 0) And ($arr[$j-1]>$temp)
		 $arr[$j] = $arr[$j-1]
		 $j -= 1
	  WEnd
	  $arr[$j] = $temp
   Next
   Return $arr
EndFunc

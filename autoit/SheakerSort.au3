#comments-start
ShakerSort implementation (bi-directional BubbleSort)
#comments-end

Func SheakerSort($arr)
   Local $left = 1
   Local $right = UBound($arr) - 1
   Local $k = UBound($arr) - 1
   Do
	  For $i = $right To $left Step -1
		 If $arr[$i-1] > $arr[$i] Then
			Local $temp = $arr[$i]
			$arr[$i] = $arr[$i-1]
			$arr[$i-1] = $temp
			$k = $i
		 EndIf
		 $left = $k + 1
	  Next
	  For $i = $left To $right Step 1
		 If $arr[$i-1] > $arr[$i] Then
			Local $temp = $arr[$i]
			$arr[$i] = $arr[$i-1]
			$arr[$i-1] = $temp
			$k = $i
		 EndIf
		 $right = $k - 1
	  Next
   Until $left > $right
   Return $arr
EndFunc

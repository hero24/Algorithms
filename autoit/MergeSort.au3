Local $arr[5] = [1]
$arr = MergeSort($arr)
For $i = 0 To UBound($arr)-1
   ConsoleWrite($arr[$i])
Next

Func MergeSort($arr)
   If UBound($arr) > 1 Then
	  Local $mid = UBound($arr)/2
	  Local $lowerarr[$mid+1], $higherarr[$mid+1]
	  For $i = 0 To $mid
		 $lowerarr[$i] = $arr[$i]
		 $higherarr[$i] = $arr[$i+$mid]
	  Next
	  $lowerarr = MergeSort($arr)
	  $higherarr = MergeSort($arr)
   Local $i = 0, $j = 0
   For $k = 0 To UBound($arr)-1
	  If $i == UBound($lowerarr) Then
		 $arr[$k] = $higherarr[$j]
		 $j+= 1
		 ContinueLoop
	  EndIf
	  If $j == UBound($higherarr) Then
		 $arr[$k] = $lowerarr[$i]
		 $i += 1
		 ContinueLoop
	  EndIf
	  If $lowerarr[$i] < $higherarr[$j] Then
		 $arr[$k] = $lowerarr[$i]
		 $i += 1
	  Else
		 $arr[$k] = $higherarr[$j]
		 $j += 1
	  EndIf
   Next
   EndIf
   Return $arr
EndFunc

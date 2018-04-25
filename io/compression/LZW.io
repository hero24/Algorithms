/*
  "Learning never exhausts the mind." ~ Leonardo da Vinci
*/
/*
	Implementation of LZW compression algorithm in io.
	Throws LZWBadCompressionError if there is an error in decompress
	LZW compress - compresses a string using LZW algorithm
	LZW decompress - decompresses previously compressed string.
*/
LZWBadCompressionError := Error clone

LZW := Object clone
LZW compress := method(uncomp,
    dict_size := 255
    dict := Map clone
    for(i, 0, dict_size, dict atPut(i asCharacter, i))
	dict_size = dict_size + 1
    w := ""
    result := List clone
    for(i,0, uncomp size - 1,
	   c := uncomp at(i) asCharacter
       wc := w .. c
       if(dict hasKey(wc),
          w = wc,
          result append(dict at(w))
          dict atPut(wc, dict_size)
		  dict_size = dict_size + 1
          w = c
       )
    )
    if(w != "",result append(dict at(w)))
    return result
)
LZW decompress := method(comprsd,
    dict_size := 255
	dict := Map clone
    for(i, 0, dict_size, dict atPut(i asCharacter, i asCharacter))
	dict_size = dict_size + 1
	w := comprsd at(0) asCharacter
	result := w
	for(i, 1, comprsd size-1,
		i_at := comprsd at(i)
	    if(dict hasKey(i_at asCharacter)) then(
		    entry := dict at(i_at asCharacter)
		) elseif(i_at == dict_size) then(
		    entry := w .. (w at(0) asCharacter)
		) else(LZWBadCompressionError raise("Invalid compression"))
		result = result .. entry
		dict atPut(dict_size asCharacter, w .. entry at(0) asCharacter)
		dict_size = dict_size + 1
		w = entry
	)
	return result
)
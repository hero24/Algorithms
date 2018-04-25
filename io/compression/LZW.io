LZW := Object clone
LZW compress := method(uncomp,
    dict_size := 255
    dict := Map clone
    for(i, 0, dict_size,
        dict atPut(i asCharacter, i)
    )
    w := ""
    result := List clone
    for(i,0, uncomp size - 1,
       wc := w .. uncomp at(i) asCharacter
       if(dict hasKey(wc),
          w = wc,
          result append(dict at(w))
          dict_size = dict_size + 1
          dict atPut(wc, dict_size)
          w = uncomp at(i) asCharacter
       )
    )
    if(w size > 0,
        result append(dict at(w))
    )
    return result
)


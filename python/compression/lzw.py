#!/usr/bin/env python3
# "There is nothing premanent except change" ~ Heraclitus

class BadCompressionError(Exception):
    pass

class LZW:
    @staticmethod
    def compress(uncompressed):
        dict_size = 256
        hashmap = {chr(i): i for i in range(dict_size)}
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in hashmap:
                w = wc
            else:
                result.append(hashmap[w])
                hashmap[wc] = dict_size
                dict_size += 1
                w = c
        if w:
            result.append(hashmap[w])
        return result

    def decompress(compressed):
        dict_size = 256
        hashmap = {i:chr(i) for i in range(dict_size+1)}
        w = chr(compressed[0])
        result = w
        for i in compressed[1:]:
            if i in hashmap:
                entry = hashmap[i]
            elif i == dict_size:
               entry = w + w[0]
            else:
                raise BadCompressionError("Corrupted data")
            result += entry
            hashmap[dict_size] = w + entry[0]
            dict_size += 1
            w = entry
        return result

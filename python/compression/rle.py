"""
There is no compression algorithm for experience.
~ Andy Jassy
"""

class RunLengthEncoding:
    """
    Run lenght encoding algorithm implementation
    """
    @staticmethod
    def encode(value):
        """
        Encode value using RLE algorithm
        """
        encoded = []
        count = 0
        prev = None
        for v in value:
            if prev is None:
                prev = v
            if v == prev:
                count += 1
                continue
            if count > 1:
                encoded.append((prev, count))
            else:
                encoded.append((prev))
            prev = v
            count = 1
        encoded.append((prev, count))
        return encoded

    @staticmethod
    def decode(value):
        """
        decode value using RLE algorithm
        """
        result = ""
        for v in value:
            if len(v) == 1:
                result += v
                continue
            v, count = v
            result += count * v
        return result
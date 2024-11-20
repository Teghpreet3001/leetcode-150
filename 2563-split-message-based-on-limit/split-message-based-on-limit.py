class Solution:

    # Case 1 (10 <= parts < 100): 9 parts with "<K/NN>" suffixes where suffix length is 6 AND (total_parts - 9) parts with "<KK/NN>" suffixes where suffix length is 7.
    # Case 1 (100 <= parts < 1000): 9 parts with "<K/NNN>" suffixes where suffix length is 7 AND 90 with with "<KK/NNN>" suffixes where suffix length is 8 (total_parts - 99) parts with "<KKK/NN>" suffixes where suffix length is 9.

    def getParts(self, message, limit): 
        if limit <= 5:
            return 0 
        message_length = len(message)
        parts = math.ceil(message_length / (limit - 5))

        if 10 <= parts <= 100: 
            if limit > 7: 
                parts = math.ceil((message_length - 9) / (limit - 7))
            else: 
                parts = 0
        if 100 <= parts < 1000: 
            if limit > 9: 
                parts = math.ceil((message_length - 108) / (limit - 9))
            else: 
                parts = 0
        if 1000 <= parts < 10000: 
            if limit > 11: 
                parts = math.ceil((message_length - 1107) / (limit - 11))
            else: 
                parts = 0
        if parts > 10000:
            parts = math.ceil((message_length + 118894) / limit)
            if parts > 10000:
                parts = 0
        return parts

    def splitMessage(self, message: str, limit: int) -> List[str]:
        res = []
        start = 0
        end = 0
        parts = self.getParts(message, limit)
        for i in range(parts): 
            suffix = f"<{i + 1}/{parts}>"
            end = start + limit - len(suffix)
            content = f"{message[start:end]}"
            full_message = content + suffix
            res.append(full_message)
            start = end
        return res


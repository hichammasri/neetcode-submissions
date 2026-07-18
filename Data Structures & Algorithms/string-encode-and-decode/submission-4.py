class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            temp_encoded = '#' + str(len(s)) +'#' + s
            result += temp_encoded
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:
            i  = 1
            s_length = ""
            while i < len(s) -1 and s[i]!='#':
                s_length += s[i]
                i+=1
            cur = s[1+i:1+i+int(s_length)]
            rem = s[1+i+int(s_length):]
            return [cur] + self.decode(rem)
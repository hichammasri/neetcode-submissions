class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) +'#' + s
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        i  = 0
        s_length = ""
        while i < len(s) -1 and s[i]!='#':
            s_length += s[i]
            i+=1

        j = i + 1
        cur = s[j:j+int(s_length)]
        rem = s[j+int(s_length):]

        return [cur] + self.decode(rem)
class Solution:
    def encode(self, strs: list[str]) -> str:
        # Encode each string as "<length>#<string>"
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            # read length prefix
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # extract the string of that length
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

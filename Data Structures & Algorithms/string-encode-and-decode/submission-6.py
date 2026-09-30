# class Solution:

#     def reverse_letter(self, ch):
#         return chr(0 + 127 - ord(ch))

#     def encode(self, strs: List[str]) -> str:
#         # delimiter = ""
#         combined_str = "§".join(strs)
#         print(combined_str)
#         res = ""
#         for val in list(combined_str):
#             o = val
#             if val != "§":
#                 o = self.reverse_letter(val)
            
#             res = res + o
            
#         return res

#     def decode(self, s: str) -> List[str]:
#         # d = s.split(",")
#         words = []
#         for w in s.split("§"):
#             r = ""
#             print
#             for l in list(w):
#                 r = r + self.reverse_letter(l)
            
#             if len(r) > 0:
#                 words.append(r)
    
#         return words


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])

            i = end

        return res
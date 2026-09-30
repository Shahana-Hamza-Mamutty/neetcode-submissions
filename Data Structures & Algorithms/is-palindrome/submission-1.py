class Solution:
    def IsAlphaNumeric(self, l: str) -> bool:
        ascii_val = ord(l)

        return (
            65 <= ascii_val <= 90 or
            97 <= ascii_val <= 122 or
            48 <= ascii_val <= 57
        )


    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        split_s = list(s)

        while start < end:
            print(split_s[start]) 
            print(split_s[end])

            if not self.IsAlphaNumeric(split_s[start]):
                start = start + 1
                continue

            print(end) 
            print(split_s)

            if not self.IsAlphaNumeric(split_s[end]):
                end = end - 1
                continue

            if split_s[start].lower() != split_s[end].lower():
                return False

            start = start + 1
            end = end - 1

        return True


        
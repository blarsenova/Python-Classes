
class SubstringIndex(object):
    def strStr(self, haystack, needle):
        # 1. Define lengths inside the function scope
        n, m = len(haystack), len(needle)

        # 2. Loop through the haystack
        for i in range(n - m + 1):
            # 3. Check if the slice matches the needle
            if haystack[i:i + m] == needle:
                return i

        # 4. If no match is found, return -1
        return -1



if __name__ == "__main__":
    sol = SubstringIndex()
    print(sol.strStr("leetcode", "r"))  # Output: 2
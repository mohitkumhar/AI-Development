class Solution(object):
    def licenseKeyFormatting(self, s, k):
        
        s = s.upper()
        s = s[::-1]
        s = s.replace("-", "")
        result = []
        print(s)
        for i in range(0, len(s), k):
            result.append(s[i:i+k])
            
            print(result)
        print(result[::-1])

a1 = Solution()
a1.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)

        
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator*denominator<0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        q, r = divmod(numerator, denominator)
        if r == 0:
            return sign+str(q)
        
        d = {r: 1}
        ans = [sign + str(q) + '.']
        while r != 0:
            q, r = divmod(r*10, denominator)
            ans.append(str(q))
            if r in d:
                p = d[r]
                return ''.join(ans[:p]) + '(' + ''.join(ans[p:]) + ')'
            d[r] = len(ans)
        return ''.join(ans)

if __name__ == "__main__":
    obj = Solution()
    print(obj.fractionToDecimal(3, 14))
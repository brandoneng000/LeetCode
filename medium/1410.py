class Solution:
    def entityParser(self, text: str) -> str:
        special_char = { "&gt;": '>', "&lt;": '<', "&quot;": '"', "&apos;": "'", "&frasl;": '/', "&amp;": '&' }

        for code, c in special_char.items():
            text = text.replace(code, c)
        
        return text

    # def entityParser(self, text: str) -> str:
    #     n = len(text)
    #     special_char_size = [4, 5, 6, 7]
    #     special_char = { "&amp;": '&', "&gt;": '>', "&lt;": '<', "&quot;": '"', "&apos;": "'", "&frasl;": '/' }
    #     index = 0
    #     res = []

    #     while index < n:
    #         if text[index] != '&':
    #             res.append(text[index])
    #             index += 1
    #         else:
    #             adjust = 1
    #             for size in special_char_size:
    #                 cur = text[index: index + size]
    #                 if cur in special_char:
    #                     res.append(special_char[cur])
    #                     adjust = size
    #                     break
    #             if adjust == 1:
    #                 res.append(text[index])
    #             index += adjust
        
    #     return "".join(res)

        
def main():
    sol = Solution()
    print(sol.entityParser("&amp;gt;"))
    print(sol.entityParser("&amp; is an HTML entity but &ambassador; is not."))
    print(sol.entityParser("and I quote: &quot;...&quot;"))

if __name__ == '__main__':
    main()
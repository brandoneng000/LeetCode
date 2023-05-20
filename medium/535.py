import string
import random

class Codec:
    def __init__(self) -> None:
        self.database = {}
        self.size = 6

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        end_URL = ''.join(random.choices(chars, k=self.size))
        while end_URL in self.database:
            end_URL = ''.join(random.choices(chars, k=self.size))
        self.database[end_URL] = longUrl
        return f'http://tinyurl.com/{end_URL}'
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        end_url = shortUrl[-6:]
        if end_url in self.database:
            return self.database[end_url]
        return 'http://tinyurl.com/'
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
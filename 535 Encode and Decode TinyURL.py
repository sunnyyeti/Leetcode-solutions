# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
import string
import random
class Codec:

    encodes = {}
    decodes = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.encodes:
            return encodes[longUrl]
        
        short = "".join(random.choice(string.ascii_letters+string.octdigits)  for _ in range(6))
        while short in self.decodes:
             short = "".join(random.choice(string.ascii_letters+string.octdigits)  for _ in range(6))
        self.encodes[longUrl] = f"http://tinyurl.com/{short}"
        self.decodes[short] = longUrl
        return self.encodes[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodes[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
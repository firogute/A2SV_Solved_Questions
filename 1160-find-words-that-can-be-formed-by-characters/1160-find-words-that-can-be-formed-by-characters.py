class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0

        for word in words:
            freq = {x: chars.count(x) for x in chars}
            print(freq)
            for c in word:
                 if c in chars and freq[c] > 0:
                    freq[c] -= 1
                 else:
                    break
            else:
                sum += len(word)
                print(word, sum)

        return sum
            
        
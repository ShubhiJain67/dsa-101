class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        wordLens = list(set(len(word) for word in words))
        wordLens.sort()
        
        # return self.find(s, words, wordLens, 0)

        # memo = [None]*(len(s)+1)
        # return self.findMemo(s, words, wordLens, 0, memo)

        return self.findDP(s, words, wordLens)
        
    def find(self, s, words, wordLens, i):
        sentences = []
        if i == len(s):
            sentences = [""]
        else:
            for wordLen in wordLens:
                if i + wordLen > len(s):
                    break
                if s[i:i+wordLen] in words:
                    otherSentences = self.find(s, words, wordLens, i+wordLen)
                    for sentence in otherSentences:
                        if sentence == "":
                            sentences.append(s[i:i+wordLen])
                        else:
                            sentences.append(f"{s[i:i+wordLen]} {sentence}")
        return sentences

    def findMemo(self, s, words, wordLens, i, memo):
        sentences = []
        if memo[i] is not None:
            return memo[i]
        if i == len(s):
            sentences = [""]
        else:
            for wordLen in wordLens:
                if i + wordLen > len(s):
                    break
                if s[i:i+wordLen] in words:
                    otherSentences = self.find(s, words, wordLens, i+wordLen)
                    for sentence in otherSentences:
                        if sentence == "":
                            sentences.append(s[i:i+wordLen])
                        else:
                            sentences.append(f"{s[i:i+wordLen]} {sentence}")
        memo[i] = sentences
        return memo[i]

    def findDP(self, s, words, wordLens):
        memo = [None]*(len(s)+1)
        for i in range(len(s), -1, -1):
            sentences = []
            if memo[i] is not None:
                return memo[i]
            if i == len(s):
                sentences = [""]
            else:
                for wordLen in wordLens:
                    if i + wordLen > len(s):
                        break
                    if s[i:i+wordLen] in words:
                        otherSentences = memo[i+wordLen]
                        for sentence in otherSentences:
                            if sentence == "":
                                sentences.append(s[i:i+wordLen])
                            else:
                                sentences.append(f"{s[i:i+wordLen]} {sentence}")
            memo[i] = sentences
        return memo[0]

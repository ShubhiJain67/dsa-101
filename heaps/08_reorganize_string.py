class Solution:
    def reorganizeString(self, s: str) -> str:
        store = {}
        for ch in s:
            if ch not in store:
                store[ch] = 0
            store[ch] += 1
        if max(store.values()) > (len(s) + 1) // 2:
            return ""
        
        heap = []
        for ch in store:
            heap.append([-store[ch], ch])

        heapq.heapify(heap)
        index = 0
        newStr = [None]*len(s)
        while heap:
            freq, ch = heapq.heappop(heap)
            freq *= -1
            while freq > 0:
                if index >= len(s):
                    index = 1

                newStr[index] = ch
                index += 2
                freq -= 1

        return "".join(newStr)

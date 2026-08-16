from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return self.getMinDist(beginWord, endWord, wordList)
        return self.getMinDistV2(beginWord, endWord, wordList)

    def getMinDistV2(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for neighbour in graph[pattern]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, level + 1))
                graph[pattern] = []

        return 0
    
    def getMinDist(self, beginWord, endWord, wordList):
        if len(endWord) != len(beginWord):
            return 0
        wordList.append(beginWord)
        src = len(wordList) - 1
        dst = None
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                dst = i
        if dst is None:
            return 0
        adjList = self.getAdjList(wordList, len(beginWord))
        visited = [False]*len(adjList)
        que = deque([[src, 1]])
        while que:
            node, dist = que.popleft()
            if visited[node]:
                continue
            visited[node] = True
            if node == dst:
                return dist
            for neigh in adjList[node]:
                if not visited[neigh]:
                    que.append([neigh, dist+1])
        return 0

    def getAdjList(self, wordList, wordLen):
        adjList = [[] for _ in range(len(wordList))]
        for i in range(len(wordList)):
            if len(wordList[i]) != wordLen:
                continue
            for j in range(i+1, len(wordList)):
                dist = self.getDist(wordList[i], wordList[j])
                if dist == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        return adjList

    def getDist(self, word1, word2):
        dist = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dist+=1
            if dist > 1:
                break
        return dist

from collections import deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        mpp = {}
        ans = []
        b = beginWord

        def dfs(word, seq):
            if word == b:
                seq.reverse()
                ans.append(seq[:])
                seq.reverse()
                return

            sz = len(word)
            steps = mpp[word]

            for i in range(sz):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in mpp and mpp[new_word] + 1 == steps:
                        seq.append(new_word)
                        dfs(new_word, seq)
                        seq.pop()

                word = word[:i] + original + word[i+1:]

        st = set(wordList)
        q = deque()
        b = beginWord
        q.append([beginWord])

        mpp[beginWord] = 1
        sz = len(beginWord)
        if beginWord in st:
            st.remove(beginWord)

        while q:
            word = q.popleft()
            steps = mpp[word[-1]]
            
            if word[-1] == endWord:
                break

            for i in range(sz):
                original = word[-1][i]

                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[-1][:i] + ch + word[-1][i+1:]
                    if new_word in st:
                        q.append(word + [new_word])
                        st.remove(new_word)
                        mpp[new_word] = steps + 1

                word[-1] = word[-1][:i] + original + word[-1][i+1:]

        if endWord in mpp:
            seq = [endWord]
            dfs(endWord, seq)

        return ans

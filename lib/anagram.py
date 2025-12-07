# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # normalize to lowercase

    def match(self, candidates):
        results = []
        sorted_word = sorted(self.word)
        for candidate in candidates:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word and sorted(candidate_lower) == sorted_word:
                results.append(candidate)
        return results

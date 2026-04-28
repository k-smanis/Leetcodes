class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Group Words
        word_identities = dict()

        for word in strs:
            word_sorted_as_list = sorted(word)
            word_sorted = "".join(word_sorted_as_list)

            if word_sorted in word_identities:
                word_identities[word_sorted].append(word)
            else:
                word_identities[word_sorted] = [word]
        
        #Step 2: Create Output List
        output: List[List[str]] = list()

        for word_identity, words in word_identities.items():
            output.append(words)
        
        #Step 3: Return
        return output

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #my code
        morse_table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabet_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']
        result = set()
        for word in words:
            temp_str = ""
            for i in word:
                temp_str += morse_table[alphabet_table.index(i)]
            result.add(temp_str)
        return len(result)
        #best code
        transformations = set()

        for word in words:
            transformation = ""
            for letter in word:
                transformation += morse[ord(letter) - 97]
            if transformation not in transformations:
                transformations.add(transformation)

        return len(transformations)

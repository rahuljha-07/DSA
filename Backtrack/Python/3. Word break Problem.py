# Function to perform the word break using backtracking
def solve(str, currentSentence, dictionary, results):
    # Base case: if the string size is zero, add the constructed sentence to the results and
    # return
    if len(str) == 0:
        results.append(currentSentence)
        return
    # Iterate through the string to find all possible prefixes
    for i in range(len(str)):
        # Extract the prefix
        prefix = str[:i + 1]
        if prefix in dictionary:
            # Get the remaining part of the string
            remaining = str[i + 1:]
            # Recur with the remaining string and add the prefix to the current sentence
            solve(remaining, currentSentence + prefix + ("" if not remaining else " "),
                  dictionary, results)


# Wrapper function to initiate the word break
def wordBreak(str, dictionary):
    # list to store all valid sentences
    results = []
    solve(str, "", dictionary, results)
    return results


def main():
    inputString = "catsanddog"
    dictionary = {"cat", "cats", "and", "sand", "dog"}
    results = wordBreak(inputString, dictionary)
    print("All possible word breaks:")
    for sentence in results:
        print(sentence)


if __name__ == "__main__":
    main()


'''
Let n be input length and P total output characters.
Time: O(n^2*2^n + P) conservative worst-case bound: without memoization,
try exponentially many splits; each call creates/hashes prefixes and
copies remaining text/sentences, costing up to O(n^2).
Space: O(n^2) auxiliary retained suffixes/sentences across O(n) calls,
plus O(P) output. Dictionary storage is supplied; hash lookups average O(1)
after the O(prefix length) hash cost.
'''

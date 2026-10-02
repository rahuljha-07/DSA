def solve(str, currentSentence, dictionary, results):
    if len(str) == 0:
        results.append(currentSentence)
        return
    for i in range(len(str)):
        prefix = str[:i + 1]
        if prefix in dictionary:
            remaining = str[i + 1:]
            solve(remaining, currentSentence + prefix + ("" if not remaining else " "),
                  dictionary, results)


def wordBreak(str, dictionary):
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

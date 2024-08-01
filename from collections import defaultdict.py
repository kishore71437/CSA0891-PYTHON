from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_map = defaultdict(list)
for s in strs:
    sorted_str = ''.join(sorted(s))
    anagram_map[sorted_str].append(s)
result = list(anagram_map.values())
print(result)
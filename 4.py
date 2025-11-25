n = int(input())  
words = input().split()
anagram_groups = {}

for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_groups:
        anagram_groups[sorted_word].append(word)
    else:
        anagram_groups[sorted_word] = [word]

for group in anagram_groups.values():
    print(f"Группа: {', '.join(group)}")

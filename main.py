word_count = {}

with open('wc.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            word = word.lower()  # 可选：统一为小写
            word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
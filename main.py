with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

word_count = {}

for letter in file_contents:
    if not letter.isalpha():
        continue
    letter = letter.lower()
    if letter not in word_count:
        word_count[letter] = 0
    word_count[letter] += 1

word_count_list = []
for count in word_count:
    word_count_list.append({"letter": count,
                            "count": word_count[count]})
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words were found in the document")
word_count_list.sort(key = lambda letter_counter: -letter_counter["count"])
for letter_count in word_count_list:
    print(f"The \'{letter_count['letter']}\' character was found {letter_count['count']} times")

print("--- End report ---")

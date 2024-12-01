file_path = 'C:/Users/이강민/doodle/PythonPractice/BestPythonBook/context.txt'
def analyze_sentence(sentence):
    sentence = sentence.strip()
    print(sentence)
    words = sentence.rstrip('.').split()
    quoted_words = [f"'{word}'" for word in words]
    print(f"[{', '.join(quoted_words)}]")

    for word in words:
        print(word)
    print()


with open(file_path, 'r') as file:
    sentences = file.readlines()


for sentence in sentences:
    if sentence.strip():
        analyze_sentence(sentence)


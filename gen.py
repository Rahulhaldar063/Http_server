import os
import random
import string

# Create a directory to store the text files
output_directory = "random_text_files"
os.makedirs(output_directory, exist_ok=True)

# Number of files to create
num_files = 30

# Number of paragraphs in each file
num_paragraphs = 10

# Number of sentences in each paragraph
sentences_per_paragraph = 20

# Words per sentence
words_per_sentence = 100

for i in range(1, num_files + 1):
    paragraphs = []
    for _ in range(num_paragraphs):
        sentences = []
        for _ in range(sentences_per_paragraph):
            sentence = ' '.join(
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
                for _ in range(words_per_sentence)
            )
            sentences.append(sentence.capitalize() + '.')
        paragraphs.append(' '.join(sentences))

    # Create a file with a unique name in the specified directory
    file_name = os.path.join(output_directory, f"{i}.txt")

    # Write the random text to the file
    with open(file_name, 'w') as file:
        file.write('\n'.join(paragraphs))

print(f"{num_files} text files created in the '{output_directory}' directory.")

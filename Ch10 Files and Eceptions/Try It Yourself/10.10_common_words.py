############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


filenames = ['/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/Far from the Madding Crowd by Thomas Hardy.txt',
             '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/The sleepers awakes by H. G. Wells.txt']


def count_common_word(filename, word):
    """Count how many times word appears in the text."""

    try:
        with open(filename, encoding='utf-8')as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


count_common_word(filenames[0], 'the ')


############################################
print('\n')  # Spaces for convention only!
############################################

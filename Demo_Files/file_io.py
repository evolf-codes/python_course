from pathlib import Path
data_folder = Path("/Users/evolfson/Desktop/Git/Python_Course/Demo_Files/")
story = data_folder / "story.txt"
story2 = data_folder / "story2.txt"

# copy a file
def copy(s1, s2):
    with open(s1) as story:
        story_content = story.read()
    with open(s2, 'w') as story2:
        story2.write(story_content)

# reverse a file
def copy_and_reverse(s1, s2):
    with open(s1) as story:
        story_content = story.read()
    with open(s2, 'w') as story2:
        story2.write(story_content[::-1])

copy(story,story2)
copy_and_reverse(story,story2)

# get statistics on a file
def statistics(s1):


    with open(s1) as story:
        story_content = story.readlines()
        lines = len(story_content)

    with open(s1) as story:
        story_content = story.read()
        word_list = story_content.split()
        number_of_words = len(word_list)

    with open(s1) as story:
        story_content = story.read()
        char = len(story_content)

    stats = {'lines':lines, 'words':number_of_words, 'characters':char}
    return stats



print(statistics(story))


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
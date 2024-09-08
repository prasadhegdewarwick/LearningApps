import os

def load_journal(name):
    """
    This Method creates and Loads New Journal
    :param name: This bas name of journal to load
    :return: A New Journal data structure populated with file data
    """

    data = []

    filename = get_full_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save_journal(name, journal_data):
    filename = get_full_path(name)

    print(f"....Saving Journal to {filename}")
    # filename = './journals/' + name + '.jrl'

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def add_entry(text, journal_data):
    journal_data.append(text)


def get_full_path(name):
    return os.path.abspath(os.path.join('./journals/', name + '.jrl'))

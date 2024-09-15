import os.path
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def get_folder_from_user():
    folder_name = input("What folder do you want to search? ")
    if not folder_name or not folder_name.strip():
        return None
    if not os.path.isdir(folder_name):
        return None


    return os.path.abspath(folder_name)


def search_file(file_name, text):

    try:
        with open(file_name, 'r', encoding='utf-8') as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if line.lower().find(text) >= 0:
                    m = SearchResult(line=line_num, file=file_name, text=line)

                    yield m

    except UnicodeDecodeError:
        print("NOTICE: Binary file {} skipped.".format(file_name))


def get_search_text():
    search_text = input("Please Enter the Text you want to Search ")
    return search_text


def print_result(matches):
    print()
    for ele in matches:
        print(f" Text Found in {ele[0]} file at line {ele[1]} and text is as below")
        print(f"{ele[2]}")
        print()


def search_folder(folder, search_text):
    items = os.listdir(folder)
    for item in items:
        full_path = os.path.join(folder, item)

        if os.path.isdir(full_path):

            yield from search_folder(full_path, search_text)
        else:

            yield from search_file(full_path, search_text.lower())



def main():
    print_header()
    folder = get_folder_from_user()

    if not folder:
        print(" We cannot Search that Folder")

    search_text = get_search_text()

    if not search_text:
        print("We cannot Search for nothing")

    result = search_folder(folder, search_text)

    print_result(result)





def print_header():
    print("------------------------------------------------")
    print("            FILE SEARCH APP                     ")
    print("------------------------------------------------")




if __name__ == '__main__':
    main()

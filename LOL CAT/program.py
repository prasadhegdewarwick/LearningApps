# Print Header
# Get or Create Output Folder
# download cats
# display Cats
import filepath
import cat_service


def print_header():
    print("------------------------------------")
    print("         CAT FACTORY                 ")
    print("------------------------------------")


if __name__ == '__main__':
    print_header()
    full_path = filepath.get_file_path()
    print(f"Found or Created Folder at {full_path}")
    cat_service.get_cat(full_path)
    cat_service.open_images(full_path)

import journal
def print_header():
    print("---------------------------------")
    print("Welcome To Journal App")
    print("---------------------------------")
    print()


def run_event_loop():
    print('What do you Want to Do with Your Journal')
    cmd = 'EMPTY'
    journal_name = "default"
    journal_data = journal.load_journal(journal_name)
    while cmd != 'x' and cmd:
        cmd = input("[L]ist Entries, [A]dd Entries, E[x]it: ")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f"Sorry, We do not recognize {cmd} command")
    print("Good Bye")
    journal.save_journal(journal_name, journal_data)


def list_entries(data):
    if data:
        print("Your Journal Entries Are")
    else:
        print("Your Journal Entry is Empty")
    for idx, entry in enumerate(data[::-1]):
        print(f"{idx + 1}. {entry}")



def add_entry(data):
    entry = input("Please Enter your Entry, <enter> to Exit: ")
    journal.add_entry(entry, data)
    # data.append(entry)




def main():
    print_header()
    run_event_loop()

main()

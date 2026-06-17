# Project Name: Banevich_Python
import sys


def process_input(user_input: str) -> None:
    original_text = user_input.strip()
    if not original_text:
        return

    cleaned_input = original_text.replace(',', ' ').replace('[', ' ').replace(']', ' ')
    tokens = cleaned_input.split()

    # numeric array
    if len(tokens) > 1:
        try:

            numeric_array = [float(x) for x in tokens]

            multiples = [x for x in numeric_array if x % 3 == 0]

            result = [int(x) if x.is_integer() else x for x in multiples]

            if result:
                print(*result)
            return
        except ValueError:

            pass

    # one number
    try:
        number = float(original_text)
        if number > 7:
            print("Hello")

        return
    except ValueError:
        pass

    # name
    if original_text == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def main() -> None:

    print("--- QA Automation Task ---")
    print("Enter a number, a name, or a numeric array (space-separated). Type 'exit' to quit.")

    while True:
        user_data = input("> ")
        if user_data.strip().lower() == 'exit':
            break
        process_input(user_data)


if __name__ == "__main__":
    main()
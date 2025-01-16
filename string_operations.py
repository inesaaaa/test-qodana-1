# Function with improper exception handling
def get_char_at_index(string, index):
    try:
        return string[index]
    except:  # Bare except; does not specify an exception type
        print("An error occurred")

# Function with redundant logic
def check_string_contains_hello(string):
    if "hello" in string:
        return True
    elif "hello" not in string:  # Redundant elif
        return False


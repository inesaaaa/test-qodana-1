# Missing imports
def read_file(filename):
    with open(filename, 'r') as file:  # NameError: open() might not work if not imported
        return file.read()

# Improper resource management
def write_to_file(filename, content):
    file = open(filename, 'w')  # File not properly closed
    file.write(content)


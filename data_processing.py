# Function with missing type hints and hardcoded values
def process_data(data):
    threshold = 100  # Hardcoded value
    if data > threshold:
        print("Data is too large")
    return data * 2

# Function with unreachable code
def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)
    print("This will never run")  # Unreachable


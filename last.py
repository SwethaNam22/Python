def fib_generator():
    a, b = 0, 1
    generated_numbers = []
    
    def next_fib():
        nonlocal a, b
        result = a
        generated_numbers.append(result)
        a, b = b, a + b
        return result
    
    def accumulate_sum():
        return sum(generated_numbers)
    
    return next_fib, accumulate_sum

def create_even_generator():
    current = 0
    generated_numbers = []
    
    def next_even():
        nonlocal current
        result = current
        generated_numbers.append(result)
        current += 2
        return result
    
    def accumulate_sum():
        return sum(generated_numbers)
    
    return next_even, accumulate_sum

def interact_with_generator(generator, accumulate_function, max_calls):
    call_count = 0

    while call_count < max_calls:
        input("Press Enter to get the next number...")
        print(generator())
        call_count += 1

    # Print accumulated sum after max_calls
    print("Accumulated sum:", accumulate_function())

def main():
    generator_type = input("Enter the type of generator (Fibonacci/Even): ").strip().lower()

    if generator_type == "fibonacci":
        next_number, accumulate_sum = fib_generator()
    elif generator_type == "even":
        next_number, accumulate_sum = create_even_generator()
    else:
        print("Invalid input. Please enter 'Fibonacci' or 'Even'.")
        return

    interact_with_generator(next_number, accumulate_sum, 4)


main()

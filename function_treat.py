data_1d = []
data_2d = []
dataset_summary = {}


def input_data():
    global data_1d, data_2d

    array_type = int(input("Enter array type 1D / 2D (Enter only 1/2): "))
    if array_type == 1:
        size = int(input("Enter Size of Array : "))
        data_1d = list(
            map(int, input(f"Enter {size} elements separated by spaces: ").split())
        )[:size]
        print("1D Data successfully saved!")

    elif array_type == 2:
        size = int(input("Enter Size of Array (Rows): "))
        data_2d = []
        for i in range(size):
            row = list(
                map(int, input(f"Enter Elements {i+1} Row (ex.1 2 3) : ").split())
            )
            data_2d.append(row)
        print("2D Data successfully saved!")


def choose_dataset():
    
    if len(data_1d) > 0 and len(data_2d) > 0:
        ch = input("Both Array are avalaible ,Choise Array (1: 1D, 2: 2D): ").strip()
        return "1D" if ch == "1" else "2D"
    elif len(data_1d) > 0:
        return "1D"
    elif len(data_2d) > 0:
        return "2D"
    return None


def display_kwargs_summary(**kwargs):
    """Displays dataset characteristics using **kwargs."""
    print("\n--- Summary Characteristics (**kwargs) ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def data_summary():
    """Displays the total, minimum, maximum, sum, and average of the data."""
    global dataset_summary
    print("\n[DOC]:", data_summary.__doc__)

    selected = choose_dataset()
    if not selected:
        print("No data available. Please input data first.")
        return

    data_use = []
    if selected == "1D":
        data_use = data_1d
        print("Operating on 1D Data:", data_1d)
    else:
        print("Operating on 2D Grid:")
        for row in data_2d:
            print(row)
            for item in row:
                data_use.append(item)

    print("\n--- Summary Statistics ---")
    print("Total count:", len(data_use))
    print("Minimum value:", min(data_use))
    print("Maximum value:", max(data_use))
    print("Sum total:", sum(data_use))
    avg_val = round(sum(data_use) / len(data_use), 2)
    print("Average value:", avg_val)

    dataset_summary = {
        "Dataset_Type": selected,
        "Total_Elements": len(data_use),
        "Overall_Mean": avg_val,
        "Min_Value": min(data_use),
        "Max_Value": max(data_use),
    }
    display_kwargs_summary(**dataset_summary)


def factorial(num):
    """Finds the factorial of a number using recursion."""
    if num < 0:
        return "Invalid number"
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


def show_values_args(*args):
    """Displays values using *args."""
    print("Values displayed using *args:", list(args))


def filter_data_threshold():
    """Filters data with threshold and transforms using map() and lambda."""
    print("\n[DOC]:", filter_data_threshold.__doc__)

    selected = choose_dataset()
    if not selected:
        print("No data available to filter.")
        return

    data_use = []
    if selected == "1D":
        data_use = data_1d
    else:
        for row in data_2d:
            for item in row:
                data_use.append(item)

    i = int(input("Enter threshold value: "))
    filtered_list = list(filter(lambda x: x >= i, data_use))

    print(f"Results (values >= {i}):", filtered_list)

    if filtered_list:
        show_values_args(*filtered_list)

    transformed_list = list(map(lambda x: x * 2, filtered_list))
    print("Transformed data (each value multiplied by 2):", transformed_list)


def sort_data():
    """Sorts the data using sort() for 1D and sorted() for 2D."""
    print("\n[DOC]:", sort_data.__doc__)

    selected = choose_dataset()
    if not selected:
        print("No data available to sort.")
        return

    if selected == "1D":
        order = input("Select 1. Ascending and 2. Descending order: ")
        temp_data = data_1d.copy()
        if order == "1":
            temp_data.sort()
            print("Sorted Ascending order (using sort()):", temp_data)
        elif order == "2":
            temp_data.sort(reverse=True)
            print("Sorted Descending order (using sort()):", temp_data)
        else:
            print("Invalid input.")

    elif selected == "2D":
        print("Sorting each row using sorted() (returns new sorted list):")
        for row in data_2d:
            print(sorted(row))


def statistics():
    """Displays dataset statistics about the data and returns multiple values."""
    print("\n[DOC]:", statistics.__doc__)

    selected = choose_dataset()
    if not selected:
        print("No data available for statistics.")
        return

    flat_data = []
    if selected == "1D":
        flat_data = data_1d
    else:
        for row in data_2d:
            for item in row:
                flat_data.append(item)

    def get_statistics(nums):
        val_min = min(nums)
        val_max = max(nums)
        val_sum = sum(nums)
        val_avg = val_sum / len(nums)
        return val_min, val_max, val_sum, val_avg

    minimum, maximum, total, average = get_statistics(flat_data)

    print(f"\n--- Final Statistics for {selected} (Returned Multiple Values) ---")
    print("Min Value:", minimum)
    print("Max Value:", maximum)
    print("Total Sum:", total)
    print("Average  :", round(average, 2))


while True:
    print("\n=== DATA ANALYZER AND TRANSFORMER PROG ===")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter & Transform Data (Lambda, filter, map, *args)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = input("Select an option (1-7): ").strip()

    if choice == "1":
        input_data()
    elif choice == "2":
        data_summary()
    elif choice == "3":
        print("\n[DOC]:", factorial.__doc__)
        n = int(input("Enter number to find factorial: "))
        ans = factorial(n)
        print(f"Result: Factorial of {n} is {ans}")
    elif choice == "4":
        filter_data_threshold()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        statistics()
    elif choice == "7":
        print("Exiting program. Thank you!")
        break
    else:
        print("Wrong input. Choose between 1 and 7.")
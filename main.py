# INSTAGRAM & X: @jacmax_13 || YouTube: Jac Max

while True:
    try:
        print("WELCOME TO JAC MAX's SIMPLE INTEREST CALCULATOR WITH PYTHON 3.12")
        # Prompts the user to select the calculation type
        prompt = int(input("Do you want to calculate Simple Interest, Principal, Rate or Time? POV: 0 for S.I.; 1 for Principal; 2 for Rate; 3 for Time: "))

        # Validates the input to ensure it's one of the allowed options
        if prompt not in [0, 1, 2, 3]:
            raise ValueError("Invalid choice! You must enter 0, 1, 2, or 3.")

        def simple_interest() -> float:
            '''
            Calculates Simple Interest based on user inputs for Principal, Rate, and Time.
            Handles both yearly and monthly time periods.
            '''
            # global int_time
            print("\nINPUT THE REQUIRED VALUES TO CALCULATE SIMPLE INTEREST:")
            p = float(input("Enter the principal(💵) as a whole number or decimal: "))
            r = float(input("Enter the rate(%) as a whole number or decimal: "))
            t_prompt = int(input("Is the time(⏳) in years or months? POV: 0 for years, 1 for months: "))

            # Checks if time is in years or months and handles accordingly using an if-else statement
            if t_prompt == 0:
                int_time = float(input("Enter the time in years: "))
            elif t_prompt == 1:
                int_time = float(input("Enter the time in months: "))
                int_time /= 12  # Convert months to years by dividing the number of months by 12 as 12 months = 1 year and reassigns divided value to variable "int_time"
            else:
                raise ValueError("Invalid choice for time! You must enter 0 for years or 1 for months.")

            # Calculates Simple Interest using the formula Principal*Rate*Time/100 and assigns the result to the variable "si"
            si = (p * r * int_time) / 100
            return si

        def principal() -> float:
            '''
            Calculates Principal based on user inputs for Simple Interest, Rate, and Time.
            Handles both yearly and monthly time periods.
            '''
            global p_time
            print("\nINPUT THE REQUIRED VALUES TO CALCULATE PRINCIPAL:")
            si = float(input("Enter the interest(💹) as a whole number or decimal: "))
            r = float(input("Enter the rate(%) as a whole number or decimal: "))
            t_prompt = int(input("Is the time(⏳) in years or months? POV: 0 for years, 1 for months: "))

            # Also checks if time is in years or months and handles accordingly
            if t_prompt == 0:
                p_time = float(input("Enter the time in years: "))
            elif t_prompt == 1:
                p_time = float(input("Enter the time in months: "))
                p_time /= 12  # Converts months to years
            else:
                raise ValueError("Invalid choice for time! You must enter 0 for years or 1 for months.")

            # Calculates Principal using the formula SI*100/Rate*Time
            p = (si * 100) / (r * p_time)
            return p

        def rate() -> float:
            '''
            Calculates Rate based on user inputs for Simple Interest, Principal, and Time.
            Handles both yearly and monthly time periods.
            '''
            global r_time
            print("\nINPUT THE REQUIRED VALUES TO CALCULATE RATE:")
            si = float(input("Enter the interest(💹) as a whole number or decimal: "))
            p = float(input("Enter the principal(💵) as a whole number or decimal: "))
            t_prompt = int(input("Is the time(⏳) in years or months? POV: 0 for years, 1 for months: "))

            # Also checks if time is in years or months and handles accordingly
            if t_prompt == 0:
                r_time = float(input("Enter the time in years: "))
            elif t_prompt == 1:
                r_time = float(input("Enter the time in months: "))
                r_time /= 12  # Converts months to years
            else:
                raise ValueError("Invalid choice for time! You must enter 0 for years or 1 for months.")

            # Calculates Rate using the formula SI*100/Principal*Time
            r = (si * 100) / (p * r_time)
            return r

        def time() -> float:
            '''
            Calculates Time (in years and months) based on user inputs for Simple Interest, Principal, and Rate.
            '''
            print("\nINPUT THE REQUIRED VALUES TO CALCULATE TIME:")
            si = float(input("Enter the interest(💹) as a whole number or decimal: "))
            p = float(input("Enter the principal(💵) as a whole number or decimal: "))
            r = float(input("Enter the rate(%) as a whole number or decimal: "))

            # Checks for division by zero
            if r == 0:
                raise ZeroDivisionError("Rate cannot be zero, as it would lead to a division by zero.")

            # Calculates Time using the formula SI*100/Principal*Rate
            t = (si * 100) / (p * r)
            t_month = t * 12  # Converts years to months
            return t, t_month

        # Determines which function to call based on user selection
        if prompt == 0:
            print(f"\n<-------------------------------\nThe simple interest(💹) is {simple_interest()}.\n------------------------------->")
        elif prompt == 1:
            print(f"\n<----------------------------\nThe principal(💵) is {principal()}.\n---------------------------->")
        elif prompt == 2:
            print(f"\n<----------------------------\nThe rate(%) is {rate()}%.\n---------------------------->")
        elif prompt == 3:
            print(f"\n<----------------------------------------------------\nThe time(⏳) is {time()} years/months respectively.\n---------------------------------------------------->")

        break  # Exits the loop if everything is successful

    except ValueError as ve:
        # Handle invalid input errors, like entering non-numeric values or invalid options
        print(f"Invalid input! {ve}\n")
    except ZeroDivisionError:
        # Handle math errors like division by zero
        print("Math error! Division by zero occurred, check your inputs.\n")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}\n")

# INSTAGRAM & X: @jacmax_13 || YouTube: Jac Max

# assert simple_interest(120, 5, 2) == 12

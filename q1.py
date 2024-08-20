"""
A day has 86,400 secs (24*60*60). Given a number in the range 1 to 86,400, output the current time
as hours, minutes, and seconds with a 24-hour clock. For example, 70,000 sec is 19 hours, 26 minutes,
and 40 seconds.
"""
def main():
    # Obtain integer from user input
    num = get_int(0, 86400)
    # Convert seconds to hours, minutes and seconds
    time = convert(num)
    # Output formatted time
    print(f"{time["hours"]} hours, {time["minutes"]} minutes and {time["seconds"]} seconds.")


"""
Function which if passed a lower limit (int) and upper limit(int) as arguments,
prompts the user for an integer input which lies between the lower and upper limits.
Prompts user for an input until a valid input is entered.
Returns an integer value.
"""
def get_int(lower_limit, upper_limit):
    try:
        # Try requesting user for an input and converting string input to int
        num = int(input(f"Enter number ({lower_limit} - {upper_limit}): "))
        # Check that integer input falls within range, otherwise raise an error
        if not lower_limit <= num <= upper_limit:
            raise ValueError
    # If any error occurs
    except Exception as e:
        # Display error type to user
        print(f"Invalid integer: {type(e)}")
        # Prompt user for input again
        num = get_int(lower_limit, upper_limit)
    return num


def convert(num):
    hours = num // 3600 # Obtain num of hours
    minutes = (num % 3600) // 60 # Obtain num of minutes
    seconds = num - hours * 3600 - minutes * 60 # Obtain num of seconds
    return {"minutes" : minutes, "hours" : hours, "seconds" : seconds} # Return dictionary containing calculated values
    

if __name__ == "__main__":
    main()
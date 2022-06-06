#!/usr/bin/env python3

# Created by: Hertz
# Created on: jun 5, 2022.
# This program creats a list of marks & display them in a list,calculates
# its average and then displays it to the user.


# This function calculates the average marks of the elements in the list.
def calc_average(list_of_marks):
    if len(list_of_marks) == 0:
        return -1
    else:
        sum_of_m = 0
        for a_num in list_of_marks:
            sum_of_m = sum_of_m + a_num
            mark_avrg = sum_of_m / len(list_of_marks)
    return mark_avrg


def main():
    print("This program will calculate the average of all the user’s marks.")

    # create a list
    mark_list_of_f = []
    num_mark = None

    # gets user Mark.
    while num_mark != "-1":
        num_mark = input("Please enter your mark and to stop enter -1: ")

        try:
            # convert from a string to a float
            mark_int = float(num_mark)

            # handle invalid inputs.
            if mark_int < -1:
                print("Please enter a positive number.")
                continue
            mark_list_of_f.append(mark_int)

        # Error case
        except Exception:
            print("{} is taken as an invalid mark.".format(num_mark))

    # removing the last number(-1) from the list and call the function
    mark_list_of_f.pop()
    average = calc_average(mark_list_of_f)

    # This play the list and the average to the user
    print("For the lists of marks: {}".format(mark_list_of_f))
    print("The average is: {:,.2f}%".format(average))


if __name__ == "__main__":
    main()

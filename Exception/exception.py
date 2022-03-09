from typing import final


def calculate_expenditure(list_of_expenditure):
    total = 0
    for expenditure in list_of_expenditure:
        total += (int(expenditure))
    print(total)


list_of_values = [100, 200, 300, "400", 500]
calculate_expenditure(list_of_values)


def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")


list_of_values = [100, 200, 300, "400", 500]
calculate_expenditure(list_of_values)

calculate_expenditure(list_of_values)


def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total/num_values
        print("Average:", avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")
    finally:
        print("RUn at end of try excpet")


list_of_values = [100, 200, 300, "400", 500]
num_values = 0
calculate_expenditure(list_of_values)

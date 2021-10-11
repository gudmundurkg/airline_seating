'''
Höfundur: Guðmundur Kristján Guðnason
'''
FIRST_LETTER = 'A'
BOOKED_LETTER = 'X'

def initialize_seating(no_of_rows, no_of_seats):
    ''' Returns an empty seating allocation: list of lists
        Each seat in each row is marked with a letter, starting from "A" '''

    seating = []
    for _ in range(0, no_of_rows):
        seats = []
        # creates consecutive letters starting from first_letter
        for col in range(0, no_of_seats):
            next_letter = chr(ord(FIRST_LETTER) + col)  
            seats.append(next_letter)
        seating.append(seats)
    return seating

def ask_for_rows_and_seats():
    ''' Asks user for the amount of rows and seats on the airplane'''

    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))
    return rows, seats

def print_seating_arrangement(a_list_of_lists):
    ''' Formats and counts each row of seats within the airplane. Prints results, returns nothing '''

    counter = 1
    length_of_row = len(a_list_of_lists[0])
    half_a_row = int((length_of_row / 2))

    for list in a_list_of_lists:
        left_row_list = list[:half_a_row]
        right_row_list = list[half_a_row:]
        left_row_str = " ".join(left_row_list)
        right_row_str = " ".join(right_row_list)
        print(f"{counter:>2}   {left_row_str}   {right_row_str}")
        counter += 1

def offer_user_a_seat():
    ''' Asks user which seat number he would like to book. Returns row and seat numbers '''

    user_choice = input("Input seat number (row seat): ")
    user_choice_split = user_choice.split()
    row_number = user_choice_split[0]
    seat_number = user_choice_split[1]
    return int(row_number), (seat_number)

def check_if_legal_input(row, seat, list_of_lists):
    for list in list_of_lists:
        if seat in list:
            return True

def main():
    user_check = "y"
    no_of_rows, no_of_seats = ask_for_rows_and_seats()
    list_of_lists = initialize_seating(no_of_rows,no_of_seats)
    print_seating_arrangement(list_of_lists)

    while user_check == "y": 
        chosen_row, chosen_seat = offer_user_a_seat()
        chosen_seat = chosen_seat.upper()
        try:
            seat_index = (list_of_lists[chosen_row-1].index(chosen_seat)) # Get index for chosen seat
            list_of_lists[chosen_row-1][seat_index] = (BOOKED_LETTER)
            print_seating_arrangement(list_of_lists)
        except ValueError:
            print("That seat is taken!")
        user_check = input("More seats y/n? ") 
    
# Main program starts here
if __name__ == "__main__":
    main()
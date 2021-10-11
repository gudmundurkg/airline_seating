'''
Höfundur: Guðmundur Kristján Guðnason
'''

'''
Fjöldi raða og fjöldi sæta er stimplað inn af notanda
Þá eru raðir og sæti birt (Sjá mynd 2)

T.D. Raðir eru 7 og sæti eru 4 í hverri röð
Númer raðar er birt fremst
 '''
FIRST_LETTER = 'A'
BOOKED_LETTER = 'X'
LEFT_COLUMN = "{:>2}"
MIDDLE_COLUMN = "{:>3}"
RIGHT_COLUMN = "{:>3}"



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
    
def main():
    no_of_rows, no_of_seats = ask_for_rows_and_seats()
    list_of_lists = initialize_seating(no_of_rows,no_of_seats)
    print_seating_arrangement(list_of_lists)
    
    
# Main program starts here
if __name__ == "__main__":
    main()
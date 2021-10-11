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
    ''' Formats the lists within the list according to examples from instructions and prints them out '''
    counter = 1
    index_counter = 0
    list_example = a_list_of_lists[0]
    length_of_lists= len(list_example)

    for list in a_list_of_lists:
        print("", counter, end ='   ')
        for item in list:
            if index_counter < (length_of_lists/2): # Formatting for the left row of seats
                print(item, end= ' ')
                index_counter += 1
            elif index_counter == (length_of_lists/2): #Formatting for the middle space between rows of seats
                print(" ", item, end=' ')
                index_counter += 1
            else: # Formatting for the right row of seats
                print(item, end= ' ')
                index_counter += 1
        index_counter = 0

        counter += 1
        print()

def main():
    no_of_rows, no_of_seats = ask_for_rows_and_seats()
    list_of_lists = initialize_seating(no_of_rows,no_of_seats)
    print_seating_arrangement(list_of_lists)
    
    
# Main program starts here
if __name__ == "__main__":
    main()
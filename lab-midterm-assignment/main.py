""" CINEMA HALL MOVIE TICKET BOOKING SYSTEM """

class Star_Cinema :
    __hall_list = []
    
    def entry_hall(self, hall) :
        self.__hall_list.append(hall)


# external function for creating user readble seat number
def generate_actual_seat(row, col) :
    letter_row = chr(65+row)
    seat = letter_row + str(col)
    return seat


# external function for creating row, col wise seat number
def generate_row_col_seat(seat) :
    if seat[0] >= "A" and seat[0] <= "D" :
        row_num = ord(seat[0])
        col_num = int(seat[1])
        row_num = row_num - 65
        seat_tuple = (row_num, col_num)
        return seat_tuple, True
    else :
        return seat, False


class Hall(Star_Cinema) :
    __unique_id = 0
    __show_id = 0

    def __init__(self, rows, cols, id) :
        Hall.__unique_id += 1
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = f"{id}" + str(Hall.__unique_id)
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time) :
        id = self.__generate_show_id(id)
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = self.__generate_seat_list()

    def __generate_show_id (self, id) :
        Hall.__show_id += 1
        return f"{id}" + str(Hall.__show_id)

    def __generate_seat_list(self) :
        seat_list = []
        for i in range(self.__rows) :
            seat_list.append([])
        
        for seat in seat_list :
            for i in range(self.__cols) :
                seat.append(False)

        return seat_list

    def book_seats(self, cst_name, ph_number, show_id, booking_seats) :
        sh_found = 0
        ticket_managed = 0
        for show in self.__show_list :
            if show_id in show :
                sh_found = 1
                for book_item in booking_seats[:] :
                    if book_item[0] < len(self.__seats[show_id]) :
                        if book_item[1] < len(self.__seats[show_id][book_item[1]-1]) :
                            if book_item[1] < len(self.__seats[show_id][book_item[1]-1]) :                            
                                if self.__seats[show_id][book_item[0]][book_item[1]] != True :
                                    self.__seats[show_id][book_item[0]][book_item[1]] = True 
                                    ticket_managed = 1
                                else :
                                    if ticket_managed == 0 :
                                        ticket_managed = 0
                                    print("")
                                    print("---------------------------------------------------------------------------------")
                                    print(f"SORRY, THIS '{generate_actual_seat(book_item[0],book_item[1])}' SEAT IS ALREADY BOOKED, PLEASE BOOK ANOTHER SEAT")
                                    print("---------------------------------------------------------------------------------")
                                    booking_seats.remove(book_item)
                            else :
                               print("")
                               print("-------------------------------------------------------------------")
                               print(f"SORRY, THIS '{generate_actual_seat(book_item[0],book_item[1])}' SEAT IS NOT VALID")
                               print("-------------------------------------------------------------------")
                        else :
                            print("")
                            print("-------------------------------------------------------------------")
                            print(f"SORRY, THIS '{generate_actual_seat(book_item[0],book_item[1])}' SEAT IS NOT VALID")
                            print("-------------------------------------------------------------------")
                    else :
                        print("")
                        print("-------------------------------------------------------------------")
                        print(f"SORRY, THIS '{generate_actual_seat(book_item[0],book_item[1])}' SEAT IS NOT VALID")
                        print("-------------------------------------------------------------------")
        if sh_found == 0 :
            print("")
            print("---------------------------------------------")
            print(f"SORRY, SHOW ID: '{show_id}' IS INVALID")
            print("PLEASE TYPE OPTION 1 TO SEE TODAY'S ALL SHOWS")
            print("---------------------------------------------")
            return

        if ticket_managed  == 1 :
            print("")
            print("---------------------TICKET BOOKED SUCCESSFULLY------------------------")
            print(f"NAME: {cst_name}")
            print(f"PHONE NUMBER: {ph_number}")
            for sh in self.view_show_list() :
                if sh[0] == show_id :
                    print(f"MOVIE NAME: {sh[1]}", end="         ")
                    print(f"MOVIE TIME: {sh[2]}")
            print("")
            print("TICKETS: ", end="")
            for seat in booking_seats :
                chair = generate_actual_seat(seat[0], seat[1])
                print(f"{chair}", end=" ")
            print("")
            print(f"HALL: {self.__hall_no}")
            print("-----------------------------------------------------------------------")

    def view_show_list(self) :
        return self.__show_list

    def view_available_seats(self, show_id) :
        show_found = 0
        for show in self.__show_list :
            if show_id in show :
                show_found = 1
                all_seats = self.__seats[show_id]
                for i,seat in enumerate(all_seats) :
                    s_len = len(seat)
                    for j,chair in enumerate(seat) :
                        if chair != True :
                            if s_len != 0 :
                                print(generate_actual_seat(i, j), end="    ")
                                s_len -=1
                        else :
                            print("X", end="     ")
                    print("")
                break
        if show_found == 0 :
            print(f"SHOW ID: '{show_id}' IS NOT VALID")


hall = Hall(4, 5, "Almass")
hall.entry_show("ae12", "BLACK ADAM", "Octobar 30, 2022 | 12:30 PM")
hall.entry_show("ae25", "SPIDER MAN", "Octobar 30, 2022 | 2:30 PM")

print("")
print("-----------------------------------------")
print("CINEMA HALL MOVIE TICKET BOOKING SYSTEM")
print("-----------------------------------------")

while True :
    print("")
    # print("")
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")

    choice = input("ENTER OPTION : ")
    if choice == "1" :
        print("")
        print("--------------------------------------------------------------------------------------")
        for show in hall.view_show_list() :
            print(f"MOVIE NAME: {show[1]}       SHOW ID: {show[0]}      TIME: {show[2]}")
        print("--------------------------------------------------------------------------------------")
    elif choice == "2" :
        sh_id = input("ENTER SHOW ID: ")
        print("")
        print("-------------ALL AVAILABLE SEATS-------------")
        hall.view_available_seats(sh_id)
        print("---------------------------------------------")
    elif choice == "3" :
        name = input("ENTER YOUR NAME: ")
        ph_number = input("ENTER YOUR PHONE NO: ")
        show_id = input("ENTER THE SHOW ID: ")
        num_of_seats = int(input("HOW MANY SEATS DO YOU WANT: "))
        seat_list = []
        for i in range(num_of_seats) :
            inputed_seat = input("ENTER YOUR DESIRE SEAT: ")
            response = generate_row_col_seat(inputed_seat)
            if response[1] == False :
                print("")
                print("-------------------------------------------------------------")
                print(f"SEAT NUMBER '{response[0]}' IS INVALID")
                print("PLEASE TYPE OPTION 2 TO SEE ALL THE AVAILABLE SEATS")
                print("-------------------------------------------------------------")
                print("")
                break 
            else :
                seat_list.append(response[0])

        if len(seat_list) == num_of_seats :
            hall.book_seats(name, ph_number, show_id, seat_list)

    else :
        print("")
        print("-------------------------------------------------------------------------------------")
        print(f"THIS '{choice}' IS A RONG OPTION, PLEASE TYPE A RIGHT OPTION FROM THE BELOW OPTIONS")
        print("-------------------------------------------------------------------------------------")



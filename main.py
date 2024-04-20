class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {} #protected
        self._show_list = [] #protected
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        super().__init__() 

    def entry_show(self, id, movie_name, time):
        info = (id, movie_name, time)
        self._show_list.append(info)

        seat_list = [[0 for i in range(self.cols)] for j in range(self.rows)]

        self._seats[id] = seat_list

    def book_seats(self, id, row, col):
        #seat = []
        if id in self._seats:
            seats = self._seats[id]

            seats[row][col] = 1

    def view_show_list(self):
        for show_info in self._show_list:
            print("Movie:", show_info[1], "Show ID:", show_info[0], "Time:", show_info[2])

    def view_available_seats(self, id):
        if id in self._seats:
            seats = self._seats[id]

        for row in seats:
            print(row)

cinema = Star_Cinema()
hall1 = Hall(5, 5, 1)
hall1.entry_show("111", "Jawan Maji", "22/4/2024")
cinema.entry_hall(hall1)

hall2 = Hall(5, 5, 2)
hall2.entry_show("333", "Sujon Maji", "24/4/2024")
cinema.entry_hall(hall2)


ids_hall1 = []
ids_hall2 = []

for id in hall1._show_list: 
    ids_hall1.append(id[0])
for id in hall2._show_list: 
    ids_hall2.append(id[0])

run = True
while run:
    option = int(input("1.VIEW ALL SHOW TODAY\n2.VIEW AVAILABLE SEATS\n3.BOOK TICKET\n4.EXIT\nENTER OPTION: "))
    
    if option == 1:
        print("-------")
        hall1.view_show_list()
        hall2.view_show_list()
        print("-------")

    elif option == 2:
        start = True
        while start:
            show_id = input("ENTER SHOW ID: ")
            show_id = str(show_id)

            if show_id in ids_hall1 or show_id in ids_hall2:
                if show_id in ids_hall1:
                    hall1.view_available_seats(show_id)

                elif show_id in ids_hall2:
                    hall2.view_available_seats(show_id)
                break
            else:
                raise ValueError("You Entered Wrong Show ID !!!")
    
    elif option == 3:    
        start = True

        while start:
            show_id = input("ENTER SHOW ID: ")

            if show_id in ids_hall1 or show_id in ids_hall2:
                num_of_tickets = int(input("ENTER NUMBER OF TICKETS YOU WANT: "))

                for i in range(num_of_tickets):
                    is_ = True
                    
                    while is_:
                        row = int(input("Enter seat row: "))
                        if show_id in ids_hall1:
                            if row < 0 or row >= hall1.rows:
                                print("You Entered Invalid seat row!!!")        
                            else:
                                break
                        else:
                            if row < 0 or row >= hall2.rows:
                                print("You Entered Invalid seat row!!!")        
                            else:
                                break                            

                    again = True
                    while again:
                        col = int(input("Enter seat column: "))
                        if show_id in ids_hall1:
                            if col < 0 or col >= hall1.cols:
                                print("You Entered Invalid seat row!!!")        
                            else:
                                break
                        else:
                            if col < 0 or col >= hall2.cols:
                                print("You Entered Invalid seat column!!!")        
                            else:
                                break    

                    
                    if show_id in ids_hall1:
                        if hall1._seats[show_id][row][col] == 0:
                            hall1.book_seats(show_id, row, col)
                            print("Congrats! You booked a seat !!!")
                        else:
                            print("This Seat Has Been Booked by others!!!")

                    elif show_id in ids_hall2:
                        if hall2._seats[show_id][row][col] == 0:
                            hall2.book_seats(show_id, row, col)
                            print("Congrats! You booked a seat !!!")
                        else:
                            print("This Seat Has Been Booked by others!!!")                            
                    start = False

            else:
                print("You Entered Wrong Show Id!!!")

    elif option == 4:
        run = False
        break
    
    else:
        raise ValueError("You Entered Wrong Option!!!")        

#                      Car Rental Module
from datetime import datetime
from pytz import timezone

tstamp1 = datetime.strptime(datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),
                            '%Y-%m-%d %H:%M:%S')
print("Current Date-Time = ", tstamp1)

all_cust=[]

class Cars:

    all_cars = []

    def __init__(self, customer_name='', car_name='', car_no='', customer_no = None, brand='', color='', renting_scale='', rate_h=0,
                 rate_d=0,rate_w=0,car_out_time=None,car_in_time=None, availability=''):
        self.customer_name = customer_name
        self.car_name = car_name
        self.car_no = car_no
        self.customer_no = customer_no
        self.brand = brand
        self.color = color
        self.car_out_time = car_out_time
        self.car_in_time = car_in_time
        self.renting_scale = renting_scale
        self.rate_h = rate_h
        self.rate_d = rate_d
        self.rate_w = rate_w
        self.availability = availability

    def create_car(self):
        Cars.all_cars.append(Cars('', 'Tata Altroz', 'KA01V0001', '', 'Tata',
                                  'BLACK', 'H',  70, 65, 62,availability='Y'))
        Cars.all_cars.append(Cars('', 'Tata Nexon', 'KA01V0002', '', 'Tata',
                                  'WHITE', 'W',  80, 75, 72,availability='Y'))
        Cars.all_cars.append(Cars('', 'Tata Safari', 'KA01V0003', '', 'Tata',
                                  'RED', 'W', 90, 85, 80,availability='Y'))
    @staticmethod
    def list_details(self):
        print("************  Available Cars ************")
        self.car_available = 0
        self.car_available_release = 0
        for x in Cars.all_cars:
            print("Car Name : {}".format(x.car_name))
            print("Car No : {}".format(x.car_no))
            print("Brand : {}".format(x.brand))
            print("Color : {}".format(x.color))
            print("Car Out Time : {}".format(x.car_out_time))
            print("Car  In Time : {}".format(x.car_in_time))
            print("Availability : {}".format(x.availability))
            print("Rate H = {}, Rate D = {}, Rate W = {} in Rs/mins".format(x.rate_h,x.rate_d,x.rate_w))
            print("-------------------------")
            if x.availability == 'Y':
                self.car_available += 1
            elif x.availability == 'N':
                self.car_available_release += 1
        if self.car_available == 0:
            print ("Sorry!, No available cars")
        all_customers = []

    def Car_processing(self, car_available='', car_available_release=''):
        cust_no = int(input("Please enter your cust_no"))
        customer_found = '0'
        for cust in all_cust:
            if cust.customer_no == cust_no:
                customer_found = '1'
                while True:
                    print("1. Rent a car")
                    print("2. Release a car")
                    print("3. Back to Main Menu")
                    choice2 = input("Enter your choice")
                    if choice2 == '1':
                        Cars.list_details(self)

                        print("Count of Available cars in the inventory are ", self.car_available)
                        rent_car_no = input("Please enter the car no to rent Or Press '#' to return back")
                        if rent_car_no == '#':
                            continue
                        rent_scale = input("Please enter the Renting Scale - (H)ourly/(D)aily/(W)eekly?")
                        if (rent_scale != 'H' and rent_scale != 'D' and rent_scale != 'W'
                                and rent_scale != 'h' and rent_scale != 'd' and rent_scale != 'w'):
                            print("Please enter valid Renting Scale values - 'H' or 'D'or 'W'")
                            break
                        for c in Cars.all_cars:
                            if c.car_no == rent_car_no and c.availability == 'Y':
                                c.car_no = rent_car_no
                                c.customer_no = cust_no
                                c.availability = 'N'
                                c.renting_scale = rent_scale

                                c.car_out_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
                                c.car_in_time = datetime.strptime('9999-12-31 00:00:00', '%Y-%m-%d %H:%M:%S')

                                print("The car no %s is rented to you!" % c.car_no)
                                break
                        else:
                            print("Please select other car")

                    elif choice2 == '2':
                        #Car_deallocation()
                        Cars.list_details(self)
                        print("Count of Available cars for release in the inventory are ", self.car_available_release)
                        rent_car_no = input("Please enter the Car no to Return Or Press '#' to go back")
                        if rent_car_no == '#':
                            continue

                        for c in Cars.all_cars:
                            if c.car_no == rent_car_no:
                                if c.availability == 'Y':
                                    print("The Car is already available and release not valid")
                                    break
                                if cust_no != c.customer_no:
                                    print("Only the allocated customer can deallocate a car!")
                                    break
                                c.availability = 'Y'
                                print("Car is returned Successfully!")
                                c.car_in_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
                                print("**** Car Bill ****")
                                print("Current Dt-Tm     = ", c.car_in_time)
                                print("Customer Name     = ", cust.customer_name)
                                print("Customer No       = ", c.customer_no)
                                print("Car Renting scale = ", c.renting_scale)

                                car_dur = (datetime.strptime(c.car_in_time, '%Y-%m-%d %H:%M:%S') -
                                           datetime.strptime(c.car_out_time, '%Y-%m-%d %H:%M:%S'))
                                cust.rented_duration = int(round(car_dur.total_seconds() / 60))
                                print("Car was rented for duration = %s mins" % cust.rented_duration)
                                if c.renting_scale == 'H':
                                    cust.rented_bill = cust.rented_duration * c.rate_h
                                elif c.renting_scale == 'D':
                                    cust.rented_bill = cust.rented_duration * c.rate_d
                                else:
                                    cust.rented_bill = cust.rented_duration * c.rate_w

                                print("Car bill is: Rs ", cust.rented_bill)

                                break
                        else:
                            print("Please select another available Car no")

                    else:  # choice == '3':
                        break
                    break
        if customer_found != '1':
            print("Customer Not found!")

class Customer():

    valid_customer = 0
    count = 0
    all_cust=[]
    def __init__(self):
        car = Cars()

        self.customer_name = input("Please enter your name")
        Cars.customer_name = self.customer_name
        if self.customer_name == '':
            print("Please enter a valid customer name")
        else:
            Customer.count += 1
            Customer.valid_customer = 1
        self.customer_no = Customer.count
        self.rented_car_name = None
        self.rented_car_no = None
        self.rented_duration = 0
        self.rented_bill = 0

    def create_customer(self):
        if Customer.valid_customer == 1:
            print("Your customer no is: ", Customer.count)
            all_cust.append(self)
''''''
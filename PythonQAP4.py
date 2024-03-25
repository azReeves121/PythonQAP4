#Program made by AbdulAziz Kassim aka Abdul Reeves
#date 3/24/2024
import datetime
#Constance
POLICY_NUMBER_RATE = "1944"
BASIC_PREMIUM_RATE = 869.00
DISCOUNT_RATE = .25
LIABILITY_COVERAGE_RATE = 130.00
GLASS_COVERAGE_RATE = 86.00
LOANER_COVERAGE_RATE = 58.00
HST_RATE = .15
PROCESSING_FEE_RATE = 39.99

name_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ,'. abcdefghijklmnopqrstuvwxyz")

# program functions
def insurance_premium(num_cars):
    if num_cars == 1:
        return BASIC_PREMIUM_RATE
    if num_cars > 1:
        return BASIC_PREMIUM_RATE + ((BASIC_PREMIUM_RATE - BASIC_PREMIUM_RATE * DISCOUNT_RATE) * (num_cars - 1))

def total_extra_costs(extra_liability, glass_coverage, loaner_car,):
    # Calculate total extra costs if options are selected
    extra_cost = 0
    if extra_liability == 'Y':
        extra_cost += LIABILITY_COVERAGE_RATE * num_cars

    extra_cost = 0
    if glass_coverage == 'Y':
        extra_cost += GLASS_COVERAGE_RATE * num_cars

    extra_cost = 0
    if loaner_car == 'Y':
        extra_cost += LOANER_COVERAGE_RATE * num_cars

    return extra_cost

def monthly_payments(total_cost, down_pay):
    monthly_pay = 0.00
    monthly_pay = (total_cost - down_pay + PROCESSING_FEE_RATE)
    return monthly_pay

province_list = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]


payment_methods_list = ["Full", "Monthly", "Down Pay"]



while True:
    # Get customer first name
    while True:
        first_name = input("Enter customer first name: ").title()
        if first_name == "":
            print("First name cannot be empty.")
        elif not set(first_name).issubset(name_set):
            print("invalid character")
        else:

            break

    # Get customer last name
    while True:
        last_name = input("Enter customer last name: ").title()
        if last_name == "":
            print("First name cannot be empty.")
        elif set(last_name).issubset(name_set) == False:
            print("invalid character")
        else:
            break

    while True:
        street = input("Enter your street ")
        if street == "":
            print("Can't be empty")
        else:
            break

    while True:
        city = input("Enter your city: ")
        if city == "":
            print("Can't be empty")
        else:
            break
    while True:
        province = input("Enter your province: ").upper()
        if province in province_list:
            break
        else:
            print("Invalid province")

    while True:
        postal_code = input("Enter costumer postal code A1A1A1: ").upper()
        if postal_code == "":
            print("Postal code cant not be blank, Please re-enter.")
        elif len(postal_code) != 6:
            print("Postal code most be six characters only, Please re-enter. ")
        elif postal_code[0].isalpha() == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        elif postal_code[1].isdigit == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        elif postal_code[2].isalpha() == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        elif postal_code[3].isdigit() == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        elif postal_code[4].isalpha() == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        elif postal_code[5].isdigit() == False:
            print("Postal code must be entered as :A1A1A1, Please re-enter.")
        else:
            break

    while True:
        phone_number = input("Enter phone number (10 digits): ")
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number format. Please enter 10 digits.")
        else:
            break
    full_name = first_name + " " + last_name
    address = street + " " + city + " " + province + " " + postal_code
    num_cars = int(input("Enter the number of cars being insured: "))
    extra_liability = input("Enter 'Y' for extra liability coverage up to $1,000,000, or 'N' otherwise: ").upper()
    glass_coverage = input("Enter 'Y' for optional glass coverage, or 'N' otherwise: ").upper()
    loaner_car = input("Enter 'Y' if a loaner car is required, or 'N' otherwise: ").upper()

    payment_method = input("Enter payment method (Full, Monthly, or Down Pay): ").title()
    while payment_method not in payment_methods_list:
        payment_method = input("Invalid payment method. Please enter Full, Monthly, or Down Pay: ").title()
    if payment_method == "Down Pay":
        down_pay = float(input("Enter the amount of the down payment: $"))
    else:
        down_pay = 0
    claims_dates_list = []
    claims_amounts_list = []
    while True:
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        if claim_date == "":
            break
        try:
            claim_date = datetime.datetime.strptime(claim_date, "%Y-%m-%d")
            if claim_date > datetime.datetime.now():
                print("Claim date can't be greater than today's date.")
                continue
        except ValueError:
            print("Invalid date, please re-enter.")
            continue

        while True:
            try:
                claim_amount = float(input("Enter claim amount: $"))
                if claim_amount < 0:
                    print("Claim amount can't be less than 0. Please re-enter.")
                else:
                    break
            except ValueError:
                print("Invalid input, please re-enter.")
                continue
        claims_dates_list.append(claim_date)
        claims_amounts_list.append(claim_amount)

    total_extra_cost = total_extra_costs(extra_liability, glass_coverage, loaner_car)
    # Total insurance premium
    insurance = insurance_premium(num_cars)
    total_insurance_premium = insurance + total_extra_cost

    # Calculate HST
    hst = total_insurance_premium * HST_RATE

    # Total cost including HST
    total_cost = total_insurance_premium + hst

    # Determine payment method and calculate monthly payments
    monthly_pay = monthly_payments(total_cost, down_pay)


    # Calculate invoice date (current date)
    invoice_date = datetime.date.today()


    # Calculate first payment date (first day of the next month)
    if invoice_date.month == 12:
        first_payment_date = datetime.date(invoice_date.year + 1, 1, 1)
    else:
        first_payment_date = datetime.date(invoice_date.year, invoice_date.month + 1, 1)

    #DSP OUTPUTS
    invoice_Date_DSP = invoice_date.strftime("%B-%d-%Y")
    first_payment_date_DSP = first_payment_date.strftime("%d-%B-%Y")
    total_extra_cost_DSP = "${:,.2f}".format(total_extra_cost)
    num_cars_DSP = "{:,.0f}".format(num_cars)
    total_cost_DSP = "${:,.2f}".format(total_cost)
    insurance_DSP = "${:,.2f}".format(insurance)
    total_insurance_premium_DSP = "${:,.2f}".format(total_insurance_premium)
    hst_DSP = "${:,.2f}".format(hst)
    monthly_pay_DSP = "${:,.2f}".format(monthly_pay)

    print()
    print(f"          CUSTOMER INFORMATION")
    print(u'\u2500' * 72)
    print(f"Invoice Date:                           {invoice_Date_DSP:>18s}")
    print(f"Welcome:                                       {full_name:<10s}")
    print(f"Address:                          {address:<10s}")
    print(f"Phone Number:                                   {phone_number:<10s}")
    print(f"Number of Cars:                                      {num_cars_DSP:<10s}")
    print(f"Extra liability coverage up to $1,000,000:               {extra_liability:<10s}")
    print(f"Optional glass coverage:                                 {glass_coverage:<10s}")
    print(f"Loaner car is required:                                  {loaner_car:<10s}")
    print(u'\u2500' * 72)
    print(f"              Calculations                                      ")
    print(f"Total Extra Cost:                                  {total_extra_cost_DSP:<10s}")
    print(f"Insurance Cost:                                  {insurance_DSP:<10s}")
    print(f"Total Insurance Premium:                         {total_insurance_premium_DSP:<10s}")
    print(f"HST:                                               {hst_DSP:<10s}")
    print(f"Total Cost:                                      {total_cost_DSP:<10s}")
    print(f" Claims list loop ")
    for i in range(3):
        try:
            claims_dates_list_Dsp = claims_dates_list[i].strftime("%Y-%m-%d")
            claims_amounts_list_Dsp = "{:.2f}".format(claims_amounts_list[i])
        except IndexError:
            claims_dates_list_Dsp = "N/A"
            claims_amounts_list_Dsp = "N/A"
        print(f" {i+1}   {claims_dates_list_Dsp:<10s}   {claims_amounts_list_Dsp:<10s}")
    print(f"-----------------------------")
    print(f"    Invoice date: {invoice_Date_DSP:>10s}    First payment date: {first_payment_date_DSP:<10s} ")
    print(u'\u2500' * 72)
    print(f"")
    Continue = input("Do you want to enter another customer(Y for Yes or N for No)? ").upper()
    if Continue == 'N':
        break

# ROI Rental Property Calculator

# The calculator accepts all sorts of inputs including: payments, expences, and capital investments.

class rentalCalculator():

    def __init__(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def addIncome(self, itemized = []):
        while True:
            print('\nEnter Income below, or type "Back" to return to previous menu ')
            income_item = input('\nWhat type of income would you like to enter? (Options are: "Rent Payments", "Storage", "Parking", or "Pet Rent" ')
            if income_item.lower() == 'rent payments':
                income_amount = int(input('\nInput the $/month amount: ')) * 12
                self.income.append(income_amount)
                itemized.append([income_item, income_amount])
            elif income_item.lower() == 'storage':
                income_amount = int(input('\nInput the $/month amount: ')) * 12
                self.income.append(income_amount)
                itemized.append([income_item, income_amount])
            elif income_item.lower() == 'parking':
                income_amount = int(input('\nInput the $/month amount: ')) * 12
                self.income.append(income_amount)
                itemized.append([income_item, income_amount])
            elif income_item.lower() == 'pet rent':
                income_amount = int(input('\nInput the $/month amount: ')) * 12
                self.income.append(income_amount)
                itemized.append([income_item, income_amount])
            elif income_item.lower() == 'back':
                print(f'\nYour total rental income is {sum(self.income)}/year or {sum(self.income)/12}/month ')
                print(f'\nHere is your itemized list of income: {itemized}')
                break
            else:
                print('Incorrect Income Type')
    
    def addExpense(self, itemized_expenses = []):
        while True:
            print('\nEnter Expenses below, or type "Back" to return to previous menu ')
            expense_item = input('\nWhat type of monthly expense would you like to enter? (Options are: "Mortgage", "Property Tax", "HOA", "Insurance", "Repairs" ')
            if expense_item.lower() == 'mortgage':
                expense_amount = int(input('\nInput the $/month amount: ')) * 12
                self.expenses.append(expense_amount)
                itemized_expenses.append([expense_item, expense_amount])
            elif expense_item.lower() == 'property tax': # All of the property tax rates by state
                tax_rates = {'hi':0.0028, 'al':0.0041, 'co':0.0051, 'la':0.0055, 'dc':0.0056, 'sc':0.0057, 'de':0.0057, 'wv':0.0058, 'nv':0.006, 'wy':0.0061, 
                'ar':0.0062, 'ut':0.0063, 'az':0.0066, 'id':0.0069, 'tn':0.0071, 'ca':0.0076, 'nm':0.008, 'ms':0.0081, 'va':0.0082, 'mt':0.0084, 'nc':0.0084,
                'in':0.0085, 'ky':0.0086, 'fl':0.0089, 'ok':0.009, 'ga':0.0092, 'mo':0.0097, 'or':0.0097, 'nd':0.0098, 'wa':0.0098, 'md':0.0109, 'mn':0.0112,
                'ak':0.0119, 'ma':0.0123, 'sd':0.0131, 'me':0.0136, 'ks':0.0141, 'mi':0.0154, 'oh':0.0156, 'ia':0.0157, 'pa':0.0158, 'ri':0.0163, 'ny':0.0172,
                'ne':0.0173, 'tx':0.0180, 'wi':0.0185, 'vt':0.0190, 'ct':0.0214, 'nh':0.0218, 'il':0.0227, 'nj':0.0249}
                state = input('\nEnter your State. Example "CA" for California ')
                home_value = int(input('\nWhat is the value of the property? '))
                self.expenses.append((tax_rates[state.lower()]) * home_value)
                itemized_expenses.append([expense_item, expense_amount])
            elif expense_item.lower() == 'hoa':
                expense_amount = int(input('\nInput the $/month amount: ')) * 12
                self.expenses.append(expense_amount)
                itemized_expenses.append([expense_item, expense_amount])
            elif expense_item.lower() == 'insurance':
                expense_amount = int(input('\nInput the $/month amount: ')) * 12
                self.expenses.append(expense_amount)
                itemized_expenses.append([expense_item, expense_amount])
            elif expense_item.lower() == 'repairs':
                expense_amount = int(input('\nInput the $/month amount: ')) * 12
                self.expenses.append(expense_amount)
                itemized_expenses.append([expense_item, expense_amount])
            elif expense_item.lower() == 'back':
                print(f'\nYour total property expenses are {sum(self.expenses)}/year or {sum(self.expenses)/12}/month ')
                print(f'Here is your itemized list of yearly expenses: {itemized_expenses} ')
                break
            else:
                print('\nIncorrect Expense Type')

    def myInvestment(self, itemized_investments = []):
        while True:
            print('\nEnter Investments below, or type "Back" to return to previous menu ')
            invest_item = input("\nEnter the type of investment below including: 'purchase price', 'closing costs', 'renovation', 'other' ")
            if invest_item.lower() == 'purchase price':
                invest_amt = int(input('\nInput the $ amount: '))
                self.investment.append(invest_amt)
                itemized_investments.append([invest_item, invest_amt])
            elif invest_item.lower() == 'closing costs':
                invest_amt = int(input('\nInput the $ amount: '))
                self.investment.append(invest_amt)
                itemized_investments.append([invest_item, invest_amt])
            elif invest_item.lower() == 'renovation':
                invest_amt = int(input('\nInput the $ amount: '))
                self.investment.append(invest_amt)
                itemized_investments.append([invest_item, invest_amt])
            elif invest_item.lower() == 'other':
                invest_amt = int(input('\nInput the $ amount: '))
                self.investment.append(invest_amt)
                itemized_investments.append([invest_item, invest_amt])
            elif invest_item.lower() == 'back':
                print(f'\nYour total investments amount to ${sum(self.investment)}')
                print(f'Here is your itemized list of investments: {itemized_investments} ')
                break
            else:
                print('\nIncorrect Investment Type ')

    def seeCash(self):
        cash_flow = sum(self.income) - sum(self.expenses)
        monthly_flow = cash_flow/12
        print('\nYour total Cash Flow so far is: ')
        print(f'${cash_flow}/year or {monthly_flow}/month')


    def calcRoi(self):
        if len(self.investment) > 0:
            total_roi = ((sum(self.income) - sum(self.expenses))/sum(self.investment))*100
            print('\nYour total ROI: ')
            print(f'{total_roi}%')
            print("\nThank you! Goodbye.")
        else:
            print('You need to complete the Investment section before continuing!')
     

rental = rentalCalculator([],[],[])


def runCalculator():
    print("Welcome to the ROI Calculator!")
    print('\nIn order to calculate the ROI of your rental property, please enter your monthly income amounts, your monthly expenses, and the total amount invested into your property!')
    while True:
        user_input = input('What would you like to do? \n"Add Income" to add monthly income amounts\n"Add Expense" to add monthly expenses\n"Add Investment Amount" to add the total amount invested in the property\n"See Cashflow" to view your cashflow\n"Calculate ROI" to view your final ROI: \n"Quit" to exit ')
        if user_input.lower() == 'add income':
            rental.addIncome()
        elif user_input.lower() == 'add expense':
            rental.addExpense()
        elif user_input.lower() == 'add investment amount':
            rental.myInvestment()
        elif user_input.lower() == 'see cashflow':
            rental.seeCash()
        elif user_input.lower() == 'calculate roi':
            rental.calcRoi()
            break
        elif user_input.lower() == 'quit':
            print('\nThank you! Goodbye.')
            break       
                    
runCalculator()
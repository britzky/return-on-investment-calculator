
class ROI_Calculator():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.cash_flow = 0
        self.total_investment = 0
        self.annual_cash_flow = 0
        self.roi = 0
        self.money = {
            'income': {
                'rental_income': 0,
                'laundry_income': 0,
                'storage_income': 0,
                'misc_income': 0,
            },
            'expenses': {
                'tax': 0,
                'insurance': 0,
                'utilities': {
                    'electric': 0,
                    'water': 0,
                    'sewer': 0,
                    'garbage': 0,
                    'gas': 0,
                },
                'hoa': 0,
                'lawn_snow': 0,
                'vacancy': 0,
                'repairs': 0,
                'capex': 0,
                'property_management': 0,
                'mortgage': 0,
            }, 
            'cash_on_cash': {
                'down_payment': 0,
                'closing_costs': 0,
                'rehab_budget': 0,
                'misc': 0,
                'total_investment': 0,
                'annual_cash_flow': 0,
                'roi': 0,
            }
        }   
        
    def income(self):
        '''
        determine monthly income
        '''
        monthly_income = []
        
        rental_total = int(input('rental income: '))
        monthly_income.append(rental_total)
        self.money['income']['rental_income'] = rental_total
        
        laundry_total = int(input('laundry income: '))
        monthly_income.append(laundry_total)
        self.money['income']['laundry_income'] = laundry_total
        
        storage_total = int(input('storage income: '))
        monthly_income.append(storage_total)
        self.money['income']['storage_income'] = storage_total
        
        misc_total = int(input('miscellaneous income: '))
        monthly_income.append(misc_total)
        self.money['income']['misc_income'] = misc_total
        
        self.monthly_income = sum(monthly_income)
        
        print(f'You make ${self.monthly_income} a month \n')


    
    def expenses(self):
        '''
        determine monthly expenses
        '''
        monthly_expenses = []
        
        tax_total = int(input('Taxes: '))
        monthly_expenses.append(tax_total)
        self.money['expenses']['tax'] = tax_total

        insurance_total = int(input('Insurance: '))
        monthly_expenses.append(insurance_total)
        self.money['expenses']['insurance'] = insurance_total

        question = input('Do you pay for utilities or does the tenant? ("y" for you and "t" for tenant)').lower()
        
        if question == 'y':
            electric_total = int(input('Electric: '))
            monthly_expenses.append(electric_total)
            self.money['expenses']['utilities']['electric'] = electric_total
            
            water_total = int(input('Water: '))
            monthly_expenses.append(water_total)
            self.money['expenses']['utilities']['water'] = water_total

            sewage_total = int(input('Sewage: '))
            monthly_expenses.append(sewage_total)
            self.money['expenses']['utilities']['sewage'] = sewage_total

            garbage_total = int(input('Garbage: '))
            monthly_expenses.append(garbage_total)
            self.money['expenses']['utilities']['garbage'] = garbage_total

            gas_total = int(input('Gas: '))
            monthly_expenses.append(gas_total)
            self.money['expenses']['utilities']['gas'] = gas_total
        
        hoa_total = int(input('HOA: '))
        monthly_expenses.append(hoa_total)
        self.money['expenses']['hoa'] = hoa_total

        lawn_snow_total = int(input('Lawn/Snow: '))
        monthly_expenses.append(lawn_snow_total)
        self.money['expenses']['lawn_snow'] = lawn_snow_total

        vacancy_total = int(input('Vacancy: '))
        monthly_expenses.append(vacancy_total)
        self.money['expenses']['vacancy'] = vacancy_total

        repairs_total = int(input('Repair: '))
        monthly_expenses.append(repairs_total)
        self.money['expenses']['repairs'] = repairs_total

        capex_total = int(input('Capex: '))
        monthly_expenses.append(capex_total)
        self.money['expenses']['capex'] = capex_total

        property_management_total = int(input('Property Management: '))
        monthly_expenses.append(property_management_total)
        self.money['expenses']['property_management'] = property_management_total

        mortgage_total = int(input('Mortgage: '))
        monthly_expenses.append(mortgage_total)
        self.money['expenses']['mortgage'] = mortgage_total

        self.monthly_expenses = sum(monthly_expenses)
        
        print(f'You spend ${self.monthly_expenses} a month. \n' )

    def cashFlow(self):
        '''
        Determine cash flow 
        '''
        self.cash_flow = self.monthly_income - self.monthly_expenses 
        self.annual_cash_flow = self.cash_flow * 12
        
        print(f'Your monthly cashflow is ${self.cash_flow} and annually ${self.annual_cash_flow} \n')

    def investment(self):
        '''
        Determine investment total
        '''
        investment_total = []
        
        initial_payment = int(input('Down Payment: '))
        investment_total.append(initial_payment)
        self.money['cash_on_cash']['down_payment'] = initial_payment

        closing_payment = int(input('Closing Cost: '))
        investment_total.append(closing_payment)
        self.money['cash_on_cash']['closing_costs'] = closing_payment

        rehab = int(input('Rehab Budget? '))
        investment_total.append(rehab)
        self.money['cash_on_cash']['down_payment'] = rehab

        miscellaneous = int(input('Miscellaneous Costs:  '))
        investment_total.append(miscellaneous)
        self.money['cash_on_cash']['down_payment'] = miscellaneous

        self.total_investment = sum(investment_total)
        
        print(f'Your total investment is ${self.total_investment} \n')

    def cashOnCash(self):
        '''
        determine cash on cash 
        '''
        self.roi = (self.annual_cash_flow / self.total_investment) * 100
        print(f'You have {self.roi}% cash on cash return on investment \n')

    def runner(self):
        '''
        run all the methods
        '''
        print('For your monthly income, enter totals for the following: \n')
        self.income()
        print('For your monthly expenses, enter totals for the following: \n')
        self.expenses()
        print('\n')
        self.cashFlow()
        print('For your total invesment, enter totals for the following: \n')
        self.investment()
        print('\n')
        self.cashOnCash()

test = ROI_Calculator()
test.runner()

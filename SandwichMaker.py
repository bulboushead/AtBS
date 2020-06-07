import pyinputplus as pyip

print('Welcome to the ultimate sandwich maker')

menuItems = {
    'bread':{
        'wheat':'0.42',
        'white':'0.23',
        'sourdough':'0.86'
    },
    'meat':{
        'chicken':'1.11',
        'turkey':'1.33',
        'ham':'0.99',
        'tofu':'0.22'
    },
    'cheese':{
        'cheddar':'0.38',
        'Swiss':'0.58',
        'mozzarella':'0.04',
        'none':'0.00'
    },
    'condiment':{
        'mayo':'0.01',
        'mustard':'0.02',
        'lettuce':'0.00',
        'tomato':'0.15'
    }
}

breadChoice = pyip.inputMenu(menuItems['bread'],'Do you want %s?' % list(menuItems['bread']))

meatChoice = pyip.inputMenu(menuItems['meat'],'Do you want %s?' % list(menuItems['meat']))

cheeseYesNo = pyip.inputYesNo('Would you like cheese?')

if cheeseYesNo == 'yes':
    cheeseChoice = pyip.inputMenu(menuItems['cheese'],'Do you want %s?' % list(menuItems['cheese']))
else:
    cheeseChoice = 'none'

condimentChoice = pyip.inputMenu(menuItems['condiment'],'Do you want %s?' % list(menuItems['condiment']))

numberOfSandwiches = pyip.inputInt('How many sandwiches would you like?: ', min=1)

print('Your sandwich will cost $%s, thanks!' % round(numberOfSandwiches * (float(menuItems['bread'][breadChoice]) +
                                               float(menuItems['meat'][meatChoice]) +
                                               float(menuItems['cheese'][cheeseChoice]) +
                                               float(menuItems['condiment'][condimentChoice])), 3)
      )


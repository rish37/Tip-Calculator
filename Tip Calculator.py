print('''
.___________. __  .______        ______      ___       __        ______  __    __   __           ___   .___________.  ______   .______      
|           ||  | |   _  \      /      |    /   \     |  |      /      ||  |  |  | |  |         /   \  |           | /  __  \  |   _  \     
`---|  |----`|  | |  |_)  |    |  ,----'   /  ^  \    |  |     |  ,----'|  |  |  | |  |        /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
    |  |     |  | |   ___/     |  |       /  /_\  \   |  |     |  |     |  |  |  | |  |       /  /_\  \    |  |     |  |  |  | |      /     
    |  |     |  | |  |         |  `----. /  _____  \  |  `----.|  `----.|  `--'  | |  `----. /  _____  \   |  |     |  `--'  | |  |\  \----.
    |__|     |__| | _|          \______|/__/     \__\ |_______| \______| \______/  |_______|/__/     \__\  |__|      \______/  | _| `._____|
                                                                                                                                                                                                                                                                                
''')
print('welcome to Tip Calculator!')
total_bill = float(input('What was the total bill? Rs. '))
percentage = int(input('What percentage tip would you like to give ?10, 12 or 15 ?'))
no_people = int(input('How many people to split the bill? '))

percentage = (percentage / 100 ) + 1
Tip_split = (total_bill * percentage)/ no_people
print(f"Each person should pay around: Rs. {round(Tip_split)}")




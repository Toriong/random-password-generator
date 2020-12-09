
from password_character_selection import all_options

import random

spot_1 = ''
spot_2 = ''
spot_3 = ''
spot_4 = ''
spot_5 = ''
spot_6 = ''
spot_7 = ''
spot_8 = ''
spot_9 = ''
spot_10 = ''

password_spot1 = spot_1.replace('', random.choice(all_options))
password_spot2 = spot_2.replace('',random.choice(all_options))
password_spot3 = spot_3.replace('',random.choice(all_options))
password_spot4 = spot_4.replace('',random.choice(all_options))
password_spot5 = spot_5.replace('', random.choice(all_options))
password_spot6 = spot_6.replace('', random.choice(all_options))
password_spot7 = spot_6.replace('', random.choice(all_options))
password_spot8 = spot_6.replace('', random.choice(all_options))
password_spot9 = spot_6.replace('', random.choice(all_options))
password_spot10 = spot_6.replace('', random.choice(all_options))


random_password = (password_spot1 + password_spot2 + password_spot3 + password_spot4 +
      password_spot5 + password_spot6 + password_spot7
      + password_spot8 + password_spot9 + password_spot10)
potential_password = print('Here\'s your randomly generated password: ' + random_password + '.')

answer = input('\n\nWould you like to keep this password? (Y or N)'
      '\n Typer HERE:    ').upper()

if answer == 'Y':
    print('Ok, your new password is: ' + str(random_password) + '.')
elif answer == 'N':
    input('Ok, press ENTER to get a new randomly generated password or create your own.')

















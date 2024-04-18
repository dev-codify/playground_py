
import sys
ray=['Hurawatch','WatchMojo','Netflix','Hulu','Amazon Prime']
print(ray)
user_input=input('\n ENTER SHOW TO REMOVE\n')
if user_input.casefold()== 'hurawatch':
    ray.remove('Hurawatch')
elif user_input.casefold()== 'watchmojo':
    ray.remove('WatchMojo')
elif user_input.casefold() == 'netflix':
    ray.remove('Netflix')
elif user_input.casefold() == 'hulu':
    ray.remove('Hulu')
elif user_input.lower()== 'amazon prime':
    ray.remove('Amazon Prime')
else:
    sys.exit('Try again\n'+'error:\n ○Typo     or\n'+'○Space indentation')
print('\ninfo:  ' + user_input +'  removed')
print('\nSettings changed, these shows will now run:')
print(ray)


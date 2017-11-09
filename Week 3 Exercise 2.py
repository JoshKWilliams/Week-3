# Number Of Pupils      Number of Teams      Children left out
#        137                  27.4                   2
#        628                 125.6                   3
#        89                   17.8                   4
#        23                    4.6                   3



number_of_pupils = int(input('Enter number of pupils: '))
football_teams = number_of_pupils / 5
print(number_of_pupils)
print(football_teams)
x = football_teams
x = int(x)
children_in_teams = x * 5
children_left_out = number_of_pupils - children_in_teams
print(children_left_out)

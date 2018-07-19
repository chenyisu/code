intra_talk = int(input())
exrra_talk = int(input())
city_talk = int(input())
intra_mes = int(input())
extra_mes = int(input())
'''------------set183-------'''
set183 = 0
set183 += 0.08*intra_talk
set183 += 0.139*exrra_talk
set183 += 0.135*city_talk
set183 += 1.128*intra_mes
set183 += 1.483*extra_mes
if(set183<183):
    set183=183
'''------------set383-------'''
set383 = 0
set383 += 0.07*intra_talk
set383 += 0.130*exrra_talk
set383 += 0.121*city_talk
set383 += 1.128*intra_mes
set383 += 1.483*extra_mes
if(set383<383):
    set383=383
'''------------set983-------'''
set983 = 0
set983 += 0.06*intra_talk
set983 += 0.108*exrra_talk
set983 += 0.101*city_talk
set983 += 1.128*intra_mes
set983 += 1.483*extra_mes
if(set983<983):
    set983=983
'''---------------------------'''
if set183 < set383 < set983:
    print("183\n",int(set183),sep ="")
elif set383 < set183 < set983:
    print("383\n",int(set383),sep ="")
elif set183 > set383 > set983:
    print("983\n",int(set983),sep ="")
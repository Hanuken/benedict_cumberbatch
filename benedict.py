#!/usr/bin/python3
import random
names = (
	'Blubberbutt', 
	'Benedict', 
	'Benadryl', 
	'Bonapart', 
	'Brokenbrick', 
	'Benefit', 
	'Scissorkick', 
	'Backitup', 
	'Beezlebub',
	'Burgerking',
	'Blenderdick',
	'Billiardball',
	'Guiltyverdict',
	'Beanbag',
	'Carrotstick',
	'Brodyquest',
	'Beachboy',
	'Bendylick',
	'Baseballmitt',
	'Bedbug',
	'Bunsendburner',
	'Bengaltiger',
	'Budapest',
	'Handpicked'
	)

last_names = (
	'Calldispatch',
	'Comedicmismatch',
	'Cunningscratch',
	'Cumberfinch',
	'Humperdinck',
	'Lumberlatch',
	'Flubbercrack',
	'Cumberbatch',
	'Bandersnatch',
	'Cuttlefish',
	'Slumberbelch',
	'Cupboardlatch',
	'Combyourthatch',
	'Thundermunch',
	'Cricketbat',
	'Johnnycash',
	'Comelycat',
	'Custardbath',
	'Thundercat',
	'Luckycatch',
	'Covertrack',
	'Uptoscratch',
	'Compasstrap',
	'Chunkybap',
	'Candygram'
	)

print('Your Benedict Cumberbatch name is ' + names[random.randint(0, len(names) - 1)] + ' ' +last_names[random.randint(0, len(last_names) - 1)])

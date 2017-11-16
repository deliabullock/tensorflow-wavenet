import pickle


groups = {}

#Group 0
groups['duet'] = 0

#Group 1
groups['classical'] = 1
groups['classic'] = 1
groups['classical'] = 1 
groups['harpsichord'] = 1
groups['harpsicord'] = 1
groups['hard'] = 1
groups['flute'] = 1
groups['violin'] = 1
groups['violins'] = 1
groups['piano solo'] = 1
groups['keyboard'] = 1
groups['flutes'] = 1
groups['cello'] = 1
groups['clarinet'] = 1
groups['orchestra'] = 1
groups['orchestral'] = 1
groups['viola'] = 1
groups['harp'] = 1
groups['strings'] = 1
groups['string'] = 1
groups['organ'] = 1
groups['woodwind'] = 1


#1.  duet

 

#2.  Classical, classic, classical, harpsichord, harpsicord, hard, flute, violin, violins, piano solo, keyboard, flutes, cello, clarinet, orchestra, orchestral, viola, harp, strings, string, organ, woodwind

 

#Group 2
#3.  Techno, electronic, electric, electro, electronica, house

groups['techno'] = 2
groups['electronic'] = 2
groups['electric'] = 2
groups['electro'] = 2
groups['electronica'] = 2
groups['house'] = 2



 
#Group 3
#4.  Ambient, echo, eerie, drone, calm, water, trance, birds, spacey, space

groups['ambient'] = 3
groups['echo'] = 3
groups['eerie'] = 3
groups['drone'] = 3
groups['calm'] = 3
groups['water'] = 3
groups['trance'] = 3
groups['birds'] = 3
groups['spacey'] = 3
groups['space'] = 3

 
#Group 4
#5.  Opera, female opera, male opera, operatic, soprano, medieval, baroque, lute

groups['opera'] = 4
groups['space'] = 4
groups['male opera'] = 4
groups['operatic'] = 4
groups['soprano'] = 4
groups['medieval'] = 4
groups['baroque'] = 4
groups['lute'] = 4


#Group 5
#6.  Funky, funk, disco, dance, synth, synthesizer

groups['funky'] = 5
groups['funk'] = 5
groups['disco'] = 5
groups['dance'] = 5
groups['synth'] = 5
groups['synthesizer'] = 5 


#Group 6
#7.  pop, dance

 
groups['pop'] = 6
groups['dance'] = 6


#Group 7
#8.  Monks, chant, chanting,

 
groups['monks'] = 7
groups['chant'] = 7
groups['chanting'] = 7


#Group 8
#9.  Jazz, jazzy, sax, blues
 
groups['jazz'] = 8
groups['jazzy'] = 8
groups['sax'] = 8
groups['blues'] = 8

 
#Group 9
#10.Oriental, indian, india, eastern, sitar, middle eastern, arabic

 
groups['oriental'] = 9
groups['indian'] = 9
groups['india'] = 9
groups['eastern'] = 9
groups['sitar'] = 9
groups['middle eastern'] = 9
groups['arabic'] = 9


#Group 10
#11.Rap, hip hop

 
groups['rap'] = 10
groups['hip hop'] = 10

#Group 11
#12.Punk, rock, hard rock, soft rock, electric guitar


groups['punk'] = 11
groups['rock'] = 11
groups['hard rock'] = 11
groups['soft rock'] = 11
groups['electric guitar'] = 11

 
#Group 12
#13.Acoustic, acoustic guitar, classical guitar

 
groups['acoustic'] = 12
groups['acoustic guitar'] = 12
groups['classical guitar'] = 12


#Group 13
#14.Celtic, irish


groups['celtic'] = 13
groups['irish'] = 13

 
#Group 14
#15.Choir, chorus, choral,

 
groups['choir'] = 14
groups['chorus'] = 14
groups['choral'] = 14


#Group 15
#16. jungle, bongos, reggae, tribal

 
groups['jungle'] = 15
groups['bongos'] = 15
groups['reggae'] = 15
groups['tribal'] = 15


#Group 16
#17.beats, percussion, beat

 
groups['beats'] = 16
groups['percussion'] = 16
groups['beat'] = 16


#Group 17
#18.fiddle, banjo, country

 
groups['fiddle'] = 17
groups['banjo'] = 17
groups['country'] = 17


#Group 18
#19.modern, new age

 
groups['modern'] = 18
groups['new age'] = 18


#Group 19
#20.metal, heavy, heavy metal


groups['metal'] = 19
groups['heavy'] = 19
groups['heavy metal'] = 19


#Group 20
#21.folk, lute

 
groups['folk'] = 20
groups['lute'] = 20


#Group 21
#22.trumpet, horns, horn

 
groups['trumpet'] = 21
groups['horns'] = 21
groups['horn'] = 21

 

pickle.dump(groups, open('groups_dict.pkl', 'wb'))



#{funk:5:25, 2:6

 

 

 

 

 

 

 

 
'''
, , , , , drums, , , fast, piano, , , vocal, , female, , , male, , , , , , , , , , , , , , , , , , , female voice, ,

, drum, , , , , , instrumental, bass, , no piano, , , , , , , , , , , , , , , spanish, , , no guitar, , male singer, , , , , , , dark, , , , , , , bells, , , , singer, , , , , , , wind, , , , , oboe, , , , , , , hard, mellow, , fast beat, , , , no violin, , , , , , , chimes, , , , , , industrial, , plucking, , , , , , repetitive, airy, world, , deep, , , light, , , , , , , , , no strings, , , , , , , , , scary, , , , , , , , , quick,
'''
 

#men, girl, no voices, man singing, not English, female singing, talking, women, male vocals, no singer, lol, clapping, different, voices, old, slow, guitar, solo, man, voice, guitars, not opera, not classical, not rock, no beat, happy, sad, strange, no drums, woman singing, noise, female singer, no flute, low, female vocals, foreign, no voice, loud, silence, English, no singing, singing, vocals, no vocals, weird, male voice, female vocal, upbeat, quiet, , woman, male vocal, no vocal, , soft

###################################
# Chavtal 4-reg on 12 nodes       #
# girth = 4 and 4-chromatic       #
# Gruenbaum class of graphs       #
# RB december 2005                #
###################################
actionset = [
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
]
valuationdomain = {'min':0.0, 'med':1.0, 'max':2.0}
relation = {
'1': {
'1':0.0,
'2':2.0,
'3':0.0,
'4':0.0,
'5':2.0,
'6':0.0,
'7':2.0,
'8':0.0,
'9':0.0,
'10':2.0,
'11':0.0,
'12':0.0,
},
'2': {
'1':2.0,
'2':0.0,
'3':2.0,
'4':0.0,
'5':0.0,
'6':2.0,
'7':0.0,
'8':2.0,
'9':0.0,
'10':0.0,
'11':0.0,
'12':0.0,
},
'3': {
'1':0.0,
'2':2.0,
'3':0.0,
'4':2.0,
'5':0.0,
'6':0.0,
'7':2.0,
'8':0.0,
'9':2.0,
'10':0.0,
'11':0.0,
'12':0.0,
},
'4': {
'1':0.0,
'2':0.0,
'3':2.0,
'4':0.0,
'5':2.0,
'6':0.0,
'7':0.0,
'8':2.0,
'9':0.0,
'10':2.0,
'11':0.0,
'12':0.0,
},
'5': {
'1':2.0,
'2':0.0,
'3':0.0,
'4':2.0,
'5':0.0,
'6':2.0,
'7':0.0,
'8':0.0,
'9':2.0,
'10':0.0,
'11':0.0,
'12':0.0,
},
'6': {
'1':0.0,
'2':2.0,
'3':0.0,
'4':0.0,
'5':2.0,
'6':0.0,
'7':0.0,
'8':0.0,
'9':0.0,
'10':0.0,
'11':2.0,
'12':2.0,
},
'7': {
'1':2.0,
'2':0.0,
'3':2.0,
'4':0.0,
'5':0.0,
'6':0.0,
'7':0.0,
'8':0.0,
'9':0.0,
'10':0.0,
'11':2.0,
'12':2.0,
},
'8': {
'1':0.0,
'2':2.0,
'3':0.0,
'4':2.0,
'5':0.0,
'6':0.0,
'7':0.0,
'8':0.0,
'9':2.0,
'10':0.0,
'11':0.0,
'12':2.0,
},
'9': {
'1':0.0,
'2':0.0,
'3':2.0,
'4':0.0,
'5':2.0,
'6':0.0,
'7':0.0,
'8':2.0,
'9':0.0,
'10':0.0,
'11':2.0,
'12':0.0,
},
'10': {
'1':2.0,
'2':0.0,
'3':0.0,
'4':2.0,
'5':0.0,
'6':0.0,
'7':0.0,
'8':0.0,
'9':0.0,
'10':0.0,
'11':2.0,
'12':2.0,
},
'11': {
'1':0.0,
'2':0.0,
'3':0.0,
'4':0.0,
'5':0.0,
'6':2.0,
'7':2.0,
'8':0.0,
'9':2.0,
'10':2.0,
'11':0.0,
'12':0.0,
},
'12': {
'1':0.0,
'2':0.0,
'3':0.0,
'4':0.0,
'5':0.0,
'6':2.0,
'7':2.0,
'8':2.0,
'9':0.0,
'10':2.0,
'11':0.0,
'12':0.0,
},
}
reflections ={
    'g1':
    frozenset([
    ('2','5'),('3','4'),('7','10'),('8','9'),('11','12'),
    ]),
    'g2':
    frozenset([		
    ('1','2'),('3','7'),('4','12'),('5','6'),('8','10'),('9','11'),
    ]),
    }
rotations = {
    }

###########################################

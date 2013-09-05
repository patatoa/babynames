__author__ = 'pthomas'

dicNickToID = {'Abe': 110, 'Addie': 111, 'Addy': 112, 'Al': 113, 'Aldie': 114, 'Aloma': 115, 'Alvie': 116, 'Ana': 117,
               'Anita': 118, 'Annie': 119, 'Ara': 120, 'Ari': 121, 'Assie': 122, 'Ave': 123, 'Avi': 124, 'Bas': 125,
               'Bastian': 126, 'Bea': 127, 'Bee': 128, 'Bella': 129, 'Belly': 130, 'Ben': 131, 'Benny': 132,
               'Beth': 133, 'Bettie': 134, 'Carol': 135, 'Cecy': 136, 'Ced': 137, 'Celia': 138, 'Charlie': 139,
               'Cindy': 140, 'Coco': 141, 'Col': 142, 'Danny': 143, 'Des': 144, 'Desi': 145, 'Eva': 146, 'Evie': 147,
               'Evita': 148, 'Flo': 149, 'Fran': 150, 'Francis': 151, 'Fred': 152, 'Freddy': 153, 'Genny': 154,
               'Harry': 155, 'Immie': 156, 'Inga': 157, 'Izzy': 158, 'Jenny': 159, 'Jules': 160, 'Julie': 161,
               'Kim': 162, 'Lee': 163, 'Lem': 164, 'Lemmy': 165, 'Lena': 166, 'Leti': 167, 'Lia': 168, 'Liam': 169,
               'Lina': 170, 'Liv': 171, 'Lizzie': 172, 'Lou': 173, 'Lowe': 174, 'Lucy': 175, 'Lula': 176, 'Maggie': 177,
               'Manny': 178, 'Manu': 179, 'Mare': 180, 'Mattie': 181, 'Mel': 182, 'Mel T.': 183, 'Minta': 184,
               'Minty': 185, 'Mira': 186, 'Miri': 187, 'Mordy': 188, 'Mort': 189, 'Murie': 190, 'Nell': 191,
               'Nick': 192, 'Noe': 193, 'Nor': 194, 'Nora': 195, 'Not Frank': 196, 'Not Judy': 197, 'Olive': 198,
               'Olly?': 199, 'Pal': 200, 'Palomita': 201, 'Penny': 202, 'Percy': 203, 'Perry': 204, 'Pet': 205,
               'Pippi': 206, 'Polly': 207, 'Poppy': 208, 'Pree-T': 209, 'Remon': 210, 'Remy': 211, 'Rick': 212,
               'Ricky': 213, 'Rocky': 214, 'Rodge': 215, 'Ron': 216, 'Ronnie': 217, 'Rory': 218, 'Ryan': 219,
               'Sam': 220, 'Sammy': 221, 'Seb': 222, 'Sid': 223, 'Sol': 224, 'Sy': 225, 'Tally': 226, 'Teddy': 227,
               'Thal': 228, 'Theo': 229, 'Tillie': 230, 'Tobey': 231, 'Tom-Tom': 232, 'Tony': 233, 'Tula': 234,
               'Tulie': 235, 'Vi': 236, 'Will': 237, 'Wolfie': 238, 'Zelda': 239, 'Zor': 240}

dicNickToPrimary = {'Abe': 1, 'Addie': 2, 'Addy': 3, 'Al': 5, 'Aldie': 4, 'Aloma': 84, 'Alvie': 5, 'Ana': 10,
                    'Anita': 10, 'Annie': 6, 'Ara': 9, 'Ari': 10, 'Assie': 11, 'Ave': 13, 'Avi': 13, 'Bas': 97,
                    'Bastian': 97, 'Bea': 14, 'Bee': 17, 'Bella': 8, 'Belly': 8, 'Ben': 15, 'Benny': 15, 'Beth': 29,
                    'Bettie': 29, 'Carol': 19, 'Cecy': 20, 'Ced': 21, 'Celia': 20, 'Charlie': 22, 'Cindy': 59,
                    'Coco': 94, 'Col': 27, 'Danny': 93, 'Des': 28, 'Desi': 28, 'Eva': 39, 'Evie': 33, 'Evita': 33,
                    'Flo': 34, 'Fran': 35, 'Francis': 37, 'Fred': 38, 'Freddy': 38, 'Genny': 40, 'Harry': 43,
                    'Immie': 45, 'Inga': 46, 'Izzy': 48, 'Jenny': 39, 'Jules': 52, 'Julie': 51, 'Kim': 53, 'Lee': 19,
                    'Lem': 54, 'Lemmy': 54, 'Lena': 42, 'Leti': 105, 'Lia': 20, 'Liam': 107, 'Lina': 19, 'Liv': 81,
                    'Lizzie': 29, 'Lou': 60, 'Lowe': 58, 'Lucy': 59, 'Lula': 100, 'Maggie': 109, 'Manny': 31,
                    'Manu': 31, 'Mare': 65, 'Mattie': 67, 'Mel': 68, 'Mel T.': 68, 'Minta': 9, 'Minty': 9, 'Mira': 70,
                    'Miri': 71, 'Mordy': 72, 'Mort': 72, 'Murie': 73, 'Nell': 86, 'Nick': 75, 'Noe': 78, 'Nor': 79,
                    'Nora': 56, 'Not Frank': 36, 'Not Judy': 50, 'Olive': 81, 'Olly?': 80, 'Pal': 84, 'Palomita': 84,
                    'Penny': 86, 'Percy': 87, 'Perry': 87, 'Pet': 88, 'Pippi': 90, 'Polly': 85, 'Poppy': 86,
                    'Pree-T': 91, 'Remon': 92, 'Remy': 92, 'Rick': 21, 'Ricky': 38, 'Rocky': 94, 'Rodge': 95, 'Ron': 18,
                    'Ronnie': 18, 'Rory': 12, 'Ryan': 82, 'Sam': 96, 'Sammy': 96, 'Seb': 97, 'Sid': 99, 'Sol': 65,
                    'Sy': 98, 'Tally': 100, 'Teddy': 102, 'Thal': 101, 'Theo': 102, 'Tillie': 67, 'Tobey': 104,
                    'Tom-Tom': 103, 'Tony': 7, 'Tula': 88, 'Tulie': 88, 'Vi': 105, 'Will': 106, 'Wolfie': 58,
                    'Zelda': 41, 'Zor': 108}

i = 0

for nickname in dicNickToPrimary:
    print "insert into babynames_app_firstname_nickname (id, from_firstname_id, to_firstname_id) values " \
          "( %s, %s, %s )" % (i, dicNickToID[nickname], dicNickToPrimary[nickname])
    i += 1


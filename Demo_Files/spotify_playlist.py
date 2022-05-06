playlist = {
    'title':"erics list",
    'author':'eric',
    'song':[
        {'title':'song1','artist':['BLUE'],'duration':2.6},
        {'title':'song2','artist':['RED'],'duration':3.5},
        {'title':'song3','artist':['GREEN'],'duration':4.5},
    ]
}

# Total duration

songs=(playlist.get('song'))
total = 0
for x in songs:
    total = total + x.get('duration')

print(total)
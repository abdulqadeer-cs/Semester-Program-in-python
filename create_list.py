from os import remove

play_list=["song A ", "Song B" ,"Song C" ,"Song D"]
print("Song One Is a :",play_list[0])
for play_lists in play_list:
    print(play_lists)
#add new list
play_list.append("song E")
print(play_list)

#remove playlist from list
play_list.remove("Song C")
print(play_list)

#modify a list
play_list[0]="Tere Bin OST"
print(play_list)




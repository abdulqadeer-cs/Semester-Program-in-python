play_List=[]
while True:
 song=int(input("Enetr Your Song ('or Stop' ) :"))
 if song == "stop":
    break
 play_List.append(song)
print("\n Your playLIst: ")
for song in play_List:
    print("playing :",song)

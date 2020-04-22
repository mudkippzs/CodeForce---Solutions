TABLE_CARD = input()
HAND = input().split(" ")
FLAG = False
for c in HAND:
	if c[0] in TABLE_CARD or c[1] in TABLE_CARD:
		FLAG = True
		break
if FLAG:
	print("YES")
else:
	print("NO")




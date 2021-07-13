name1 = "ねずこ"
name2 = "ぜんいつ"

print(f"{name1}と{name2}は仲間です")

kime_list = [name1,name2]

name2 = "むざん"

kime_list = [name1,name2]
kime_list.append("ぜんいつ")

for kime in kime_list:
  if kime == "むざん":
    print(f"{kime}:仲間ではないです")
  else:
    print(f"{kime}:仲間です")

name = ["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")

for i in name:
  print(i)

def list_yaiba():
  kime_list = [name1,name2]
  kime_list.append("ぜんいつ")
  for kime in kime_list:
    if kime == "むざん":
      print(f"{kime}:仲間ではないです")
    else:
      print(f"{kime}:仲間です")

list_yaiba()

def gurenge(name):
  for name in name:
    if name == "ぎゆう":
      print("ぎゆうは含まれます") 

name = ["たんじろう","ねずこ","ぎゆう","むざん"]
name.append("ぜんいつ")
gurenge(name)
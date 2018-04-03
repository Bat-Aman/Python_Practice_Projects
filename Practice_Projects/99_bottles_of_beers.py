min = 0
i = 99
while (i >= min):
  if(i == 0):
    print("\n", "NO more bottles of beer on the wall, No more bottles of beer")
    print(" \nGo to the store and buy some more 99 bottles of beer on the wall.")
    break
  
  elif(i == 1):
    print("\n", i, "bottle of beer on the wall,", i, " bottle of beer")
    print(" \nTake one down and pass it around,", (i - 1), "bottle of beer on the wall.")  
  
  else:
    print("\n", i, "bottles of beer on the wall,", i, " bottles of beer")
    print(" \nTake one down and pass it around,", (i - 1), "bottles of beer on the wall.")
  i -= 1
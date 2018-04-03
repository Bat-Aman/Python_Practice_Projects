def valid_side(side1, side2, side3):
  if((side1 + side2 <= side3) or (side2 + side3 <= side1) or (side3 + side1 <= side2)):
    return False
  else:
    a1 = min(side1, side2, side3)
    a3 = max(side1, side2, side3)
    a2 = ((side1 + side2 + side3) - a1 - a3)
    print("Sides sorted: ", a1, a2, a3)
    is_triplets(a1, a2, a3)

def is_triplets(side1, side2, side3):
  side1 = side1 * side1
  side2 = side2 * side2
  side3 = side3 * side3
  if((side1 + side2 == side3)):
    print("YES, They're Triplets!")
  else:
    print("NO, They're not Triplets!")

side1, side2, side3 = map(int, input("Enter the sides of three triangle respectively: ").split())
if(valid_side(side1, side2, side3) == False):
  print("Invalid sides to form triangle.")

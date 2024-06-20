from random import randint


num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
num3 = int(input("ENTER THIRD NUMBER: "))


gen1 = randint(0, 9)
gen2 = randint(0, 9)
gen3 = randint(0, 9)


print(f"USER INPUT: {num1} {num2} {num3}")
print(f"GENERATED NUMBERS: {gen1} {gen2} {gen3}")


if [num1, num2, num3] == [gen1, gen2, gen3]:
    print("You Win!")
else:

    if sorted([num1, num2, num3]) == sorted([gen1, gen2, gen3]):
        print("You partially win!")
    else:
        print("You lose!")

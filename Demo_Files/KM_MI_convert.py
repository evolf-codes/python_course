print("How many KM did you run today")
km = input()


if km: # checks if KM is TRUE / not empty
    mi = float(km) * 1.60934
    mi = round(mi, 2)
    print(f"you ran {mi} miles today")
else:
    print("you did not enter any value")




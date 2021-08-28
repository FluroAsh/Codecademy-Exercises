heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []

for num in heights:
  if num > 161:
    can_ride_coaster.append(num)

print(can_ride_coaster)

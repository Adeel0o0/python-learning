weight = 80
# Ground shipping

if weight <= 2:
 cost_ground_shipping = weight * 1.5 + 20
elif weight <= 6:
 cost_ground_shipping = weight * 3 + 20
elif weight <= 10:
  cost_ground_shipping = weight * 4 + 20
else:
  cost_ground_shipping = weight * 4.75 + 20

print("Ground shipping $", cost_ground_shipping)

cost_premium_shipping = 125.00
print("Ground shipping Premium $", cost_premium_shipping)


#Drone shipping
if weight <= 2:
 cost_drone_shipping = weight * 4.5
elif weight <= 6:
 cost_drone_shipping = weight * 9
elif weight <= 10:
  cost_drone_shipping = weight * 12
else:
  cost_drone_shipping = weight * 14.25

print("Drone Shipping $", cost_drone_shipping)
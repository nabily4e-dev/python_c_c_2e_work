print("\n\n\n\n\n" + ">>>:"), print() # Spaces for convention only!
############################################



alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print(f"You just earned {alien_0['points']} points!")


alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)


alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

# My approach!!
if alien_0['speed'] is 'slow':
    alien_0['x_position'] += 1
elif alien_0['speed'] is 'medium':
    alien_0['x_position'] += 2
else:
    alien_0['x_position'] += 3

print(f"New position: {alien_0['x_position']}")


# The books approach
if alien_0['speed'] is 'slow':
    x_increment = 1
elif alien_0['speed'] is 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] # Permanent Delete!
print(alien_0)




############################################
print('\n') #Spaces for convention only!
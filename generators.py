def number_of_pickles(cucumbers):
    return "{} pickles".format(cucumbers)
    
    
def sum_of_squares(limit):
    total = 0
	for n in range(limit+1):
		total += n**2
		return total
		
# We want to be able to do this
def squares(n):
	values = []
	return [n**2 for n in range(1, n+1)]


def cubes(n):
	for i in range(1, n+1):
		yield i**3	# pass that value and then saves its state
					# until it's called again
					

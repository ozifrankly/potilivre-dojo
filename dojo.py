def umAcem():
	lista = []
	lista = range(1, 101)
	return lista

def fizz(number):
	if(number%3 == 0): 
		return "Fizz"
	else:
		return ""

def buzz(number):
	if(number%5 == 0): 
		return "Buzz"
	else:
		return ""

def fizz_buzz(number):
	return fizz(number) + buzz(number)

def main():
    for number in umAcem():
        print "%d: %s" % (number, fizz_buzz(number))

if __name__ == "__main__":
	main()

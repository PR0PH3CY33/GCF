

try:

	import sys

except Exception as e:

	print("Error: " + str(e))


firstNumberSet = []

secondNumberSet = []



def findGCF(number, arr):

	for i in range(2, int(number)+1):

		calc = int(number) / int(i)

		if((calc % 2) == 0 or str(calc).split('.')[1] == '0'):

			arr.append(int(i))

		else:

			pass




def sortArray(arr):

	for i in range(0, len(arr)):

		for j in range(i+1, len(arr)):

			if(arr[i] < arr[j]):

				temp = arr[i];

				arr[i] = arr[j];

				arr[j] = temp;







def arrayWork():

	sortArray(firstNumberSet) #descending order

	sortArray(secondNumberSet) #descending order

	for i in firstNumberSet:

		if(i in secondNumberSet):

			return i

		else:

			pass







def main():

	try:

		firstNumber = sys.argv[1]

		secondNumber = sys.argv[2]

		findGCF(firstNumber, firstNumberSet)

		findGCF(secondNumber, secondNumberSet)

		gcf = arrayWork()

		print(gcf)



	except IndexError as e:

		print("Error: " + str(e))



main()

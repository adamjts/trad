#THIS IS GOING TO BE THE MARKET INTERFACE
# can use volume to confirm a price movement.

from yahoo_finance import Share
import numpy as np



class polynomial():

	def __init__(self, array_of_coefficients):

		self.array_of_coefficients = array_of_coefficients

		self.degree = len(array_of_coefficients) - 1


	def __str__(self):

		string = ''

		for i in range(0,len(self.array_of_coefficients)):
			string = string + str("%.3f" % self.array_of_coefficients[i]) + 'x^(' + str(self.degree - i) + ')'

			if (i < len(self.array_of_coefficients) -1):
				string = string + ' + '

		return string

	def out(self, x):

		y = 0

		for i in range(0, len(self.array_of_coefficients)):
			y = y + self.array_of_coefficients[i] * (x ** (self.degree - i))

		return y

	def derivative(self, order = 1):


		higher_order_coefficients = self.array_of_coefficients

		for j in range(0,order):

			array_of_coefficients = []

			for i in range(0, len(higher_order_coefficients) - 1):

				array_of_coefficients.append(higher_order_coefficients[i] * (len(higher_order_coefficients) - 1 - i))

			higher_order_coefficients = array_of_coefficients

		return polynomial(array_of_coefficients)
		

		

def bestFit(array_of_points, order = 2):

	y_vector = np.zeros(order + 1)


	for a in range(0, len(y_vector)):

		for b in range(0, len(array_of_points)):

			y_vector[a] = y_vector[a] + (array_of_points[b][1] * (array_of_points[b][0] ** (order - a)))

	M = np.empty([order + 1, order + 1])

	for i in range(0, order + 1):

		for j in range(0, order + 1):

			M[i][j] = 0
			
			for k in range(0, len(array_of_points)):

				M[i][j] = M[i][j] + array_of_points[k][0] ** ((2*order) - (i + j))

	M_inverse = np.linalg.inv(M)

	#make it also return the variance for this bestFit

	return polynomial(np.dot(M_inverse, y_vector))

def hardFit(array_of_prices_and_times):

	#array_of_prices_and_times should be like [[time1,price1], [time2, price2], [time3,price3]]
	# parameter is a set of points... an array of 2d arrays.

	polynomial_degree = len(array_of_prices_and_times) - 1

	M = np.empty([polynomial_degree + 1, polynomial_degree + 1])

	# include handling for linearly dependent funcitons.... det(M) = 0 matrices...

	prices = np.zeros(len(array_of_prices_and_times))

	for i in range(0,len(array_of_prices_and_times)):

		prices[i] = array_of_prices_and_times[i][1]

		for j in range(0,len(array_of_prices_and_times)):
			M[i][j] = array_of_prices_and_times[i][0] ** (polynomial_degree - j)



	M_inverse = np.linalg.inv(M)

	abc = np.dot(M_inverse, prices)

	return polynomial(abc)



	# use matrices to solve a system of equations and this gives you the polynomial.
	#[x^2, x, 1] dot [a, b , c] = y1
	#[x^2, x, 1]
	#[]




	return function


class Topten():

    def __init__(self):
	    self.num= 1

	def __iter__(self):
        return self

	def __next__(self):
		if self.num <= 10:

			values = self.num
			self.num +=1

			return values
		else:
			raise StopIteration


value = Topten(1)

for i in value:
	print(i)


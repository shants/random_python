class My_LL:
	def __init__(self, data):
		self._data = data
		self._next = None

	def setData(self, data):
		self._data = data
	
	def setNext(self, data):
		self._next = data

	def getData(self):
		return self._data

	def getNext(self):
		return self._next


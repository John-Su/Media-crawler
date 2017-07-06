#! env:python3
'''
Sparse Matrix
'''
import struct
import numpy as np
import os

total = 0
class suSparse():

	def __init__(self, container = {}, dem = [128,128], dft = 0, sparsedir = 'sparce/', cachemax = 100000, filemax = 100000, head = 'matrix'):
		self.cache = container
		self._dft = dft
		assert len(dem) >1, len(dem) < 10
		self._dem = dem
		self._sparsedir = sparsedir
		self._head = head + str(dem)
		self._filemax = filemax
		self._cachemax = cachemax
		if not os.path.isdir(sparsedir):
			os.mkdir(sparsedir)
		self._nums = self._getnums()
		print( self._nums)

	def setitem(self, index, value = 1):
		sub,filename = self._sub(index)
		if not self.getitem(index) == 0:
			return 1 
		ib = self._pack(sub,value)
		if (len(self.cache) >= self._cachemax):
			self.cache.popitem()
			self.cache[sub] = value
		else:
			self.cache[sub] = value
		try:
			fp = open(self._sparsedir+filename,'ab')
			fp.write(ib)
			fp.close()
		except:
			fp = open(self._sparsedir+filename,'wb')
			fp.write(ib)
			fp.close()
		self._nums += 1
		self._setnums()

	def _getnums(self):
		filename = self._head + '_nums.txt'
		try:
			fp = open(self._sparsedir + filename,'r')
			nums = fp.read()
			fp.close()
			return int(nums)
		except:
			return 0
	def _setnums(self):
		filename = self._head + '_nums.txt'
		try:
			fp = open(self._sparsedir+filename,'w')
			fp.write(str(self._nums))
			fp.close()
		except:
			raise FileOpenError('open file failed')

			
		
			
	def getitem(self, index):
		sub,filename = self._sub(index)
		try:
			return self.cache[sub]
		except:
			return self.__from_file(sub,filename)
	def __from_file(self,sub,filename):
		try:
			fp = open(self._sparsedir+filename,'rb')
			data = self._unpack(fp.read())
			try:
				return int(data[sub])
			except:
				return self._dft
		except:
			return self._dft
	
	def _pack(self,sub,value):
		sub = sub.split(',')
		assert len(sub) == len(self._dem)
		if len(self._dem) == 2:
			return struct.pack('2is',int(sub[0]),int(sub[1]),str(value).encode('utf-8'))
		elif len(self._dem) == 3:
			return struct.pack('3is',int(sub[0]),int(sub[1]),int(sub[2]),str(value).encode('utf-8'))
		elif len(self._dem) == 4:
			return struct.pack('4is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),str(value).encode('utf-8'))
		elif len(self._dem) == 5:
			return struct.pack('5is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),int(sub[4]),str(value).encode('utf-8'))
		elif len(self._dem) == 6:
			return struct.pack('6is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),int(sub[4]),int(sub[5]),str(value).encode('utf-8'))
		elif len(self._dem) == 7:
			return struct.pack('7is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),int(sub[4]),int(sub[5]),int(sub[6]),str(value).encode('utf-8'))
		elif len(self._dem) == 8:
			return struct.pack('8is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),int(sub[4]),int(sub[5]),int(sub[6]),int(sub[7]),str(value).encode('utf-8'))
		elif len(self._dem) == 9:
			return struct.pack('9is',int(sub[0]),int(sub[1]),int(sub[2]),int(sub[3]),int(sub[4]),int(sub[5]),int(sub[6]),int(sub[7]),int(sub[8]),str(value).encode('utf-8'))

		
	def _unpack(self,data):
		output = {}
		if len(self._dem) == 2:
			middle = np.fromstring(data, dtype = '2i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 3:
			middle = np.fromstring(data, dtype = '3i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 4:
			middle = np.fromstring(data, dtype = '4i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 5:
			middle = np.fromstring(data, dtype = '5i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 6:
			middle = np.fromstring(data, dtype = '6i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 7:
			middle = np.fromstring(data, dtype = '7i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 8:
			middle = np.fromstring(data, dtype = '8i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output
		elif len(self._dem) == 9:
			middle = np.fromstring(data, dtype = '9i,c')
			for i in middle:
				output[str(i[0]).replace('[','').replace(']','').replace(' ',',')] = i[1]
			return output

		
	def _sub(self, index):
		assert type(index) == list
		assert len(index) == len(self._dem)
		sub = ''
		seq = 1
		for i in range(0,len(index)):
			if index[i] >= self._dem[i] or index[i] <= 0:
				raise IndexError('invalid index')
			sub += str(index[i]) + ','
			seq *= index[i]
		sub = sub[:-1]
		filename = self._head + '_' + str(int(seq / self._filemax)) + '.spa'

		return sub, filename























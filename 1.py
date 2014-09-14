#!/usr/bin/env python

class fooclass(object):
	"""docstring for fooclass"""
	version = 0.1
	def __init__(self,nm="ok!"):
		self.name = nm
		print "1 ",nm
	def  show(self):
		print self.name
		print  self.__class__.__name__
foo = fooclass()
foo.show()

import os
import time

class AppState(object):

	report_path = time.strftime("%Y%m%d-%H%M%S")
	next_page_key = None
	conversations = []

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(AppState, cls).__new__(cls)
		return cls.instance
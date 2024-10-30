# Copyright (c) 2024, Ndirangu Kariuki and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# Run code every time a record is saved
	def before_save(self):
		self.full_name: f'{self.first_name} {self.last_name} or " "'
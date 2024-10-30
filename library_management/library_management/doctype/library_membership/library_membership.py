# Copyright (c) 2024, Ndirangu Kariuki and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document # type: ignore
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
	#check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                #Validate dates
                "to_date": (">", self.from_date),
			},
		)
        if exists:
            frappe.throw("There is an active membership for this member")

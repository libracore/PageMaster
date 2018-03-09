from __future__ import unicode_literals
import frappe

def get_context(context):
	selection = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'select_1' AND doctype = 'Main Page Setup'", as_dict=True)
	if selection[0].value == "Image":
		context.image = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img' AND doctype = 'Main Page Setup'", as_dict=True)
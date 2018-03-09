from __future__ import unicode_literals
import frappe

def get_context(context):
	context.image = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'select_1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image = True
		context.imagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img' AND doctype = 'Main Page Setup'", as_dict=True)
	else:
		context.sliders = frappe.db.sql("SELECT slide_img_alt, slide_img FROM `tabMain Page Slider` WHERE parent = 'Main Page Setup' ORDER BY idx ASC", as_dict=True)
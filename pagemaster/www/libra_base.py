from __future__ import unicode_literals
import frappe

def get_context(context):
	context.bodyimage = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.bodyimage = True
		context.bodyimagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img' AND doctype = 'Main Page Setup'", as_dict=True)
		context.bodyimageheight = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img_height' AND doctype = 'Main Page Setup'", as_dict=True)
from __future__ import unicode_literals
import frappe

def get_context(context):
	#body
	# -->Background
	context.bodyimage = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.bodyimage = True
		context.bodyimagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#navbar
	#tbd...
	
	#Part 1
	#-->image
	context.image = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image = True
		context.imagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part1' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider = True
		context.slideshow = frappe.get_doc("Page Slideshow", frappe.db.sql("SELECT name FROM `tabPage Slideshow`", as_dict=True)[0].name)
		# to be completed....
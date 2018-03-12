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
	
	#footer
	#tbd...
	
	#Part 1
	#---------------
	#-->image
	context.image1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image1 = True
		context.imagesource1 = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part1' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider1 = True
		context.slideshow1 = frappe.db.sql("SELECT parent,idx,slider_img,img_alt FROM `tabPage Slider`", as_dict=True)
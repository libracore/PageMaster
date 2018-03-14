from __future__ import unicode_literals
import frappe

def get_context(context):
	#part qty
	context.parts = int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'section_qty' AND doctype = 'Main Page Setup'", as_dict=True)[0].value)
	
	#body
	#---------------
	# -->Background-Image
	context.bodyimage = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.bodyimage = True
		context.bodyimagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img' AND doctype = 'Main Page Setup'", as_dict=True)
		
	# -->Background-Color
	context.bodycolor = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Color":
		context.bodycolor = True
		context.bodycolorcode = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_color' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#navbar
	#---------------------
	context.navbar = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_navbar' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "1":
		context.navbar = True
		context.nav_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_bg_color' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
		context.nav_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_txt_color' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
	#footer
	#-------------------
	context.footer = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_footer' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "1":
		context.footer = True
		context.footer_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_bg_color' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
		context.footer_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_txt_color' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
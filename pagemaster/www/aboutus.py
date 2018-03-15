from __future__ import unicode_literals
import frappe

def get_context(context):
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
		
	#timeline
	#-----------------------
	context.timeline = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_timeline' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.timeline = True
		
	#cards
	#--------------------------
	context.card = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_cards' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.card = True
		card_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'cards'", as_dict=True)[0].value
		context.cards = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card_parent+"' ORDER BY idx ASC", as_dict=True)
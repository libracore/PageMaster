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
		
	#-->card
	context.card1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card1 = True
		card1_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part1'", as_dict=True)[0].value
		context.cards1 = frappe.db.sql("SELECT link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card1_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#-->Text
	context.text1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Text":
		context.text1 = True
		context.txt1 = frappe.db.sql("SELECT value FROM tabSingles WHERE doctype = 'Main Page Setup' AND field = 'txt_part1'", as_dict=True)[0].value
		
	#-->media
	context.media1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Media":
		context.media1 = True
		media1_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'media_part1'", as_dict=True)[0].value
		context.medias1 = frappe.db.sql("SELECT media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media1_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#Part 2
	#---------------
	#-->image
	context.image2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image2 = True
		context.imagesource2 = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part2' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider2 = True
		context.slideshow2 = frappe.db.sql("SELECT parent,idx,slider_img,img_alt FROM `tabPage Slider`", as_dict=True)
		
	#-->card
	context.card2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card2 = True
		card2_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part2'", as_dict=True)[0].value
		context.cards2 = frappe.db.sql(" SELECT link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card2_parent+"' ORDER BY idx ASC", as_dict=True)
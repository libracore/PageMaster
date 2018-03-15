from __future__ import unicode_literals
import frappe

def get_context(context):
	#part qty
	context.parts = int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'section_qty' AND doctype = 'Main Page Setup'", as_dict=True)[0].value)
	
	#body
	#---------------
	# -->Background-Image
	context.bodyimage = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Body Settings'", as_dict=True)[0].value == "Image":
		context.bodyimage = True
		context.bodyimagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img' AND doctype = 'Body Settings'", as_dict=True)
		
	# -->Background-Color
	context.bodycolor = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Body Settings'", as_dict=True)[0].value == "Color":
		context.bodycolor = True
		context.bodycolorcode = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_color' AND doctype = 'Body Settings'", as_dict=True)
		
	#navbar
	#---------------------
	context.navbar = True
	context.nav_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_bg_color' AND doctype = 'Navbar'", as_dict=True)[0].value
	context.nav_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_txt_color' AND doctype = 'Navbar'", as_dict=True)[0].value
	context.navlinks = frappe.db.sql("SELECT title, link FROM `tabNavbar Item` WHERE parent = 'Navbar' ORDER BY idx ASC", as_dict=True)
	
	#footer
	#-------------------
	context.footer = True
	context.footer_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_bg_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.footer_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_txt_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.txt = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'txt' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link_title' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	
	#Part 1
	#---------------
	#ROW settings
	#Height & Background-Color
	if int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'set_height_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value) == 1:
		context.part1_height = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'height_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	context.part1_bg = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
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
		context.cards1 = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card1_parent+"' ORDER BY idx ASC", as_dict=True)
		
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
		context.medias1 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media1_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#Part 2
	#---------------
	#ROW settings
	#Height & Background-Color
	if int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'set_height_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value) == 1:
		context.part2_height = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'height_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	context.part2_bg = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
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
		context.cards2 = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card2_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#-->Text
	context.text2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Text":
		context.text2 = True
		context.txt2 = frappe.db.sql("SELECT value FROM tabSingles WHERE doctype = 'Main Page Setup' AND field = 'txt_part2'", as_dict=True)[0].value
		
	#-->media
	context.media2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Media":
		context.media2 = True
		media2_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'media_part2'", as_dict=True)[0].value
		context.medias2 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media2_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#Part 3
	#---------------
	#ROW settings
	#Height & Background-Color
	if int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'set_height_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value) == 1:
		context.part3_height = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'height_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	context.part3_bg = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
	#-->image
	context.image3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image3 = True
		context.imagesource3 = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part3' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider3 = True
		context.slideshow3 = frappe.db.sql("SELECT parent,idx,slider_img,img_alt FROM `tabPage Slider`", as_dict=True)
		
	#-->card
	context.card3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card3 = True
		card3_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part3'", as_dict=True)[0].value
		context.cards3 = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card3_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#-->Text
	context.text3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Text":
		context.text3 = True
		context.txt3 = frappe.db.sql("SELECT value FROM tabSingles WHERE doctype = 'Main Page Setup' AND field = 'txt_part3'", as_dict=True)[0].value
		
	#-->media
	context.media3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Media":
		context.media3 = True
		media3_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'media_part3'", as_dict=True)[0].value
		context.medias3 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media3_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#Part 4
	#---------------
	#ROW settings
	#Height & Background-Color
	if int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'set_height_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value) == 1:
		context.part4_height = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'height_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	context.part4_bg = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
	#-->image
	context.image4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image4 = True
		context.imagesource4 = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part4' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider4 = True
		context.slideshow4 = frappe.db.sql("SELECT parent,idx,slider_img,img_alt FROM `tabPage Slider`", as_dict=True)
		
	#-->card
	context.card4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card4 = True
		card4_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part4'", as_dict=True)[0].value
		context.cards4 = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card4_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#-->Text
	context.text4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Text":
		context.text4 = True
		context.txt4 = frappe.db.sql("SELECT value FROM tabSingles WHERE doctype = 'Main Page Setup' AND field = 'txt_part4'", as_dict=True)[0].value
		
	#-->media
	context.media4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Media":
		context.media4 = True
		media4_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'media_part4'", as_dict=True)[0].value
		context.medias4 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media4_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#Part 5
	#---------------
	#ROW settings
	#Height & Background-Color
	if int(frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'set_height_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value) == 1:
		context.part5_height = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'height_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	context.part5_bg = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value
	
	#-->image
	context.image5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Image":
		context.image5 = True
		context.imagesource5 = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'img_part5' AND doctype = 'Main Page Setup'", as_dict=True)
		
	#-->slider
	context.slider5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Slideshow":
		context.slider5 = True
		context.slideshow5 = frappe.db.sql("SELECT parent,idx,slider_img,img_alt FROM `tabPage Slider`", as_dict=True)
		
	#-->card
	context.card5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card5 = True
		card5_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part5'", as_dict=True)[0].value
		context.cards5 = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card5_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#-->Text
	context.text5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Text":
		context.text5 = True
		context.txt5 = frappe.db.sql("SELECT value FROM tabSingles WHERE doctype = 'Main Page Setup' AND field = 'txt_part5'", as_dict=True)[0].value
		
	#-->media
	context.media5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Media":
		context.media5 = True
		media5_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'media_part5'", as_dict=True)[0].value
		context.medias5 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media5_parent+"' ORDER BY idx ASC", as_dict=True)
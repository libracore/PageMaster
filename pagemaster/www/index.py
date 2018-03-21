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
		slider1_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'slider_part1'", as_dict=True)[0].value
		context.sliders1 = frappe.db.sql("SELECT img_title, img_description, slider_img, img_alt FROM `tabPage Slider` WHERE parent = '"+slider1_parent+"' ORDER BY idx ASC", as_dict=True)
		context.slider_intro1 = frappe.db.sql("SELECT slider_intro FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].slider_intro
		context.slider1_indicator_show = frappe.db.sql("SELECT indicator_show FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].indicator_show
		context.slider1_desc_below = frappe.db.sql("SELECT slider_desc_below FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].slider_desc_below
		context.slider1_width = frappe.db.sql("SELECT slider_width FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].slider_width
		context.slider1_height = frappe.db.sql("SELECT slider_height FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].slider_height
		if int(frappe.db.sql("SELECT man_bootstrap FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].man_bootstrap) == 1:
			context.slider1_left = int(frappe.db.sql("SELECT `left` FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].left)
			context.slider1_middle = int(frappe.db.sql("SELECT `middle` FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].middle)
			context.slider1_right = int(frappe.db.sql("SELECT `right` FROM `tabPage Slideshow` WHERE title = '"+slider1_parent+"'", as_dict=True)[0].right)
	
	#-->card
	context.card1 = False
	context.incl_modal1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card1 = True
		card1_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part1'", as_dict=True)[0].value
		if int(frappe.db.sql("SELECT incl_modal FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].incl_modal) == 1:
			context.incl_modal1 = True
		context.card1_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].mob_qty)
		context.card1_mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].tablet_qty)
		context.card1_tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].desktop_qty)
		context.card1_desktop_qty = 12 / desktop_qty
		context.card1_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].card_bg_color
		context.card1_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card1_parent+"'", as_dict=True)[0].btn_bg_color
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
		context.media_title1 = frappe.db.sql("SELECT media_intro FROM `tabMedia Set` WHERE title = '"+media1_parent+"'", as_dict=True)[0].media_intro
		context.media1_bg_color = frappe.db.sql("SELECT media_bg_color FROM `tabMedia Set` WHERE title = '"+media1_parent+"'", as_dict=True)[0].media_bg_color
		context.medias1 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media1_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#-->box
	context.box1 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part1' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Box":
		context.box1 = True
		box1_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'box_part1'", as_dict=True)[0].value
		context.boxes1 = frappe.db.sql("SELECT title, fontawesome, content FROM `tabPage Box` WHERE parent = '"+box1_parent+"' ORDER BY idx ASC", as_dict=True)
	
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
		slider2_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'slider_part2'", as_dict=True)[0].value
		context.slider_intro2 = frappe.db.sql("SELECT slider_intro FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].slider_intro
		context.slider2_indicator_show = frappe.db.sql("SELECT indicator_show FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].indicator_show
		context.slider2_desc_below = frappe.db.sql("SELECT slider_desc_below FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].slider_desc_below
		context.slider2_width = frappe.db.sql("SELECT slider_width FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].slider_width
		context.slider2_height = frappe.db.sql("SELECT slider_height FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].slider_height
		context.sliders2 = frappe.db.sql("SELECT img_title, img_description, slider_img, img_alt FROM `tabPage Slider` WHERE parent = '"+slider2_parent+"' ORDER BY idx ASC", as_dict=True)
		if int(frappe.db.sql("SELECT man_bootstrap FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].man_bootstrap) == 1:
			context.slider2_left = int(frappe.db.sql("SELECT `left` FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].left)
			context.slider2_middle = int(frappe.db.sql("SELECT `middle` FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].middle)
			context.slider2_right = int(frappe.db.sql("SELECT `right` FROM `tabPage Slideshow` WHERE title = '"+slider2_parent+"'", as_dict=True)[0].right)
		
	#-->card
	context.card2 = False
	context.incl_modal2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card2 = True
		card2_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part2'", as_dict=True)[0].value
		if int(frappe.db.sql("SELECT incl_modal FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].incl_modal) == 1:
			context.incl_modal2 = True
		context.card2_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].mob_qty)
		context.card2_mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].tablet_qty)
		context.card2_tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].desktop_qty)
		context.card2_desktop_qty = 12 / desktop_qty
		context.card2_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].card_bg_color
		context.card2_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card2_parent+"'", as_dict=True)[0].btn_bg_color
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
		context.media_title2 = frappe.db.sql("SELECT media_intro FROM `tabMedia Set` WHERE title = '"+media2_parent+"'", as_dict=True)[0].media_intro
		context.media2_bg_color = frappe.db.sql("SELECT media_bg_color FROM `tabMedia Set` WHERE title = '"+media2_parent+"'", as_dict=True)[0].media_bg_color
		context.medias2 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media2_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#-->box
	context.box2 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part2' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Box":
		context.box2 = True
		box2_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'box_part2'", as_dict=True)[0].value
		context.boxes2 = frappe.db.sql("SELECT title, fontawesome, content FROM `tabPage Box` WHERE parent = '"+box2_parent+"' ORDER BY idx ASC", as_dict=True)
		
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
		slider3_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'slider_part3'", as_dict=True)[0].value
		context.slider_intro3 = frappe.db.sql("SELECT slider_intro FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].slider_intro
		context.slider3_indicator_show = frappe.db.sql("SELECT indicator_show FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].indicator_show
		context.slider3_desc_below = frappe.db.sql("SELECT slider_desc_below FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].slider_desc_below
		context.slider3_width = frappe.db.sql("SELECT slider_width FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].slider_width
		context.slider3_height = frappe.db.sql("SELECT slider_height FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].slider_height
		context.sliders3 = frappe.db.sql("SELECT img_title, img_description, slider_img, img_alt FROM `tabPage Slider` WHERE parent = '"+slider3_parent+"' ORDER BY idx ASC", as_dict=True)
		if int(frappe.db.sql("SELECT man_bootstrap FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].man_bootstrap) == 1:
			context.slider3_left = int(frappe.db.sql("SELECT `left` FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].left)
			context.slider3_middle = int(frappe.db.sql("SELECT `middle` FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].middle)
			context.slider3_right = int(frappe.db.sql("SELECT `right` FROM `tabPage Slideshow` WHERE title = '"+slider3_parent+"'", as_dict=True)[0].right)
		
	#-->card
	context.card3 = False
	context.incl_modal3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card3 = True
		card3_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part3'", as_dict=True)[0].value
		if int(frappe.db.sql("SELECT incl_modal FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].incl_modal) == 1:
			context.incl_modal3 = True
		context.card3_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].mob_qty)
		context.card3_mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].tablet_qty)
		context.card3_tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].desktop_qty)
		context.card3_desktop_qty = 12 / desktop_qty
		context.card3_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].card_bg_color
		context.card3_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card3_parent+"'", as_dict=True)[0].btn_bg_color
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
		context.media_title3 = frappe.db.sql("SELECT media_intro FROM `tabMedia Set` WHERE title = '"+media3_parent+"'", as_dict=True)[0].media_intro
		context.media3_bg_color = frappe.db.sql("SELECT media_bg_color FROM `tabMedia Set` WHERE title = '"+media3_parent+"'", as_dict=True)[0].media_bg_color
		context.medias3 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media3_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#-->box
	context.box3 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part3' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Box":
		context.box3 = True
		box3_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'box_part3'", as_dict=True)[0].value
		context.boxes3 = frappe.db.sql("SELECT title, fontawesome, content FROM `tabPage Box` WHERE parent = '"+box3_parent+"' ORDER BY idx ASC", as_dict=True)
		
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
		slider4_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'slider_part4'", as_dict=True)[0].value
		context.slider_intro4 = frappe.db.sql("SELECT slider_intro FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].slider_intro
		context.slider4_indicator_show = frappe.db.sql("SELECT indicator_show FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].indicator_show
		context.slider4_desc_below = frappe.db.sql("SELECT slider_desc_below FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].slider_desc_below
		context.slider4_width = frappe.db.sql("SELECT slider_width FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].slider_width
		context.slider4_height = frappe.db.sql("SELECT slider_height FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].slider_height
		context.sliders4 = frappe.db.sql("SELECT img_title, img_description, slider_img, img_alt FROM `tabPage Slider` WHERE parent = '"+slider4_parent+"' ORDER BY idx ASC", as_dict=True)
		if int(frappe.db.sql("SELECT man_bootstrap FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].man_bootstrap) == 1:
			context.slider4_left = int(frappe.db.sql("SELECT `left` FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].left)
			context.slider4_middle = int(frappe.db.sql("SELECT `middle` FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].middle)
			context.slider4_right = int(frappe.db.sql("SELECT `right` FROM `tabPage Slideshow` WHERE title = '"+slider4_parent+"'", as_dict=True)[0].right)
		
	#-->card
	context.card4 = False
	context.incl_modal4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card4 = True
		card4_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part4'", as_dict=True)[0].value
		if int(frappe.db.sql("SELECT incl_modal FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].incl_modal) == 1:
			context.incl_modal4 = True
		context.card4_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].mob_qty)
		context.card4_mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].tablet_qty)
		context.card4_tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].desktop_qty)
		context.card4_desktop_qty = 12 / desktop_qty
		context.card4_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].card_bg_color
		context.card4_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card4_parent+"'", as_dict=True)[0].btn_bg_color
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
		context.media_title4 = frappe.db.sql("SELECT media_intro FROM `tabMedia Set` WHERE title = '"+media_title4+"'", as_dict=True)[0].media_intro
		context.media4_bg_color = frappe.db.sql("SELECT media_bg_color FROM `tabMedia Set` WHERE title = '"+media4_parent+"'", as_dict=True)[0].media_bg_color
		context.medias4 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media4_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#-->box
	context.box4 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part4' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Box":
		context.box4 = True
		box4_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'box_part4'", as_dict=True)[0].value
		context.boxes4 = frappe.db.sql("SELECT title, fontawesome, content FROM `tabPage Box` WHERE parent = '"+box4_parent+"' ORDER BY idx ASC", as_dict=True)
		
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
		slider5_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'slider_part5'", as_dict=True)[0].value
		context.slider_intro5 = frappe.db.sql("SELECT slider_intro FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].slider_intro
		context.slider5_indicator_show = frappe.db.sql("SELECT indicator_show FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].indicator_show
		context.slider5_desc_below = frappe.db.sql("SELECT slider_desc_below FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].slider_desc_below
		context.slider5_width = frappe.db.sql("SELECT slider_width FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].slider_width
		context.slider5_height = frappe.db.sql("SELECT slider_height FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].slider_height
		context.sliders5 = frappe.db.sql("SELECT img_title, img_description, slider_img, img_alt FROM `tabPage Slider` WHERE parent = '"+slider5_parent+"' ORDER BY idx ASC", as_dict=True)
		if int(frappe.db.sql("SELECT man_bootstrap FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].man_bootstrap) == 1:
			context.slider5_left = int(frappe.db.sql("SELECT `left` FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].left)
			context.slider5_middle = int(frappe.db.sql("SELECT `middle` FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].middle)
			context.slider5_right = int(frappe.db.sql("SELECT `right` FROM `tabPage Slideshow` WHERE title = '"+slider5_parent+"'", as_dict=True)[0].right)
		
	#-->card
	context.card5 = False
	context.incl_modal5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Cards":
		context.card5 = True
		card5_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'cards_part5'", as_dict=True)[0].value
		if int(frappe.db.sql("SELECT incl_modal FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].incl_modal) == 1:
			context.incl_modal5 = True
		context.card5_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].mob_qty)
		context.card5_mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].tablet_qty)
		context.card5_tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].desktop_qty)
		context.card5_desktop_qty = 12 / desktop_qty
		context.card5_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].card_bg_color
		context.card5_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card5_parent+"'", as_dict=True)[0].btn_bg_color
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
		context.media_title5 = frappe.db.sql("SELECT media_intro FROM `tabMedia Set` WHERE title = '"+media5_parent+"'", as_dict=True)[0].media_intro
		context.media5_bg_color = frappe.db.sql("SELECT media_bg_color FROM `tabMedia Set` WHERE title = '"+media5_parent+"'", as_dict=True)[0].media_bg_color
		context.medias5 = frappe.db.sql("SELECT img_or_fa, media_fa, media_fa_size, media_img, media_img_size, media_img, subtitle, title, medi_align FROM `tabMedia` WHERE parent = '"+media5_parent+"' ORDER BY idx ASC", as_dict=True)
	
	#-->box
	context.box5 = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'layout_part5' AND doctype = 'Main Page Setup'", as_dict=True)[0].value == "Box":
		context.box5 = True
		box5_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'Main Page Setup' AND field = 'box_part5'", as_dict=True)[0].value
		context.boxes5 = frappe.db.sql("SELECT title, fontawesome, content FROM `tabPage Box` WHERE parent = '"+box5_parent+"' ORDER BY idx ASC", as_dict=True)
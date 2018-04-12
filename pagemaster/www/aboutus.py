from __future__ import unicode_literals
import frappe

def get_context(context):
	
	#meta
	#---------------
	context.head_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'head_title' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.head_favicon = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'head_favicon' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.meta_keywords = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'meta_keywords' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.meta_description = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'meta_description' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.meta_page_topic = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'meta_page_topic' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.meta_robots = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'meta_robots' AND doctype = 'Head Settings'", as_dict=True)[0].value
	context.meta_revisit_after = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'meta_revisit_after' AND doctype = 'Head Settings'", as_dict=True)[0].value
	
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
	context.nav_logo = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_logo' AND doctype = 'Navbar'", as_dict=True)[0].value
	
	#footer
	#-------------------
	context.footer = True
	context.footer_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_bg_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.footer_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_txt_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.txt = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'txt' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link_title' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	
	#google analytics
	#-------------------------
	if frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'enable' AND doctype = 'Google Analytics'", as_dict=True)[0].value:
		context.google_enable = int(frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'enable' AND doctype = 'Google Analytics'", as_dict=True)[0].value)
		context.google_id = frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'id' AND doctype = 'Google Analytics'", as_dict=True)[0].value
		
	#timeline
	#-----------------------
	context.timeline = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_timeline' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.timeline = True
		timeline_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'timeline'", as_dict=True)[0].value
		context.timeline_intro = frappe.db.sql("SELECT timeline_intro FROM `tabTimeline Set` WHERE title = '"+timeline_parent+"'", as_dict=True)[0].timeline_intro
		context.timelines = frappe.db.sql("SELECT year, highlight, align FROM `tabTimeline` WHERE parent = '"+timeline_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#cards
	#--------------------------
	context.card = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_cards' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.card = True
		card_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'cards'", as_dict=True)[0].value
		context.card_title = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].mob_qty)
		context.mob_qty = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].tablet_qty)
		context.tablet_qty = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].desktop_qty)
		context.desktop_qty = 12 / desktop_qty
		context.card_bg_color = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].card_bg_color
		context.card_btn_bg_color = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+card_parent+"'", as_dict=True)[0].btn_bg_color
		context.cards = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#partner cards
	#--------------------------
	context.partner_card = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_partner' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.partner_card = True
		partner_card_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'partner_card'", as_dict=True)[0].value
		context.card_titleX = frappe.db.sql("SELECT card_intro FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].card_intro
		mobile_qty = int(frappe.db.sql("SELECT mob_qty FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].mob_qty)
		context.mob_qtyX = 12 / mobile_qty
		tablet_qty = int(frappe.db.sql("SELECT tablet_qty FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].tablet_qty)
		context.tablet_qtyX = 12 / tablet_qty
		desktop_qty = int(frappe.db.sql("SELECT desktop_qty FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].desktop_qty)
		context.desktop_qtyX = 12 / desktop_qty
		context.card_bg_colorX = frappe.db.sql("SELECT card_bg_color FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].card_bg_color
		context.card_btn_bg_colorX = frappe.db.sql("SELECT btn_bg_color FROM `tabPage Card Set` WHERE title = '"+partner_card_parent+"'", as_dict=True)[0].btn_bg_color
		context.cardsX = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+partner_card_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#introduction
	context.intro = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'introduction' AND doctype = 'About Us'", as_dict=True)[0].value
	
	#post scriptum
	context.post_scriptum = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'ps' AND doctype = 'About Us'", as_dict=True)[0].value
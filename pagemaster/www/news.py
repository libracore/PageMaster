from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

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
		
	#google analytics
	#-------------------------
	if frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'enable' AND doctype = 'Google Analytics'", as_dict=True)[0].value:
		context.google_enable = int(frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'enable' AND doctype = 'Google Analytics'", as_dict=True)[0].value)
		context.google_id = frappe.db.sql("SELECT value FROM `tabSingles` WHERE field = 'id' AND doctype = 'Google Analytics'", as_dict=True)[0].value
		
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
	
	#blog general
	context.blog_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'blog_title' AND doctype = 'Blog Settings'", as_dict=True)[0].value
	
	#blog categories
	context.categories = frappe.get_all('Blog Category', filters={'published': '1'}, fields=['title'])
	
	#blog posts
	context.posts = frappe.get_list('Blog Post', fields=['title', 'blog_category', 'blogger', 'published_on', 'blog_intro', 'prev_img'], filters={'published': '1'}, order_by='published_on desc', limit_page_length=None, ignore_permissions=True)
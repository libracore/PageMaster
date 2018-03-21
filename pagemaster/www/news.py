from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

def get_context(context):
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
	
	#blog general
	context.blog_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'blog_title' AND doctype = 'Blog Settings'", as_dict=True)[0].value
	
	#blog categories
	context.categories = frappe.get_all('Blog Category', filters={'published': '1'}, fields=['title'])
	
	#blog posts
	#context.posts = frappe.get_all('Blog Post', filters={'published': '1'}, fields=['title', 'blog_category', 'blogger', 'published_on', 'blog_intro'])
	context.posts = frappe.get_list('Blog Post', fields=['title', 'blog_category', 'blogger', 'published_on', 'blog_intro'], filters={'published': '1'}, order_by='published_on desc', limit_page_length=None, ignore_permissions=True)
	#context.older_posts = frappe.get_list('Blog Post', fields=['title', 'blog_category', 'blogger', 'published_on', 'blog_intro'], filters={'published': '1'}, order_by='published_on', limit_start=3, ignore_permissions=True)
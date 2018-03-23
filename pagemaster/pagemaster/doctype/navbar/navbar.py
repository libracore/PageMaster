# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Navbar(Document):
	pass
	
@frappe.whitelist()
def updateValues(doctype, name, field, value):
	frappe.db.set_value(doctype, name, field, value, update_modified=False)

@frappe.whitelist()
def deleteOldNavLinks(docparent):
	frappe.db.sql("DELETE FROM `tabNavbar Item` WHERE parent = '"+docparent+"'")
	
@frappe.whitelist()
def insertNewNavLinks(docparent, idx, link, title):
	doc = frappe.new_doc("Navbar Item")
	doc.parent = docparent
	doc.parentfield = "navlinks"
	doc.idx = idx
	doc.link = link
	doc.title = title
	doc.docstatus = 0
	doc.parenttype = "PageMaster Page"
	doc.insert()
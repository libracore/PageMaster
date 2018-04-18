# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import get_comment_list
from frappe import _

base_template_path = "www/auto_generator/libra_auto_base.html"

class PageMasterBlogPost(WebsiteGenerator):
	def get_context(self, context):
		context.comment_list = get_comment_list(self.doctype, self.name)
		if not context.comment_list:
			context.comment_text = _('No comments yet')
		else:
			if(len(context.comment_list)) == 1:
				context.comment_text = _('1 comment')
			else:
				context.comment_text = _('{0} comments').format(len(context.comment_list))
				
		context.user = frappe.session.user
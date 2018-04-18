// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('PageMaster Blog Post', {
	validate: function(frm) {
		if (cur_frm.doc.title) {
			cur_frm.set_value('route', "news/"+cur_frm.doc.title);
		}
	}
});

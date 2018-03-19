// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Page Slideshow', {
	validate: function(frm) {
		if (frm.doc.man_bootstrap == 1) {
			if (frm.doc.left + frm.doc.middle + frm.doc.right != 12) {
				frappe.msgprint('<img src="/assets/pagemaster/images/max12.png"><br><p>Please correct the columns!</p>', "Check the columns quantity!");
				frappe.validated = false;
			}
		}
	}
});

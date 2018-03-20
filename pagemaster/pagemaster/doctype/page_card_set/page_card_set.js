// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Page Card Set', {
	validate: function(frm) {
		if (frm.doc.mob_qty == "5"||frm.doc.mob_qty == "7"||frm.doc.mob_qty == "8"||frm.doc.mob_qty == "9"||frm.doc.mob_qty == "10"||frm.doc.mob_qty == "11") {
			frappe.msgprint('Allowed values for mobile columns quantity are just:<br><ul><li>1 to 4</li><li>6</li><li>12</li></ul>', "Check the columns quantity!");
			frappe.validated = false;
		}
		if (frm.doc.tablet_qty == "5"||frm.doc.tablet_qty == "7"||frm.doc.tablet_qty == "8"||frm.doc.tablet_qty == "9"||frm.doc.tablet_qty == "10"||frm.doc.tablet_qty == "11") {
			frappe.msgprint('Allowed values for tablet columns quantity are just:<br><ul><li>1 to 4</li><li>6</li><li>12</li></ul>', "Check the columns quantity!");
			frappe.validated = false;
		}
		if (frm.doc.desktop_qty == "5"||frm.doc.desktop_qty == "7"||frm.doc.desktop_qty == "8"||frm.doc.desktop_qty == "9"||frm.doc.desktop_qty == "10"||frm.doc.desktop_qty == "11") {
			frappe.msgprint('Allowed values for desktop columns quantity are just:<br><ul><li>1 to 4</li><li>6</li><li>12</li></ul>', "Check the columns quantity!");
			frappe.validated = false;
		}
	}
});

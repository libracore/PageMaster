// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Page Box Set', {
	refresh: function(frm) {
		var newValue = (parseInt(frm.doc.box_height) - 10);
		frm.set_value('p_height', newValue);
	}
});

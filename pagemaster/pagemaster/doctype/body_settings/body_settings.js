// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Body Settings', {
	refresh: function(frm) {
		frm.add_custom_button(__("Update Subpages"),
			function() {
				getAllSubpages(frm);
				frappe.show_alert('All Subpages are updated', 5);
			}
		);
	}
});

function getAllSubpages(frm) {
	frappe.call({
		"method": "frappe.client.get_list",
		"args": {
			"doctype": "PageMaster Page",
			"fields": ['name', 'bg_color', 'bg_img']
		},
		"callback": function(response) {
			var docs = response.message;
			updateAllRecords(frm, docs);
		}
	});
}

function updateAllRecords(frm, docs) {
	for (var i = 0; i < docs.length; i++) {
		for (doc_field in docs[i]) {
			if (doc_field != "name") {
				if (frm.doc[doc_field]) {
					console.log("update von: "+doc_field+" als "+ frm.doc[doc_field]);
					frappe.call({
						method: "pagemaster.pagemaster.doctype.head_settings.head_settings.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: frm.doc[doc_field]
						}
					});
				} else {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.pagemaster_footer.pagemaster_footer.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: ""
						}
					});
				}
			}
		}
	}
}
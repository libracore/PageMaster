// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Head Settings', {
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
			"fields": ['name', 'head_title', 'meta_keywords', 'meta_description', 'meta_page_topic', 'meta_robots', 'meta_revisit_after', 'head_favicon']
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
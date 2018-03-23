// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('PageMaster Footer', {
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
			"fields": ['name', 'footer_bg_color', 'footer_txt_color', 'footer_txt', 'footer_link_title', 'footer_link']
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
				
			if (doc_field == "name") {
			} else if (doc_field == "footer_txt") {
				if (frm.doc["txt"]) {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.pagemaster_footer.pagemaster_footer.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: frm.doc["txt"]
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
			} else if (doc_field == "footer_link_title") {
				if (frm.doc["link_title"]) {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.pagemaster_footer.pagemaster_footer.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: frm.doc["link_title"]
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
			} else if (doc_field == "footer_link") {
				if (frm.doc["link"]) {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.pagemaster_footer.pagemaster_footer.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: frm.doc["link"]
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
			} else {
				if (frm.doc[doc_field]) {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.pagemaster_footer.pagemaster_footer.updateValues",
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
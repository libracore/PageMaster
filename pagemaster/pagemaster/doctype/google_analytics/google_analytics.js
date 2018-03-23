// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Google Analytics', {
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
			"fields": ['name', 'google_enable', 'google_id']
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
				if (doc_field == "google_enable") {
					if (frm.doc["enable"] == 0||frm.doc["enable"] == 1) {
						frappe.call({
							method: "pagemaster.pagemaster.doctype.google_analytics.google_analytics.updateValues",
							args: {
								doctype: "PageMaster Page",
								name: docs[i].name,
								field: doc_field,
								value: frm.doc["enable"]
							}
						});
					} else {
						frappe.call({
							method: "pagemaster.pagemaster.doctype.google_analytics.google_analytics.updateValues",
							args: {
								doctype: "PageMaster Page",
								name: docs[i].name,
								field: doc_field,
								value: 0
							}
						});
					}
				} else if (doc_field == "google_id") {
					if (frm.doc["id"]) {
						frappe.call({
							method: "pagemaster.pagemaster.doctype.google_analytics.google_analytics.updateValues",
							args: {
								doctype: "PageMaster Page",
								name: docs[i].name,
								field: doc_field,
								value: frm.doc["id"]
							}
						});
					} else {
						frappe.call({
							method: "pagemaster.pagemaster.doctype.google_analytics.google_analytics.updateValues",
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
}
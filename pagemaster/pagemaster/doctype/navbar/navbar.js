// Copyright (c) 2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Navbar', {
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
			"fields": ['name', 'nav_logo', 'nav_bg_color', 'nav_txt_color']
		},
		"callback": function(response) {
			var docs = response.message;
			deleteOldNavLinks(frm, docs);
		}
	});
}

function deleteOldNavLinks(frm, docs) {
	for (var i = 0; i < docs.length; i++) {
		for (doc in docs[i]) {
			try {
				frappe.call({
					method: "pagemaster.pagemaster.doctype.navbar.navbar.deleteOldNavLinks",
					args: {
						docparent: docs[i].name
					}
				});
			} catch (err) {
			  frappe.msgprint(err.message);
			}
		}
	}
	getAllNewNavLinks(frm, docs);
}

function getAllNewNavLinks(frm, docs) {
	frappe.call({
		"method": "frappe.client.get_list",
		"args": {
			"doctype": "Navbar Item",
			"fields": ['link', 'title', 'idx'],
			"order_by": "idx ASC"
		},
		"callback": function(response) {
			var nav_links = response.message;
			insertAllNewNavLinks(frm, docs, nav_links);
		}
	});
}

function insertAllNewNavLinks(frm, docs, nav_links) {
	for (var y = 0; y < docs.length; y++) {
		for (var i = 0; i < nav_links.length; i++) {
			frappe.call({
				method: "pagemaster.pagemaster.doctype.navbar.navbar.insertNewNavLinks",
				args: {
					docparent: docs[y].name,
					idx: nav_links[i].idx,
					link: nav_links[i].link,
					title: nav_links[i].title
				}
			});
		}
	}
	updateAllRecords(frm, docs);
}

function updateAllRecords(frm, docs) {
	for (var i = 0; i < docs.length; i++) {
		for (doc_field in docs[i]) {
			if (doc_field != "name") {
				if (frm.doc[doc_field]) {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.navbar.navbar.updateValues",
						args: {
							doctype: "PageMaster Page",
							name: docs[i].name,
							field: doc_field,
							value: frm.doc[doc_field]
						}
					});
				} else {
					frappe.call({
						method: "pagemaster.pagemaster.doctype.navbar.navbar.updateValues",
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

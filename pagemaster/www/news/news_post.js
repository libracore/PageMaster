$(document).ready(function() {
	var login_required = {{ login_required and 1 or 0 }};

	if (!is_user_logged_in()) {
		$(".login-required, .comment-form-wrapper").toggleClass("hidden");
	}

	var n_comments = $(".comment-row").length;

	if(n_comments) {
		$(".no_comment").toggle(false);
	}
	if(n_comments > 50) {
		$(".add-comment").toggle(false)
			.parent().append("<div class='text-muted'>Comments are closed.</div>")
	}
	$(".add-comment").click(function() {
		$(this).toggle(false);
		$("#comment-form").toggle();
		var full_name = "", user_id = "";
		if(is_user_logged_in()) {
			full_name = getCookie("full_name");
			user_id = getCookie("user_id");
			if(user_id != "Guest") {
				$("[name='comment_by']").val(user_id);
				$("[name='comment_by_fullname']").val(full_name);
			}
		}
		$("#comment-form textarea").val("");
		})

	$("#submit-comment").click(function() {
		var args = {
			comment_by_fullname: $("[name='comment_by_fullname']").val(),
			comment_by: $("[name='comment_by']").val(),
			comment: $("[name='comment']").val(),
			reference_doctype: "{{ reference_doctype or doctype }}",
			reference_name: "{{ reference_name or name }}",
			comment_type: "Comment",
			route: "{{ pathname }}",
		}
		if(!args.comment_by_fullname || !args.comment_by || !args.comment) {
			msgprint("{{ _("All fields are necessary to submit the comment.") }}");
			return false;
		}

		if (args.comment_by!=='Administrator' && !valid_email(args.comment_by)) {
			msgprint("{{ _("Please enter a valid email address.") }}");
			return false;
		}

		call({
			//btn: this,
			//type: "POST",
			method: "frappe.templates.includes.comments.comments.add_comment",
			args: args,
			callback: function(r) {
				if(r.exc) {
					if(r._server_messages)
						msgprint(r._server_messages);
				} else {
					$(r.message).appendTo("#comment-list");
					$(".no-comment, .add-comment").toggle(false);
					$("#comment-form").toggle();
				}
				$(".add-comment").text('{{ _("Add Another Comment") }}');
				$(".add-comment").toggle();
			}
		})

		return false;
	})
});

function is_user_logged_in() {
	var current_user = "{{ user }}";
	if (current_user != "Guest") {
		return true;
	} else {
		return false;
	}
}








function getCookie(name) {
	return getCookies()[name];
}


function getCookies() {
	var c = document.cookie, v = 0, cookies = {};
	if (document.cookie.match(/^\s*\$Version=(?:"1"|1);\s*(.*)/)) {
		c = RegExp.$1;
		v = 1;
	}
	if (v === 0) {
		c.split(/[,;]/).map(function(cookie) {
			var parts = cookie.split(/=/, 2),
				name = decodeURIComponent(parts[0].trimLeft()),
				value = parts.length > 1 ? decodeURIComponent(parts[1].trimRight()) : null;
			if(value && value.charAt(0)==='"') {
				value = value.substr(1, value.length-2);
			}
			cookies[name] = value;
		});
	} else {
		c.match(/(?:^|\s+)([!#$%&'*+\-.0-9A-Z^`a-z|~]+)=([!#$%&'*+\-.0-9A-Z^`a-z|~]*|"(?:[\x20-\x7E\x80\xFF]|\\[\x00-\x7F])*")(?=\s*[,;]|$)/g).map(function($0, $1) {
			var name = $0,
				value = $1.charAt(0) === '"'
						? $1.substr(1, -1).replace(/\\(.)/g, "$1")
						: $1;
			cookies[name] = value;
		});
	}
	return cookies;
}










function msgprint(html, title) {
	if(html.substr(0,1)==="[") html = JSON.parse(html);
	if($.isArray(html)) {
		html = html.join("<hr>");
	}

	return get_modal(title || "Message", html).modal("show");
}

function get_modal(title, body_html) {
	var modal = $('<div class="modal" style="overflow: auto;" tabindex="-1">\
		<div class="modal-dialog">\
			<div class="modal-content">\
				<div class="modal-header">\
					<a type="button" class="close"\
						data-dismiss="modal" aria-hidden="true">&times;</a>\
					<h4 class="modal-title">'+title+'</h4>\
				</div>\
				<div class="modal-body ui-front">'+body_html+'\
				</div>\
			</div>\
		</div>\
		</div>').appendTo(document.body);

	return modal;
}




function valid_email(email) {
	return (email.toLowerCase().search("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")==-1) ? 0 : 1;
}

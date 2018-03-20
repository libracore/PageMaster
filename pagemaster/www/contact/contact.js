// Copyright (c) 2018, libracore GmbH and Contributors

$(document).ready(function() {

	$('.btn-send').off("click").on("click", function() {
		var email = $('[name="email"]').val();
		var message = $('[name="message"]').val();
		var contact_name = $('[name="contact_name"]').val();
		var phone = $('[name="phone"]').val();

		if(!(email && message)) {
			$("#contact-alert").html("{{ _("Please enter both your email and message so that we \
				can get back to you. Thanks!") }}").toggle(true);
			return false;
		}

		if(!validate_email(email)) {
			msgprint("{{ _("Please enter a valid email address so that we can get back.") }}");
			$('[name="email"]').focus();
			return false;
		}
		
		var message_to_send = "Absender: "+email+"<br>Contact Name: "+contact_name+"<br>Phone: "+phone+"<br>Message: "+message;
		var subject_to_send = "New Message from libracore Contact Page";
		$("#contact-alert").toggle(false);
		send_message({
			subject: subject_to_send/*$('[name="subject"]').val()*/,
			sender: email,
			message: message_to_send,
			callback: function(r) {
				if(r.message==="okay") {
					msgprint("{{ _("Thank you for your message") }}");
				} else {
					msgprint("{{ _("There were errors") }}");
					console.log(r.exc);
				}
				$(':input').val('');
			}
		}, this);
		return false;
	});

});

function validate_email(email) {
	return (email.toLowerCase().search("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")==-1) ? 0 : 1;
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

function send_message(opts, btn) {
	return call({
		type: "POST",
		method: "frappe.www.contact.send_message",
		btn: btn,
		args: opts,
		callback: opts.callback
	});
}

function call(opts) {
	// opts = {"method": "PYTHON MODULE STRING", "args": {}, "callback": function(r) {}}
	if (typeof arguments[0]==='string') {
		opts = {
			method: arguments[0],
			args: arguments[1],
			callback: arguments[2]
		}
	}

	prepare_call(opts);
	if(opts.freeze) {
		freeze();
	}
	return $.ajax({
		type: opts.type || "POST",
		url: "/",
		data: opts.args,
		dataType: "json",
		headers: { "X-Frappe-CSRF-Token": frappe.csrf_token },
		statusCode: opts.statusCode || {
			404: function() {
				msgprint(__("Not found"));
			},
			403: function() {
				msgprint(__("Not permitted"));
			},
			200: function(data) {
				if(opts.callback)
					opts.callback(data);
				if(opts.success)
					opts.success(data);
			}
		}
	}).always(function(data) {
		if(opts.freeze) {
			frappe.unfreeze();
		}

		// executed before statusCode functions
		if(data.responseText) {
			try {
				data = JSON.parse(data.responseText);
			} catch (e) {
				data = {};
			}
		}
		process_response(opts, data);
	});
}
	
function prepare_call(opts) {
	if(opts.btn) {
		$(opts.btn).prop("disabled", true);
	}

	if(opts.msg) {
		$(opts.msg).toggle(false);
	}

	if(!opts.args) opts.args = {};

	// method
	if(opts.method) {
		opts.args.cmd = opts.method;
	}

	// stringify
	$.each(opts.args, function(key, val) {
		if(typeof val != "string") {
			opts.args[key] = JSON.stringify(val);
		}
	});

	if(!opts.no_spinner) {
		//NProgress.start();
	}
}
 var freeze_count = 0;
function freeze(msg) {
	// blur
	if(!$('#freeze').length) {
		var freeze = $('<div id="freeze" class="modal-backdrop fade"></div>')
			.appendTo("body");

		freeze.html(repl('<div class="freeze-message-container"><div class="freeze-message">%(msg)s</div></div>',
			{msg: msg || ""}));

		setTimeout(function() {
			freeze.addClass("in");
		}, 1);

	} else {
		$("#freeze").addClass("in");
	}
	freeze_count++;
}

function unfreeze() {
	if(!freeze_count) return; // anything open?
	freeze_count--;
	if(!freeze_count) {
		var freeze = $('#freeze').removeClass("in");
		setTimeout(function() {
			if(!freeze_count) {
				freeze.remove();
			}
		}, 150);
	}
}

function process_response(opts, data) {
	//if(!opts.no_spinner) NProgress.done();

	if(opts.btn) {
		$(opts.btn).prop("disabled", false);
	}

	if (data._server_messages) {
		var server_messages = JSON.parse(data._server_messages || '[]');
		server_messages = $.map(server_messages, function(v) {
			// temp fix for messages sent as dict
			try {
				return JSON.parse(v).message;
			} catch (e) {
				return v;
			}
		}).join('<br>');

		if(opts.error_msg) {
			$(opts.error_msg).html(server_messages).toggle(true);
		} else {
			msgprint(server_messages);
		}
	}

	if(data.exc) {
		// if(opts.btn) {
		// 	$(opts.btn).addClass($(opts.btn).is('button') || $(opts.btn).hasClass('btn') ? "btn-danger" : "text-danger");
		// 	setTimeout(function() { $(opts.btn).removeClass("btn-danger text-danger"); }, 1000);
		// }
		try {
			var err = JSON.parse(data.exc);
			if($.isArray(err)) {
				err = err.join("\n");
			}
			console.error ? console.error(err) : console.log(err);
		} catch(e) {
			console.log(data.exc);
		}

	} else{
		// if(opts.btn) {
		// 	$(opts.btn).addClass($(opts.btn).is('button') || $(opts.btn).hasClass('btn') ? "btn-success" : "text-success");
		// 	setTimeout(function() { $(opts.btn).removeClass("btn-success text-success"); }, 1000);
		// }
	}
	if(opts.msg && data.message) {
		$(opts.msg).html(data.message).toggle(true);
	}

	if(opts.always) {
		opts.always(data);
	}
}
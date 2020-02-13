from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Settings"),
			"items": [
				{
					"type": "doctype",
					"name": "iWhatsapp Settings",
					"description": _("Connect your Whatsapp Business Account to ERPNext to send messages"),
				}
			]
		}
	]

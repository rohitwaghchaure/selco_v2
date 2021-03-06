# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "selco"
app_title = "SELCO"
app_publisher = "SELCO"
app_description = "Selco Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "basawaraj@selco-india.com"
app_license = "MIT"

doc_events = {
    "Issue": {
         "before_insert":"selco.selco.selco_customizations.selco_issue_before_insert",
         "validate": "selco.selco.selco_customizations.selco_issue_validate1"
    },
    "Warranty Claim": {
          "validate": "selco.selco.selco_customizations.selco_warranty_claim_validate"
    },
    "Material Request": {
           "validate":"selco.selco.selco_customizations.selco_material_request_validate",
           "before_insert":"selco.selco.selco_customizations.selco_material_request_before_insert"
    },
    "Purchase Receipt":{
              "before_insert":"selco.selco.selco_customizations.selco_purchase_receipt_before_insert",
              "validate":"selco.selco.selco_customizations.selco_purchase_receipt_validate"
    },
    "Payment Entry":{
              "before_insert":"selco.selco.selco_customizations.selco_payment_entry_before_insert",
              "validate":"selco.selco.selco_customizations.selco_payment_entry_validate"
    },
      "Lead":{
            "before_insert":"selco.selco.selco_customizations.selco_lead_before_insert",
            "validate":"selco.selco.selco_customizations.selco_lead_validate"

      },
      "Customer":{
            "before_insert":"selco.selco.selco_customizations.selco_customer_before_insert",
            "validate":"selco.selco.selco_customizations.selco_customer_validate"
     },
     "Journal Entry":{
             "before_insert":"selco.selco.selco_customizations.selco_journal_entry_before_insert",
             "validate":"selco.selco.selco_customizations.selco_journal_entry_validate"
     },
     "Delivery Note":{
             "before_insert":"selco.selco.selco_customizations.selco_delivery_note_before_insert",
             "validate":"selco.selco.selco_customizations.selco_delivery_note_validates"
     },
     "Sales Invoice":{
             "before_insert":"selco.selco.selco_customizations.selco_sales_invoice_before_insert",
              "validate":"selco.selco.selco_customizations.selco_sales_invoice_validate"
     },
     "Purchase Invoice":{
             "before_insert":"selco.selco.selco_customizations.selco_purchase_invoice_before_insert",
             "validate":"selco.selco.selco_customizations.selco_purchase_invoice_validate"
     },
     "Stock Entry":{
        "before_insert": "selco.selco.selco_customizations.selco_stock_entry_updates",
         "validate": "selco.selco.selco_customizations.selco_stock_entry_validate",
         "before_save": "selco.selco.selco_customizations.selco_stock_entry_updates",
         "on_submit": "selco.selco.selco_customizations.selco_stock_entry_on_submit_updates",
         "on_cancel": "selco.selco.selco_customizationss.selco_stock_entry_on_cancel_updates"
   },
   "Address":{
        "before_insert": "selco.selco.selco_customizations.selco_address_before_insert"
   },
    "Purchase Order":{
            "before_insert":"selco.selco.selco_customizations.selco_purchase_order_before_insert",
             "validate": "selco.selco.selco_customizations.selco_purchase_order_validate"
  }
 }

# scheduler_events = {
#     "all": [
#         "selco.tasks.all"
#     ],
#     "daily": [
#         "selco.tasks.daily"
#     ],
#     "hourly": [
#         "selco.tasks.hourly"
#     ],
#     "weekly": [
#         "selco.tasks.weekly"
#     ]
#     "monthly": [
#         "selco.tasks.monthly"
#     ]
# }
"""
scheduler_events = {
    "daily": [
        'selco.selco.doctype.selco_customizations.selco_customizations.send_birthday_wishes',
        'selco.selco.doctype.selco_customizations.selco_customizations.send_po_reminder'
    ],
    "hourly": [
        "selco.selco.doctype.selco_customizations.selco_customizations.service_call_info"
    ],
}
"""
# Testing
# -------

# before_tests = "selco.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "selco.event.get_events"
# }




# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selco/css/selco.css"
# app_include_js = "/assets/selco/js/selco.js"

# include js, css files in header of web template
# web_include_css = "/assets/selco/css/selco.css"
# web_include_js = "/assets/selco/js/selco.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "selco.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "selco.install.before_install"
# after_install = "selco.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selco.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"selco.tasks.all"
# 	],
# 	"daily": [
# 		"selco.tasks.daily"
# 	],
# 	"hourly": [
# 		"selco.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selco.tasks.weekly"
# 	]
# 	"monthly": [
# 		"selco.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "selco.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "selco.event.get_events"
# }


fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format", "Report", "Workflow", "Role","Workflow State", "Workflow Action"]

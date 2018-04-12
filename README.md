# PageMaster

PageMaster is a [ERPNext](https://www.erpnext.org) App, developed by [libracore GmbH](https://libracore.com), for people who do not have much knowledge of bootstrap, but still want to create nice and simple bootstrap websites in their own [ERPNext-](https://www.erpnext.org)System.

[ERPNext](https://www.erpnext.org) is a global, leading, cloud based open source enterprise resource planning software. [ERPNext](https://www.erpnext.org) is a trademark by Frappé Technologies.

## Features
Easy way to create:
* Landing page
* About-Us page
* Product page (in development)
* Contact page
* Sub-Pages
* Dashboards (in development)

With the well-known modules of bootstrap like:
* Slideshows
* Cards
* Medias
* Timeline
* Box
* ...

...as well as integrated maps from google.

And should a website be created without great effort, without using the existing structure; So this app offers the possibility to create your own template with an embedded Drag & Drop Template Builder [Grapesjs](https://github.com/artf/grapesjs).

### Additional Feature
This app also includes all the features of the [libracore FullSize](https://github.com/libracore/fullsize) tool

## Requirements
Requires an [ERPNext server instance](https://github.com/frappe/erpnext)

## Installation
From the frappe-bench folder, execute:
```
$ bench get-app https://github.com/libracore/pagemaster
$ bench install-app pagemaster
$ chown -R frappe:frappe *
$ bench migrate
$ bench restart
```

## License
GNU Affero General Public License.

PageMaster is developed and maintained by [libracore GmbH](https://libracore.com) and contributors. The copyright is owned by [libracore GmbH](https://libracore.com) and contributors. The software comes as-is without any warranty.

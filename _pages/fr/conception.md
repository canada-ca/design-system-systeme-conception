---
altLangPrefix: design
breadcrumbs:
  - title: "Accueil"
    link: /fr
contentTitle: Concevoir
lang: fr
order: 2
---

<p><b>Chercher des :</b></p>
<ul class="btn-toolbar list-inline" role="toolbar">
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-primary" data-toggle="{'selector': '#behaviours, #components, #design-patterns, #page-layouts, #styles', 'group': '.grouped', 'type': 'on'}">Tout</button>
	</li>
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-default" data-toggle="{'selector': '#behaviours', 'group': '.grouped', 'type': 'on'}">Comportements</button>
	</li>
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-default" data-toggle="{'selector': '#components', 'group': '.grouped', 'type': 'on'}">Composants</button>
	</li>
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-default" data-toggle="{'selector': '#design-patterns', 'group': '.grouped', 'type': 'on'}">Modèles de conception</button>
	</li>
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-default" data-toggle="{'selector': '#page-layouts', 'group': '.grouped', 'type': 'on'}">Mises en page</button>
	</li>
	<li class="btn-group">
		<button type="button" class="wb-toggle btn btn-default" data-toggle="{'selector': '#styles', 'group': '.grouped', 'type': 'on'}">Styles</button>
	</li>
</ul>
<div class="wb-filter">
	<section id="behaviours" class="grouped">
		<h3>Comportements</h3>
		<ul class="list-unstyled row">
			{% for behaviours in site.lib_behaviours %}
			<li class="col-md-3">
				<div class="panel panel-default">
					<header class="panel-heading">
						<h5 class="panel-title">Comportement</h5>
					</header>
					<div class="panel-body">
						<p><a class="stretched-link" href="{{ behaviours.url | relative_url }}">{{ behaviours.contentTitle }}</a></p>
						<p class="small">{{ behaviours.description }}</p>
					</div>
				</div>
			</li>
			{% endfor %}
		</ul>
	</section>
	<section id="components" class="grouped">
		<h3>Composants</h3>
		<ul class="list-unstyled row">
			{% for components in site.lib_components %}
			<li class="col-md-3">
				<div class="panel panel-default">
					<header class="panel-heading">
						<h5 class="panel-title">Composant</h5>
					</header>
					<div class="panel-body">
						<p><a class="stretched-link" href="{{ components.url | relative_url }}">{{ components.contentTitle }}</a></p>
						<p class="small">{{ components.description }}</p>
					</div>
				</div>
			</li>
			{% endfor %}
		</ul>
	</section>
	<section id="design-patterns" class="grouped">
		<h3>Modèle de conception</h3>
		<ul class="list-unstyled row">
			{% for design-patterns in site.lib_design_patterns %}
			<li class="col-md-3">
				<div class="panel panel-default">
					<header class="panel-heading">
						<h5 class="panel-title">Modèle de conception</h5>
					</header>
					<div class="panel-body">
						<p><a class="stretched-link" href="{{ design-patterns.url | relative_url }}">{{ design-patterns.contentTitle }}</a></p>
						<p class="small">{{ design-patterns.description }}</p>
					</div>
				</div>
			</li>
			{% endfor %}
		</ul>
	</section>
	<section id="page-layouts" class="grouped">
		<h3>Mises en page</h3>
		<ul class="list-unstyled row">
			{% for page-layouts in site.lib_page_layouts %}
			<li class="col-md-3">
				<div class="panel panel-default">
					<header class="panel-heading">
						<h5 class="panel-title">Mise en page</h5>
					</header>
					<div class="panel-body">
						<p><a class="stretched-link" href="{{ page-layouts.url | relative_url }}">{{ page-layouts.contentTitle }}</a></p>
						<p class="small">{{ page-layouts.description }}</p>
					</div>
				</div>
			</li>
			{% endfor %}
		</ul>
	</section>
	<section id="styles" class="grouped">
		<h3>Styles</h3>
		<ul class="list-unstyled row">
			{% for styles in site.lib_styles %}
			<li class="col-md-3">
				<div class="panel panel-default">
					<header class="panel-heading">
						<h5 class="panel-title">Style</h5>
					</header>
					<div class="panel-body">
						<p><a class="stretched-link" href="{{ styles.url | relative_url }}">{{ styles.contentTitle }}</a></p>
						<p class="small">{{ styles.description }}</p>
					</div>
				</div>
			</li>
			{% endfor %}
		</ul>
	</section>
</div>

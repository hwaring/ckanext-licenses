'''
plugin.py for the aggregator theme
'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import ckan.lib.helpers as h

class LicenseClass(plugins.SingletonPlugin):
    
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
    
    def before_map(self, m):
        
	# This sets up a route for the license plugin. The format goes as follows
	#'
	# m.connect('route_alias', 'url', controller='path.to.controller:ProperController',
	# action='function_to_call', ckan_icon='relevant_icon')
	m.connect('ckanadmin_licenses', '/ckan-admin/licenses',
                    controller='ckanext.licenses.controller:LicenseController',
                    action='add', ckan_icon='edit')
	return m

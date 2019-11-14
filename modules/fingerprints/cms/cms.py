import drupal
import joomla
import wordpress
import magento

def Cms(content):
	return (
		drupal.Drupal().run(content),
		joomla.Joomla().run(content),
		wordpress.Wordpress().run(content),
		magento.Magento().run(content)
		)	

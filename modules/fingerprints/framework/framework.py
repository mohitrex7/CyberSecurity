

import cakephp
import cherrypy
import django
import flask
import fuelphp
import grails
import larvel
import mvc
import nette
import phalcon
import rails
import symfony
import yii
import zend 

def Framework(headers,content):
	return (
		cakephp.Cakephp().run(headers),
		cherrypy.Cherrypy().run(headers),
		django.Django().run(headers),
		flask.Flask().run(headers),
		fuelphp.Fuelphp().run(headers,content),
		grails.Grails().run(headers),
		larvel.Larvel().run(headers),
		mvc.Mvc().run(headers),
		nette.Nette().run(headers),
		phalcon.Phalcon().run(headers),
		rails.Rails().run(headers),
		symfony.Symfony().run(headers),
		yii.Yii().run(headers,content),
		zend.Zend().run(headers)
		)

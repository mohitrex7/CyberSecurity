


import asp
import java
import php	
import python
import ruby
import perl

def Lang(content,headers):
	return (
		asp.Asp().run(content,headers),
		java.Java().run(content,headers),
		php.Php().run(content,headers),
		perl.Perl().run(content,headers),
		python.Python().run(content,headers),
		ruby.Ruby().run(content,headers)
		)

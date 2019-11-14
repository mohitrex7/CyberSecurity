from colors import Colors

class Output:

	r = Colors().red(0) 
	g = Colors().green(0)
	y = Colors().yellow(0)
	b = Colors().blue(0)
	w = Colors().white(0)
	e = Colors().end()

	def plus(self,String):
		print ('{}[+]{} {}{}{}'.format(
			Output.g,
			Output.e,
			Output.w,
			String,
			Output.e)
		)
	
	def less(self,String):
		print ('{}[-]{} {}{}{}'.format(
			Output.r,
			Output.e,
			Output.w,
			String,
			Output.e)
		)

	def test(self,String):
		print ('{}[i]{} {}{}{}'.format(
			Output.b,
			Output.e,
			Output.w,
			String,
			Output.e)
		)
	
	def info(self,String):
		print ('{}[i]{} {}{}{}'.format(
			Output.y,
			Output.e,
			Output.w,
			String,
			Output.e)
		)

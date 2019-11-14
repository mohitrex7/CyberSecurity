

import bsd
import linux
import mac
import solaris
import unix 
import windows

def Os(headers):
	return (
		bsd.Bsd().run(headers),
		windows.Windows().run(headers),
		linux.Linux().run(headers),
		solaris.Solaris().run(headers),
		unix.Unix().run(headers),
		mac.Mac().run(headers)
		)

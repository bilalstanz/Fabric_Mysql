
import fabric

from pprint import pprint
c = fabric.connection.Connection('what')
pprint(c.run())

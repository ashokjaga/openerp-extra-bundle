from turbogears import expose
from turbogears import controllers
import cherrypy

from erpcomparator import rpc
from erpcomparator import common

class Documents(controllers.Controller):
    
    @expose(template="erpcomparator.subcontrollers.templates.documents")
    def index(self):
        msg = "This is Documents....."
        userinfo = cherrypy.session.get('user_info', '')
        
        return dict(msg=msg, userinfo=userinfo)
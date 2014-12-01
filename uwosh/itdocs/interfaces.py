from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

#from uwosh.timeslot import timeslotMessageFactory as _


class ISetupDocument(Interface):
    pass

class IBusinessRequirementsDocument(Interface):
    pass

class IQueryInstructions(Interface):
    pass

class IWorkRequestType(Interface):
    pass
    
class IMeetingNotes(Interface):
    pass
    
class IComponentInstruction(Interface):
    pass

class IProjectMigrationRequest(Interface):
    pass

class ISystemInstruction(Interface):
    pass

class IRunInstruction(Interface):
    pass

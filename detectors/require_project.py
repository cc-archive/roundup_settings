from roundup.exceptions import Reject

def check_project(db, cl, id, newdata):

    # Fail if:
    #   no project is assigned
    #   we try to set the project to None

    if newdata.has_key('project') and newdata['project'] is not None:
        return

    if id is not None:
        # editing
        if not newdata.has_key('project') and \
               cl.get(id, 'project') is not None:
            return

    raise Reject, "The required field 'project' is missing."


def init(db):

    #db.issue.audit("create", check_project)
    db.issue.audit('set', check_project)
    

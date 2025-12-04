from graphviz import Digraph

# This script generates simple sequence-style diagrams using Graphviz.
# Each diagram is a left-to-right flow with labeled edges for steps.

def sequence_login():
    dot = Digraph(comment='Sequence: Student Login', format='png')
    dot.attr(rankdir='LR', splines='ortho')
    dot.attr('node', shape='box', style='filled', fillcolor='#E8F4FF', fontname='Arial')

    dot.node('Actor', 'Student')
    dot.node('Browser', 'Browser / UI')
    dot.node('View', 'Django View / Controller')
    dot.node('Auth', 'Auth System / DB')
    dot.node('Dashboard', 'Student Dashboard')

    dot.edge('Actor', 'Browser', label='1. Enter credentials')
    dot.edge('Browser', 'View', label='2. POST /login')
    dot.edge('View', 'Auth', label='3. Verify credentials')
    dot.edge('Auth', 'View', label='4. Success / Fail')
    dot.edge('View', 'Browser', label='5. Redirect / Response')
    dot.edge('Browser', 'Dashboard', label='6. Load Dashboard (on success)')

    out = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/sequence_login'
    dot.render(out, cleanup=True)
    print(f'Sequence diagram generated: {out}.png')


def sequence_attendance():
    dot = Digraph(comment='Sequence: Staff marks attendance', format='png')
    dot.attr(rankdir='LR', splines='ortho')
    dot.attr('node', shape='box', style='filled', fillcolor='#E8FFE8', fontname='Arial')

    dot.node('Staff', 'Staff')
    dot.node('UI', 'Browser / UI')
    dot.node('View', 'Attendance View')
    dot.node('SubjectSvc', 'Subject / Course Service')
    dot.node('DB', 'Attendance DB')

    dot.edge('Staff', 'UI', label='1. Open Attendance Module')
    dot.edge('UI', 'View', label='2. Request student list')
    dot.edge('View', 'SubjectSvc', label='3. Fetch subject & session')
    dot.edge('SubjectSvc', 'View', label='4. Return student list')
    dot.edge('View', 'UI', label='5. Render list')
    dot.edge('Staff', 'UI', label='6. Mark present/absent')
    dot.edge('UI', 'View', label='7. Submit attendance')
    dot.edge('View', 'DB', label='8. Save attendance records')
    dot.edge('DB', 'View', label='9. Confirm saved')
    dot.edge('View', 'UI', label='10. Show confirmation')

    out = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/sequence_attendance'
    dot.render(out, cleanup=True)
    print(f'Sequence diagram generated: {out}.png')


def sequence_marks_upload():
    dot = Digraph(comment='Sequence: Staff uploads marks', format='png')
    dot.attr(rankdir='LR', splines='ortho')
    dot.attr('node', shape='box', style='filled', fillcolor='#FFF0E8', fontname='Arial')

    dot.node('Staff', 'Staff')
    dot.node('UI', 'Browser / UI')
    dot.node('View', 'Marks View')
    dot.node('ResultSvc', 'Result Service / Logic')
    dot.node('DB', 'Results DB')

    dot.edge('Staff', 'UI', label='1. Open Marks Module')
    dot.edge('UI', 'View', label='2. Select subject & class')
    dot.edge('View', 'UI', label='3. Show entry form')
    dot.edge('Staff', 'UI', label='4. Enter/Upload marks')
    dot.edge('UI', 'View', label='5. Submit marks')
    dot.edge('View', 'ResultSvc', label='6. Validate & calculate grade')
    dot.edge('ResultSvc', 'DB', label='7. Store marks')
    dot.edge('DB', 'ResultSvc', label='8. Confirm stored')
    dot.edge('ResultSvc', 'View', label='9. Return result status')
    dot.edge('View', 'UI', label='10. Notify staff / students')

    out = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/sequence_marks_upload'
    dot.render(out, cleanup=True)
    print(f'Sequence diagram generated: {out}.png')


def sequence_leave_approval():
    dot = Digraph(comment='Sequence: Leave approval', format='png')
    dot.attr(rankdir='LR', splines='ortho')
    dot.attr('node', shape='box', style='filled', fillcolor='#F0F8FF', fontname='Arial')

    dot.node('Student', 'Student')
    dot.node('UI', 'Browser / UI')
    dot.node('LeaveView', 'Leave View')
    dot.node('HOD', 'HOD/Admin')
    dot.node('DB', 'Leave DB')

    dot.edge('Student', 'UI', label='1. Submit leave form')
    dot.edge('UI', 'LeaveView', label='2. POST leave request')
    dot.edge('LeaveView', 'DB', label='3. Save request')
    dot.edge('DB', 'LeaveView', label='4. Confirm saved')
    dot.edge('LeaveView', 'HOD', label='5. Notify HOD')
    dot.edge('HOD', 'LeaveView', label='6. Approve/Reject')
    dot.edge('LeaveView', 'DB', label='7. Update status')
    dot.edge('DB', 'LeaveView', label='8. Confirm update')
    dot.edge('LeaveView', 'UI', label='9. Notify student')

    out = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/sequence_leave_approval'
    dot.render(out, cleanup=True)
    print(f'Sequence diagram generated: {out}.png')


if __name__ == '__main__':
    sequence_login()
    sequence_attendance()
    sequence_marks_upload()
    sequence_leave_approval()
    print('\nAll sequence diagrams generated.')

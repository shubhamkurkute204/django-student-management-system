from graphviz import Digraph

# Create a new directed graph for DFD
dot = Digraph(comment='Student Management System Data Flow Diagram', format='png')
dot.attr(rankdir='LR', splines='curved', nodesep='0.5', ranksep='1')

# Set default attributes
dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='10')

# External Entities (Circles)
dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue', fontsize='11', fontweight='bold')
dot.node('E2', 'Staff/Teacher', shape='ellipse', fillcolor='lightgreen', fontsize='11', fontweight='bold')
dot.node('E3', 'HOD/Admin', shape='ellipse', fillcolor='lightyellow', fontsize='11', fontweight='bold')

# Processes (Rounded Rectangles - using box shape with rounded style)
dot.node('P1', 'User\nAuthentication\n(1.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P2', 'Attendance\nManagement\n(2.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P3', 'Marks/Results\nManagement\n(3.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P4', 'Course &\nSubject\nManagement\n(4.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P5', 'Leave Request\nManagement\n(5.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P6', 'Feedback &\nComplaint\nSystem\n(6.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P7', 'Notification\nSystem\n(7.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')
dot.node('P8', 'Report\nGeneration\n(8.0)', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='10')

# Data Stores (Parallel lines - using box shape)
dot.node('D1', 'User\nAccounts DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D2', 'Attendance\nData DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D3', 'Marks &\nResults DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D4', 'Course &\nSubject DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D5', 'Leave\nRequests DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D6', 'Feedback &\nComplaints DB', shape='box', fillcolor='#E0E0E0', fontsize='9')
dot.node('D7', 'Notifications\nDB', shape='box', fillcolor='#E0E0E0', fontsize='9')

# Data Flows from External Entities to Processes
# Students flows
dot.edge('E1', 'P1', label='1.1: Login Credentials', fontsize='9')
dot.edge('E1', 'P2', label='2.1: View Attendance', fontsize='9')
dot.edge('E1', 'P3', label='3.1: View Marks', fontsize='9')
dot.edge('E1', 'P5', label='5.1: Submit Leave Request', fontsize='9')
dot.edge('E1', 'P6', label='6.1: Submit Feedback', fontsize='9')

# Staff flows
dot.edge('E2', 'P1', label='1.2: Login Credentials', fontsize='9')
dot.edge('E2', 'P2', label='2.2: Mark Attendance', fontsize='9')
dot.edge('E2', 'P3', label='3.2: Upload Marks', fontsize='9')
dot.edge('E2', 'P4', label='4.2: Manage Subjects', fontsize='9')
dot.edge('E2', 'P5', label='5.2: Approve/Reject Leave', fontsize='9')

# HOD/Admin flows
dot.edge('E3', 'P1', label='1.3: Login Credentials', fontsize='9')
dot.edge('E3', 'P4', label='4.1: Create Courses', fontsize='9')
dot.edge('E3', 'P5', label='5.3: Approve Leave', fontsize='9')
dot.edge('E3', 'P8', label='8.1: Generate Reports', fontsize='9')

# Process to Data Store flows (Read/Write)
# P1: Authentication
dot.edge('P1', 'D1', label='1.3: Write User Profile', fontsize='8')
dot.edge('D1', 'P1', label='1.2: Read User Data', fontsize='8')

# P2: Attendance Management
dot.edge('P2', 'D2', label='2.2: Write/Update Attendance', fontsize='8')
dot.edge('D2', 'P2', label='2.1: Read Attendance', fontsize='8')
dot.edge('P2', 'D4', label='2.3: Read Course/Subject', fontsize='8')

# P3: Marks Management
dot.edge('P3', 'D3', label='3.2: Write/Update Marks', fontsize='8')
dot.edge('D3', 'P3', label='3.1: Read Marks', fontsize='8')
dot.edge('P3', 'D4', label='3.3: Read Subject', fontsize='8')

# P4: Course Management
dot.edge('P4', 'D4', label='4.2: Write/Update Courses', fontsize='8')
dot.edge('D4', 'P4', label='4.1: Read Courses', fontsize='8')

# P5: Leave Management
dot.edge('P5', 'D5', label='5.2: Write/Update Leave', fontsize='8')
dot.edge('D5', 'P5', label='5.1: Read Leave Requests', fontsize='8')

# P6: Feedback System
dot.edge('P6', 'D6', label='6.2: Write/Update Feedback', fontsize='8')
dot.edge('D6', 'P6', label='6.1: Read Feedback', fontsize='8')

# P7: Notification System
dot.edge('P7', 'D7', label='7.2: Write Notification', fontsize='8')
dot.edge('D7', 'P7', label='7.1: Read Notification', fontsize='8')

# P8: Report Generation
dot.edge('P8', 'D2', label='8.2: Read Attendance', fontsize='8')
dot.edge('P8', 'D3', label='8.3: Read Marks', fontsize='8')
dot.edge('P8', 'D1', label='8.4: Read User Data', fontsize='8')

# Inter-process flows
dot.edge('P1', 'P7', label='Notify User', fontsize='8', style='dashed')
dot.edge('P2', 'P7', label='Attendance Alert', fontsize='8', style='dashed')
dot.edge('P5', 'P7', label='Leave Status', fontsize='8', style='dashed')
dot.edge('P6', 'P7', label='Feedback Reply', fontsize='8', style='dashed')

# Outputs back to External Entities
dot.edge('P2', 'E1', label='2.4: Attendance Report', fontsize='8')
dot.edge('P3', 'E1', label='3.4: Marks Report', fontsize='8')
dot.edge('P7', 'E1', label='7.3: Student Notifications', fontsize='8')

dot.edge('P5', 'E2', label='5.4: Leave Status', fontsize='8')
dot.edge('P7', 'E2', label='7.4: Staff Notifications', fontsize='8')

dot.edge('P8', 'E3', label='8.5: Reports', fontsize='8')

# Save the diagram
output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd'
dot.render(output_path, cleanup=True)

print(f"Data Flow Diagram generated successfully: {output_path}.png")

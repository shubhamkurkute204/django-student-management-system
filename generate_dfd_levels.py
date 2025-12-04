from graphviz import Digraph

# =====================================================
# DFD LEVEL 0 - Context Diagram
# =====================================================
def create_dfd_level_0():
    dot = Digraph(comment='DFD Level 0 - Context Diagram', format='png')
    dot.attr(rankdir='TB', splines='curved', nodesep='0.8', ranksep='1.2')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='11')
    
    # Title
    dot.node('title', 'DFD Level 0: Context Diagram', shape='plaintext', fontsize='16', fontweight='bold')
    
    # External Entities
    dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue', fontsize='11', fontweight='bold')
    dot.node('E2', 'Staff/Teacher', shape='ellipse', fillcolor='lightgreen', fontsize='11', fontweight='bold')
    dot.node('E3', 'HOD/Admin', shape='ellipse', fillcolor='lightyellow', fontsize='11', fontweight='bold')
    
    # Main System Process
    dot.node('P0', 'Student Management\nSystem\n(0.0)', shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontsize='12', fontweight='bold')
    
    # Data Flows
    dot.edge('E1', 'P0', label='Login, View Attendance/Marks\nSubmit Leave & Feedback', fontsize='10', fontweight='bold')
    dot.edge('P0', 'E1', label='Attendance, Marks, Notifications\nLeave Status', fontsize='10', fontweight='bold')
    
    dot.edge('E2', 'P0', label='Login, Mark Attendance\nUpload Marks, Manage Courses', fontsize='10', fontweight='bold')
    dot.edge('P0', 'E2', label='Course Info, Leave Status\nNotifications', fontsize='10', fontweight='bold')
    
    dot.edge('E3', 'P0', label='Login, Create Courses\nApprove Requests, Generate Reports', fontsize='10', fontweight='bold')
    dot.edge('P0', 'E3', label='Reports, System Status\nNotifications', fontsize='10', fontweight='bold')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd_level_0'
    dot.render(output_path, cleanup=True)
    print(f"DFD Level 0 generated: {output_path}.png")

# =====================================================
# DFD LEVEL 1 - Main Processes
# =====================================================
def create_dfd_level_1():
    dot = Digraph(comment='DFD Level 1 - Main Processes', format='png')
    dot.attr(rankdir='LR', splines='curved', nodesep='0.5', ranksep='1.5')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='10')
    
    # Title
    dot.node('title', 'DFD Level 1: Main Processes', shape='plaintext', fontsize='16', fontweight='bold')
    
    # External Entities
    dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue')
    dot.node('E2', 'Staff', shape='ellipse', fillcolor='lightgreen')
    dot.node('E3', 'HOD/Admin', shape='ellipse', fillcolor='lightyellow')
    
    # Main Processes
    dot.node('P1', '1.0\nUser\nAuthentication', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    dot.node('P2', '2.0\nAttendance\nTracking', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    dot.node('P3', '3.0\nAcademic\nRecords', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    dot.node('P4', '4.0\nCourse\nManagement', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    dot.node('P5', '5.0\nRequest\nManagement', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    dot.node('P6', '6.0\nNotification\nSystem', shape='box', style='rounded,filled', fillcolor='#FFE4B5')
    
    # Data Stores
    dot.node('D1', 'D1: Users', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D2', 'D2: Attendance', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D3', 'D3: Academic', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D4', 'D4: Courses', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D5', 'D5: Requests', shape='box', fillcolor='#E0E0E0', fontsize='9')
    
    # Flows from Entities to Processes
    dot.edge('E1', 'P1', label='Credentials', fontsize='8')
    dot.edge('E1', 'P2', label='View', fontsize='8')
    dot.edge('E1', 'P3', label='Query', fontsize='8')
    dot.edge('E1', 'P5', label='Submit', fontsize='8')
    
    dot.edge('E2', 'P1', label='Credentials', fontsize='8')
    dot.edge('E2', 'P2', label='Mark', fontsize='8')
    dot.edge('E2', 'P3', label='Update', fontsize='8')
    dot.edge('E2', 'P4', label='Manage', fontsize='8')
    
    dot.edge('E3', 'P1', label='Credentials', fontsize='8')
    dot.edge('E3', 'P4', label='Create', fontsize='8')
    dot.edge('E3', 'P5', label='Approve', fontsize='8')
    
    # Flows from Processes to Entities
    dot.edge('P2', 'E1', label='Report', fontsize='8')
    dot.edge('P3', 'E1', label='Marks', fontsize='8')
    dot.edge('P6', 'E1', label='Alerts', fontsize='8')
    
    dot.edge('P5', 'E2', label='Status', fontsize='8')
    dot.edge('P6', 'E2', label='Alerts', fontsize='8')
    
    dot.edge('P6', 'E3', label='Alerts', fontsize='8')
    
    # Flows between Processes and Data Stores
    dot.edge('P1', 'D1', label='R/W', fontsize='8')
    dot.edge('D1', 'P1', label='Verify', fontsize='8')
    
    dot.edge('P2', 'D2', label='R/W', fontsize='8')
    dot.edge('D2', 'P2', label='Query', fontsize='8')
    
    dot.edge('P3', 'D3', label='R/W', fontsize='8')
    dot.edge('D3', 'P3', label='Query', fontsize='8')
    
    dot.edge('P4', 'D4', label='R/W', fontsize='8')
    dot.edge('D4', 'P4', label='Query', fontsize='8')
    
    dot.edge('P5', 'D5', label='R/W', fontsize='8')
    dot.edge('D5', 'P5', label='Query', fontsize='8')
    
    # Inter-process flows
    dot.edge('P1', 'P6', label='User Info', fontsize='8', style='dashed')
    dot.edge('P2', 'P6', label='Alerts', fontsize='8', style='dashed')
    dot.edge('P3', 'P6', label='Alerts', fontsize='8', style='dashed')
    dot.edge('P5', 'P6', label='Status', fontsize='8', style='dashed')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd_level_1'
    dot.render(output_path, cleanup=True)
    print(f"DFD Level 1 generated: {output_path}.png")

# =====================================================
# DFD LEVEL 2 - Detailed Processes (Breakdown of Process 2 & 3)
# =====================================================
def create_dfd_level_2_attendance():
    dot = Digraph(comment='DFD Level 2 - Attendance System', format='png')
    dot.attr(rankdir='LR', splines='curved', nodesep='0.5', ranksep='1')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='9')
    
    # Title
    dot.node('title', 'DFD Level 2: Attendance System (Process 2.0)', shape='plaintext', fontsize='14', fontweight='bold')
    
    # External Entities
    dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue', fontsize='9')
    dot.node('E2', 'Staff', shape='ellipse', fillcolor='lightgreen', fontsize='9')
    dot.node('E3', 'HOD', shape='ellipse', fillcolor='lightyellow', fontsize='9')
    
    # Sub-processes
    dot.node('P2.1', '2.1\nMark\nAttendance', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P2.2', '2.2\nVerify\nAttendance', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P2.3', '2.3\nGenerate\nAttendance\nReport', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P2.4', '2.4\nSend\nAttendance\nAlert', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    
    # Data Stores
    dot.node('D2', 'D2: Attendance\nRecords', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D4', 'D4: Course\nInfo', shape='box', fillcolor='#E0E0E0', fontsize='9')
    
    # External flows
    dot.edge('E2', 'P2.1', label='Attendance Data', fontsize='8')
    dot.edge('P2.3', 'E1', label='Report', fontsize='8')
    dot.edge('P2.4', 'E1', label='Alert', fontsize='8')
    dot.edge('P2.4', 'E3', label='Alert', fontsize='8')
    
    # Process to Data Store flows
    dot.edge('P2.1', 'D2', label='Store', fontsize='8')
    dot.edge('D2', 'P2.2', label='Query', fontsize='8')
    dot.edge('P2.2', 'D2', label='Validate', fontsize='8')
    dot.edge('D2', 'P2.3', label='Fetch', fontsize='8')
    dot.edge('D4', 'P2.2', label='Get Subject', fontsize='8')
    dot.edge('D4', 'P2.3', label='Get Course', fontsize='8')
    
    # Inter-process flows
    dot.edge('P2.2', 'P2.3', label='Valid Data', fontsize='8', style='dashed')
    dot.edge('P2.3', 'P2.4', label='Report', fontsize='8', style='dashed')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd_level_2_attendance'
    dot.render(output_path, cleanup=True)
    print(f"DFD Level 2 (Attendance) generated: {output_path}.png")

def create_dfd_level_2_academic():
    dot = Digraph(comment='DFD Level 2 - Academic Records', format='png')
    dot.attr(rankdir='LR', splines='curved', nodesep='0.5', ranksep='1')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='9')
    
    # Title
    dot.node('title', 'DFD Level 2: Academic Records (Process 3.0)', shape='plaintext', fontsize='14', fontweight='bold')
    
    # External Entities
    dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue', fontsize='9')
    dot.node('E2', 'Staff', shape='ellipse', fillcolor='lightgreen', fontsize='9')
    dot.node('E3', 'HOD', shape='ellipse', fillcolor='lightyellow', fontsize='9')
    
    # Sub-processes
    dot.node('P3.1', '3.1\nUpload\nMarks', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P3.2', '3.2\nValidate\nMarks', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P3.3', '3.3\nCalculate\nGPA/Result', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P3.4', '3.4\nGenerate\nResult Report', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    
    # Data Stores
    dot.node('D3', 'D3: Academic\nRecords', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D4', 'D4: Course\nSubjects', shape='box', fillcolor='#E0E0E0', fontsize='9')
    
    # External flows
    dot.edge('E2', 'P3.1', label='Exam/Assignment Marks', fontsize='8')
    dot.edge('P3.4', 'E1', label='Result Report', fontsize='8')
    dot.edge('P3.4', 'E3', label='Result Report', fontsize='8')
    
    # Process to Data Store flows
    dot.edge('P3.1', 'D3', label='Store', fontsize='8')
    dot.edge('D3', 'P3.2', label='Query', fontsize='8')
    dot.edge('P3.2', 'D3', label='Validate', fontsize='8')
    dot.edge('D3', 'P3.3', label='Fetch Records', fontsize='8')
    dot.edge('D4', 'P3.3', label='Get Subject Info', fontsize='8')
    dot.edge('D3', 'P3.4', label='Fetch', fontsize='8')
    
    # Inter-process flows
    dot.edge('P3.2', 'P3.3', label='Valid Data', fontsize='8', style='dashed')
    dot.edge('P3.3', 'P3.4', label='Calculated Result', fontsize='8', style='dashed')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd_level_2_academic'
    dot.render(output_path, cleanup=True)
    print(f"DFD Level 2 (Academic) generated: {output_path}.png")

def create_dfd_level_2_requests():
    dot = Digraph(comment='DFD Level 2 - Request Management', format='png')
    dot.attr(rankdir='LR', splines='curved', nodesep='0.5', ranksep='1')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='9')
    
    # Title
    dot.node('title', 'DFD Level 2: Request Management (Process 5.0)', shape='plaintext', fontsize='14', fontweight='bold')
    
    # External Entities
    dot.node('E1', 'Student', shape='ellipse', fillcolor='lightblue', fontsize='9')
    dot.node('E2', 'Staff', shape='ellipse', fillcolor='lightgreen', fontsize='9')
    dot.node('E3', 'HOD', shape='ellipse', fillcolor='lightyellow', fontsize='9')
    
    # Sub-processes
    dot.node('P5.1', '5.1\nSubmit\nRequest', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P5.2', '5.2\nValidate\nRequest', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P5.3', '5.3\nApprove/\nReject', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    dot.node('P5.4', '5.4\nNotify\nStatus', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontsize='9')
    
    # Data Stores
    dot.node('D5', 'D5: Leave\nRequests', shape='box', fillcolor='#E0E0E0', fontsize='9')
    dot.node('D1', 'D1: User\nInfo', shape='box', fillcolor='#E0E0E0', fontsize='9')
    
    # External flows
    dot.edge('E1', 'P5.1', label='Leave Request', fontsize='8')
    dot.edge('E2', 'P5.3', label='Approve/Reject', fontsize='8')
    dot.edge('E3', 'P5.3', label='Approve/Reject', fontsize='8')
    dot.edge('P5.4', 'E1', label='Status', fontsize='8')
    dot.edge('P5.4', 'E2', label='Status', fontsize='8')
    
    # Process to Data Store flows
    dot.edge('P5.1', 'D5', label='Store', fontsize='8')
    dot.edge('D5', 'P5.2', label='Query', fontsize='8')
    dot.edge('P5.2', 'D5', label='Store', fontsize='8')
    dot.edge('D1', 'P5.2', label='User Details', fontsize='8')
    dot.edge('D5', 'P5.3', label='Get Requests', fontsize='8')
    dot.edge('P5.3', 'D5', label='Update Status', fontsize='8')
    dot.edge('D5', 'P5.4', label='Fetch Status', fontsize='8')
    
    # Inter-process flows
    dot.edge('P5.2', 'P5.3', label='Valid Request', fontsize='8', style='dashed')
    dot.edge('P5.3', 'P5.4', label='Decision', fontsize='8', style='dashed')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/dfd_level_2_requests'
    dot.render(output_path, cleanup=True)
    print(f"DFD Level 2 (Requests) generated: {output_path}.png")

# Generate all DFD levels
print("Generating DFD diagrams...")
create_dfd_level_0()
create_dfd_level_1()
create_dfd_level_2_attendance()
create_dfd_level_2_academic()
create_dfd_level_2_requests()
print("\nAll DFD diagrams generated successfully!")

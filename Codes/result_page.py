#BISMILLAHIR RAHMANIR RAHIM

import operator

def result_by_marks_gpa(demo, student_number, _first, _second):

    t_pass=[]
    t_fail=[]
    t_absent=[]

    for i in range(student_number):

        if demo[i].count(-1)==14:
            t_absent.append(demo[i])

        elif demo[i][-1]==0:
            t_pass.append(demo[i])
        
        else:
            t_fail.append(demo[i])

    t_pass=sorted(t_pass, key=operator.itemgetter(_first, _second), reverse=True)

    for i in range(len(t_pass)):
        t_pass[i].append(i+1)
    
    t_fail=sorted(t_fail, key=operator.itemgetter(-3), reverse=True)
    t_fail=sorted(t_fail, key=operator.itemgetter(-1))

    for i in range(len(t_fail)):
        t_fail[i].append(i+len(t_pass)+1)

    for i in range(len(t_absent)):
        t_absent[i].append(-1)

    t_student=t_pass+t_fail+t_absent

    t_student=sorted(t_student, key=operator.itemgetter(0))

    return t_student


def review_of_students(demo, student_number):

    t_pass=[]
    t_fail=[]
    t_absent=[]

    for i in range(student_number):

        if demo[i][-1]==-1:
            t_absent.append(demo[i])

        else:
            if demo[i][-2]==0:
                t_pass.append(demo[i])
        
            else:
                t_fail.append(demo[i])

    t=[len(t_pass), len(t_fail), len(t_absent)]
    return t
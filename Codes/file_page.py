#BISMILLAHIR RAHMANIR RAHIM

import os
import pdfkit as pdf
import PyPDF2 

def intro_file(inst, exam, clss, sec):

    f=open('Additionals/result_sheet1.html', 'w')

    f.write('''
<html>

    <body>

        <h2>
            <p align='center'>
                <b>
    ''')

    f.write(inst)

    f.write('''
                </b>
            </p>
        </h2>

       <h3>
            <p align="center">
                <b>
    ''')

    f.write(exam)

    f.write('''
                </b>
            </p>
        </h3>

        <h4>
            <p align="center">Class: 
    ''')

    f.write(clss)
        
    f.write(''', Section: ''')
        
    f.write(sec)
    
    f.write('''
            </p>

        </h4>
    ''')

    f.close()

def result_file(demo, number_of_students,  _start, total, page_no, choose):

    if choose!=1:

        page_name='Additionals/result_sheet'+str(page_no)+'.html'
        f=open(page_name, 'w')

        f.write('''
<html>

    <body>
    ''')

    else:
        page_name='Additionals/result_sheet1.html'
        f=open(page_name, 'a')

    f.write('''
        <table border='1'>
            <tr>
                <th style='width: 120px'>Roll</th>
                <th style='width: 450px' >Name</th>
                <th style='width: 120px'>New Position</th>
                <th style='width: 150px'>Total</th>
                <th style='width: 150px'>GPA</th>
                <th style='width: 120px'>Fail</th>
            </tr>
        ''')

    for i in range(min(total, number_of_students-_start)):

        f.write('''
            <tr>
                <td style='text-align: center'>
        ''')
        f.write(str(demo[i+_start][0]))
        
        f.write('''
                </td>
                <td style='text-align: center'>
        ''')
        
        f.write(demo[i+_start][1])

        f.write('''
                </td>
                <td style='text-align: center'>
        ''')

        if demo[i+_start][-1]!=-1:
            f.write(str(demo[i+_start][-1]))

        else:
            f.write('Absent')

        f.write('''
                </td>
                <td style='text-align: center'>
        ''')

        if demo[i+_start][-1]!=-1:
            f.write(str(demo[i+_start][-4]))

        else:
            f.write('')
        
        f.write('''
                </td>
                <td style='text-align: center'>
        ''')

        if demo[i+_start][-1]!=-1:
            f.write(str(demo[i][-3]))
        
        else:
            f.write('')
        
        f.write('''
                </td>
                <td style='text-align: center'>
        ''')
        
        if demo[i+_start][-1]!=-1:
            if(demo[i+_start][-2])!=0:
                f.write(str(demo[i+_start][-2]))
            
            else:
                f.write('')
        
        else:
            f.write('')
        f.write('''
            </td>
            </tr>
        ''')

    f.write('''
        </table>

    </body>

</html>
        ''')

    f.close()

    total_pages=[0, 42, 89, 136, 183, 200]

    for i in range(len(total_pages)):
        if total_pages[i]>number_of_students:

            p_name='Additionals/result_sheet'+str(i+1)+'.html'
            pg_name='Outputs/Result Sheet '+str(i+1)+'.pdf'

            if os.path.exists(p_name):
                os.remove(p_name)

            if os.path.exists(pg_name):
                os.remove(pg_name)

    page_name='Additionals/result_sheet'+str(page_no)+'.html'
    PageName='Outputs/Result Sheet '+str(page_no)+'.pdf'

    pdf.from_file(page_name, PageName)
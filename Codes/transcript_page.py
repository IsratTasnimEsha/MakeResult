#BISMILLAHIR RAHMANIR RAHIM

import os
import pdfkit as pdf
import PyPDF2 

def transcript_file(inst, exam, clss, sec, demo, number_of_students, subject_name, net_mark):


    for i in range(number_of_students):

        if demo[i][-1]==-1:

            p_name='Additionals/Roll '+str(i+1)+'.html'
            pg_name='Outputs/Roll '+str(i+1)+'.pdf'

            if os.path.exists(p_name):
                os.remove(p_name)
            
            if os.path.exists(pg_name):
                os.remove(pg_name)

            
        else:

            page='Additionals/Roll '+str(demo[i][0])+'.html'

            f=open(page, 'w')

            f.write('''
<html>

    <head>
        <style>
            body{
                background-color: #00284d;
                color: white
            }
        </style>
    </head>
    <body>
      
                    
                    <h1>
                        <br>
                        <p align ='center'>
            ''')

            f.write(inst)

            f.write('''
                       </p>
                    </h1>
                    
                    <h2>
                        <p align ='center'>        
            ''')

            f.write(exam)

            f.write('''
                        </p>
                    </h2>

                    <u>
                        <p align ='center'>ACADEMIC TRANSCRIPT</p>
                    </u>

                    <p>Name Of Student: 
            ''')

            f.write(demo[i][1])

            f.write('''
                    </p>

                    <p>Roll: 
            ''')

            f.write(str(demo[i][0]))

            f.write('''
                    </p>
                    
                    <p>Class: 
            ''')

            f.write(clss)

            f.write('''
                    </p>
                    
                    <p>Section: 
            ''')

            f.write(sec)

            f.write('''
                    </p>

                    <table border="1">
                        <tr>
                            <th style="width: 400px">Names Of Subjects</th>
                            <th style="width: 100px">Total Marks</th>
                            <th style="width: 100px">Obtained Marks</th>
                            <th style="width: 135px">Net Marks</th>
                            <th style="width: 135px">GPA</th>
                            <th style="width: 135px">Position</th>
                        </tr>
            ''')

            f.write('''
                        <tr>

                            <td>
            ''')

            f.write(subject_name[0])

            f.write('''
                            </td>
                            
                            <td style='text-align: center'>
            ''')

            if(net_mark[0]==''):
                f.write('100')

            else:
                f.write(net_mark[0])

            f.write('''
                           </td>

                            <td style='text-align: center'>
            ''')

            if demo[i][2]!=-1:
                f.write(str(demo[i][2]))
        
            else:
                f.write('')

            f.write('''
                            </td>

                            <td rowspan='15', style='text-align: center'>
            ''')

            f.write(str(demo[i][-4]))

            f.write('''
                            </td>
                            
                            <td rowspan='15', style='text-align: center'>
            ''')

            f.write(str(demo[i][-3]))

            f.write('''
                            </td>
                            
                            <td rowspan='15', style='text-align: center'>
            ''')

            if demo[i][-1]==1:
                f.write('1st')
            
            elif demo[i][-1]==2:
                f.write('2nd')
            
            elif demo[i][-1]==3:
                f.write('3rd')
            
            else:
                f.write(str(demo[i][-1])+'th')

            f.write('''
                            </td>

                        </tr>
            ''')


            for j in range(1, 13):

                f.write('''
                            <tr>

                                <td>
                ''')

                f.write(subject_name[j])

                f.write('''
                                </td>
                                
                                <td style='text-align: center'>
                ''')

                if(net_mark[j]==''):
                    f.write('100')

                else:
                    f.write(net_mark[j])

                f.write('''
                            </td>

                            <td style='text-align: center'>
                ''')

                if demo[i][j+2]!=-1:
                    f.write(str(demo[i][j+2]))
            
                else:
                    f.write('')

                f.write('''
                            </td>

                        </tr>
                ''')

            f.write('''
                        <tr>

                            <td colspan="3", style='text-align: center'>
                                <b>Additional Subject</b>
                            </td>
                            
                        </tr>

                        <tr>

                            <td style>
            ''')

            f.write(subject_name[13])

            f.write('''
                            </td>
                            
                            <td style='text-align: center'>
            ''')

            if(net_mark[13]==''):
                f.write('100')

            else:
                f.write(net_mark[13])

            f.write('''
                           </td>

                            <td style='text-align: center'>
            ''')

            if demo[i][15]!=-1:
                f.write(str(demo[i][15]))
        
            else:
                f.write('')

            f.write('''
                            </td>
                        
                        </tr>
            ''')


            f.write('''
                    </table>
                    
                    <p>
                        <b>Remark: </b>
                    </p>

                    <p><br><br><br><br><br></p>

                    <p style="text-align: left">
                        Signature of Class Teacher: 
                        <span style="float: right">Signature of Guardian: 
            ''')

            for j in range(20):
                f.write('&nbsp ')

            f.write('''
                        </span>
                    </p>
                
                    <p style="text-align: left">
                        Date:
                        <span style="float: right">Date:
            ''')

            for j in range(20):
                f.write('&nbsp ')

            f.write('''
                         </span>
                    </p>               
                
                    <p><br><br><br></p>

                    <p align="right">______________________</p>
                    <p align="right">Signature of Head Teacher</p>

    </body>  

</html>
            ''')

            f.close()

            page_name='Outputs/Roll '+str(i+1)+'.pdf'

            if os.path.exists(page_name):
                os.remove(page_name)

            pdf.from_file(page, page_name)


        for i in range(number_of_students, 200):

            p1_name='Additionals/Roll '+str(i+1)+'.html'
            pg1_name='Outputs/Roll '+str(i+1)+'.pdf'

            if os.path.exists(p1_name):
                os.remove(p1_name)
            
            if os.path.exists(pg1_name):
                os.remove(pg1_name)
#BISMILLAHIR RAHMANIR RAHIM

from kivymd.app import MDApp
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from PyPDF2 import PdfFileMerger 
import os
from Codes import result_page, file_page, transcript_page


class TwelvethPage(Screen):
    def __init__(self, **kwargs):
        super(TwelvethPage, self).__init__(**kwargs)

        self.box=BoxLayout(orientation='vertical')

        #.........................................................................................1: Part 2.........................................................................................#

        self.b_grid=GridLayout(rows=1,  size_hint=(1, .07), padding=7, spacing=380)

        #.........................................................................................1: Part 2.1.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Class: ')
        self.grid.add_widget(self.input)

        self.c_input=TextInput()
        self.grid.add_widget(self.c_input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.2.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Section: ')
        self.grid.add_widget(self.input)

        self.sec_input=TextInput()
        self.grid.add_widget(self.sec_input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.3.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Total Subjects\n(Except Optional): ', font_size="12sp")
        self.grid.add_widget(self.input)

        self.sub_input=TextInput()
        self.grid.add_widget(self.sub_input)

        self.b_grid.add_widget(self.grid)

        self.box.add_widget(self.b_grid)

        #.........................................................................................2: Part 3.........................................................................................#

        self.s_box=BoxLayout()

        #.........................................................................................2: Part 3.1.........................................................................................#

        self.s_grid1=GridLayout(rows=3, size_hint_x=.07)

        self.s_grid1_1=GridLayout(cols=1)

        self.input=Label()
        self.s_grid1_1.add_widget(self.input)

        self.input=Button(text='Roll', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5))
        self.s_grid1_1.add_widget(self.input)

        self.r_input=[]

        for i in range(5):
            
            self.r_input.append(Button(text=str(i+196), background_color=(0, 128/255, 0, .7)))
            self.s_grid1_1.add_widget(self.r_input[i])

        self.s_grid1.add_widget(self.s_grid1_1)

        self.input=Label(size_hint_y=.3)
        self.s_grid1.add_widget(self.input)

        self.input=Label(size_hint_y=1.5)
        self.s_grid1.add_widget(self.input)

        self.s_box.add_widget(self.s_grid1)

        #.........................................................................................2: Part 3.2........................................................................................#

        self.s_grid2=GridLayout(rows=3, size_hint_x=.25)

        self.s_grid2_1=GridLayout(cols=1)

        self.input=Label()
        self.s_grid2_1.add_widget(self.input)
            
        self.input=Button(text='Name', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, 1))
        self.s_grid2_1.add_widget(self.input)

        self.n_input=[]

        for i in range(5):

            self.n_input.append(TextInput(background_color=(0, 128/255, 0, .6)))
            self.s_grid2_1.add_widget(self.n_input[i])

        self.s_grid2.add_widget(self.s_grid2_1)

        self.input=Label(size_hint_y=.3)
        self.s_grid2.add_widget(self.input)

        self.input=Label(size_hint_y=1.5)
        self.s_grid2.add_widget(self.input)

        self.s_box.add_widget(self.s_grid2)

        #.........................................................................................2: Part 3.3.........................................................................................#

        self.s_grid3=GridLayout(rows=3)

        #.........................................................................................2: Part 3.3.1.........................................................................................#

        self.s_grid3_1=GridLayout(cols=14)

        self.st_input=[]

        for i in range(14):

            if i%14==13:
                self.st_input.append(TextInput(hint_text="Optional", foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .1)))

            else:
                if i%2==0:
                    self.st_input.append(TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .2)))
                    
                else:
                    self.st_input.append(TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, .4)))

            self.s_grid3_1.add_widget(self.st_input[i])

        self .total_input=[]

        for i in range(14):

            if i%14==13:
                self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .3)))

            else:

                if i%2==0:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .4)))

                else:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, 1)))

            self.s_grid3_1.add_widget(self.total_input[i])

        self.t_input=[]

        for i in range(5*14):

            if i%14==13:
                self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+196)), background_color=(192/255, 192/255, 192/255, .5)))
            
            else:

                if i%2==0:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+196)), background_color=(0, 128/255, 128/255, .8)))    

                else:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+196)), background_color=(1, 1, 1, 1)))

            self.s_grid3_1.add_widget(self.t_input[i])

        self.s_grid3.add_widget(self.s_grid3_1)

        #.........................................................................................2: Part 3.3.2.........................................................................................#

        self.s_grid3_2=GridLayout(rows=1, size_hint_y=.3, padding=15, spacing=60)

        #.........................................................................................2: Part 3.3.2.1.........................................................................................#

        self.s_grid3_2_1=GridLayout(rows=1)
        
        self.ns_input=Button(text='No. of students: ')
        self.s_grid3_2_1.add_widget(self.ns_input)

        self.ts_input=TextInput()
        self.s_grid3_2_1.add_widget(self.ts_input)

        self.s_grid3_2.add_widget(self.s_grid3_2_1)

        #.........................................................................................2: Part 3.3.2.2.........................................................................................#

        self.by_input=Button(text='By Marks', on_press=self.position)
        self.s_grid3_2.add_widget(self.by_input)

        #.........................................................................................2: Part 3.3.2.3.........................................................................................#

        self.submit_input=Button(text='Submit', on_press=self.result)
        self.s_grid3_2.add_widget(self.submit_input)

        self.s_grid3.add_widget(self.s_grid3_2)

        #.........................................................................................2: Part 3.3.3.........................................................................................#

        self.s_grid3_3=GridLayout(cols=1, size_hint_y=1.5, padding=11, spacing=15)

        #.........................................................................................2: Part 3.3.3.1.........................................................................................#

        self.a_grid=GridLayout(cols=2)

        self.input=Button(text='Passed: ', background_color=(192/255, 192/255, 192/255, .7))
        self.a_grid.add_widget(self.input)

        self.ps_input=Button()
        self.a_grid.add_widget(self.ps_input)

        self.input=Button(text='Pass Rate: ', background_color=(192/255, 192/255, 192/255, .8))
        self.a_grid.add_widget(self.input)

        self.pps_input=Button()
        self.a_grid.add_widget(self.pps_input)

        self.s_grid3_3.add_widget(self.a_grid)

        #.........................................................................................2: Part 3.3.3.2.........................................................................................#

        self.a_grid=GridLayout(cols=2)

        self.input=Button(text='Failed: ', background_color=(192/255, 192/255, 192/255, .7))
        self.a_grid.add_widget(self.input)

        self.fl_input=Button()
        self.a_grid.add_widget(self.fl_input)

        self.input=Button(text='Fail Rate: ', background_color=(192/255, 192/255, 192/255, .8))
        self.a_grid.add_widget(self.input)

        self.pfl_input=Button()
        self.a_grid.add_widget(self.pfl_input)

        self.s_grid3_3.add_widget(self.a_grid)

        #.........................................................................................2: Part 3.3.3.3.........................................................................................#

        self.a_grid=GridLayout(cols=2)

        self.input=Button(text='Absent: ', background_color=(192/255, 192/255, 192/255, .7))
        self.a_grid.add_widget(self.input)

        self.ab_input=Button()
        self.a_grid.add_widget(self.ab_input)

        self.input=Button(text='Absence Rate: ', background_color=(192/255, 192/255, 192/255, .8))
        self.a_grid.add_widget(self.input)

        self.pab_input=Button()
        self.a_grid.add_widget(self.pab_input)

        self.s_grid3_3.add_widget(self.a_grid)


        self.s_grid3.add_widget(self.s_grid3_3)

        self.s_box.add_widget(self.s_grid3)

        #.........................................................................................2: Part 3.4.........................................................................................#

        self.s_grid4=GridLayout(rows=3, size_hint_x=0.27)

        self.s_grid4_1=GridLayout(cols=3)

        for i in range(2):
            self.input=Label()
            self.s_grid4_1.add_widget(self.input)

        self.p_input=Button(text='By Marks')
        self.s_grid4_1.add_widget(self.p_input)

        self.input=Button(text='Total Marks', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5), on_press=self.totals)
        self.s_grid4_1.add_widget(self.input)
            
        self.input=Button(text='G.P.A', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .7), on_press=self.gpa)
        self.s_grid4_1.add_widget(self.input)

        self.input=Button(text='Position', color=(1, 1, 1), bold=True,  background_color=(128/255, 0, 0, .6))
        self.s_grid4_1.add_widget(self.input)

        self.b_input=[]
        self.to_input=[]
        self.pos_input=[]
        self.k=0
        self.l=0
        self.m=0

        for i in range(3*5):
            if i%3==0:
                self.b_input.append(Button(background_color=(0, 128/255, 0, .7)))
                self.s_grid4_1.add_widget(self.b_input[self.k])
                self.k+=1

            elif i%3==1:
                self.to_input.append(Button(background_color=(0, 128/255, 0,  1)))
                self.s_grid4_1.add_widget(self.to_input[self.l])
                self.l+=1
            
            else:
                self.pos_input.append(Button(background_color=(128/255, 0, 0, 1)))
                self.s_grid4_1.add_widget(self.pos_input[self.m])
                self.m+=1
        
        self.s_grid4.add_widget(self.s_grid4_1)
        
        self.input=Label(size_hint_y=.3)
        self.s_grid4.add_widget(self.input)

        self.input=Label(size_hint_y=1.5)
        self.s_grid4.add_widget(self.input)
    
        self.s_box.add_widget(self.s_grid4)
        
        self.box.add_widget(self.s_box)
        
        #.........................................................................................2: Part 4.........................................................................................#
        
        self.grid=GridLayout(rows=1,  size_hint=(1, .07), padding=10)

        #.........................................................................................2: Part 4.1.........................................................................................#

        self.input=Button(text='Previous', size_hint_x=.2)
        self.input.bind(on_press=self.screen_transition_prev)
        self.grid.add_widget(self.input)

        self.input=Label(text='Page-12', size_hint_x=.2, bold=True)
        self.grid.add_widget(self.input)

        #.........................................................................................2: Part 4.2.........................................................................................#

        self.s_grid=GridLayout(rows=1)

        self.input=Button(text='P1')
        self.input.bind(on_press=self.screen_transition1)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P2')
        self.input.bind(on_press=self.screen_transition2)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P3')
        self.input.bind(on_press=self.screen_transition3)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P4')
        self.input.bind(on_press=self.screen_transition4)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P5')
        self.input.bind(on_press=self.screen_transition5)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P6')
        self.input.bind(on_press=self.screen_transition6)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P7')
        self.input.bind(on_press=self.screen_transition7)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P8')
        self.input.bind(on_press=self.screen_transition8)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P9')
        self.input.bind(on_press=self.screen_transition9)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P10')
        self.input.bind(on_press=self.screen_transition10)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P11')
        self.input.bind(on_press=self.screen_transition11)
        self.s_grid.add_widget(self.input)

        self.input=Button(text='P12')
        self.input.bind(on_press=self.screen_transition12)
        self.s_grid.add_widget(self.input)

        self.grid.add_widget(self.s_grid)

        #.........................................................................................2: Part 4.3.........................................................................................#

        self.input=Label(size_hint_x=.2)
        self.grid.add_widget(self.input)

        self.input=Label(size_hint_x=.2)
        self.grid.add_widget(self.input)

        self.box.add_widget(self.grid)
        
        self.add_widget(self.box)

    #.........................................................................................2: Part 5.........................................................................................#

    def screen_transition_prev(self, *args):
        self.manager.current='eleventh'
    
    def screen_transition1(self, *args):
        self.manager.current='first'

    def screen_transition2(self, *args):
        self.manager.current='second'

    def screen_transition3(self, *args):
        self.manager.current='third'

    def screen_transition4(self, *args):
        self.manager.current='forth'

    def screen_transition5(self, *args):
        self.manager.current='fifth'
    
    def screen_transition6(self, *args):
        self.manager.current='sixth'

    def screen_transition7(self, *args):
        self.manager.current='seventh'

    def screen_transition8(self, *args):
        self.manager.current='eighth'

    def screen_transition9(self, *args):
        self.manager.current='ninth'
    
    def screen_transition10(self, *args):
        self.manager.current='tenth'

    def screen_transition11(self, *args):
        self.manager.current='eleventh'

    def screen_transition12(self, *args):
        self.manager.current='twelveth'


    #.........................................................................................2: Part 6.........................................................................................#

    def totals(self, *args):

        for j in range(5):

            self.total_mark=0

            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                
                if self.mark.isdigit():
                    self.mrk=int(self.mark)
                
                else:
                    self.mrk=-1
                    self.total_mark+=0
                
                if self.mrk!=-1:
                    self.total_mark+=self.mrk

            self.b_input[j].text=str(self.total_mark)

    #.........................................................................................2: Part 7.........................................................................................#

    def gpa(self, *args):

        self.sub=self.sub_input.text
                    
        if self.sub.isdigit():
            self.totalsubs=int(self.sub)
                    
        else:
            self.totalsubs=-1

        self .TotalGPA=[]

        for i in range(14):
            self.mark=self.total_input[i].text
                
            if self.mark.isdigit():
                self.totalgpa=int(self.mark)
                
            else:
                self.totalgpa=100

            self.TotalGPA.append(self.totalgpa)

        
        self.TotalMarks=[]
        
        for j in range(5):
        
            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                    
                if self.mark.isdigit():
                    self.totalmark=int(self.mark)
                    
                else:
                    self.totalmark=-1
                
                self.TotalMarks.append(self.totalmark)
        
        self.g_input=[]

        for j in range(5):

            self.finalGPA=0
            self.pass_count=0

            for i in range(j*14, (j+1)*14):

                self.per_gpa=self.TotalMarks[i]/self. TotalGPA[i%14]

                if i%14!=13:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=5
                        self.pass_count+=1

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=4
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=3.5
                        self.pass_count+=1

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=3
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.4:
                        self.finalGPA+=2
                        self.pass_count+=1

                    elif self.per_gpa>=0.33:
                        self.finalGPA+=1
                        self.pass_count+=1
                    
                    else:
                        self.finalGPA+=0
                
                else:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=3

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=2
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=1.5

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=1

            self.t_GPA=min(5.00, self.finalGPA/self.totalsubs)
                
            if self.pass_count==self.totalsubs:

                self.g_input.append("{:.2f}".format(self.t_GPA))

                self.to_input[j].text=self.g_input[j]

                self.to_input[j].color=(1, 1, 1)
            
            else:

                self.g_input.append("0.00 ("+str(self.totalsubs-self.pass_count)+")")
                
                self.to_input[j].text=self.g_input[j]
                
                self.to_input[j].color=(1, 0, 0) 

    #.........................................................................................2: Part 8.........................................................................................#

    def position(self, *args):
    
        self.pages=['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelveth']

        if self.by_input.text=='By Marks':
            self.by_input.text='By GPA'

            for i in range(12):
                self.manager.get_screen(self.pages[i]).p_input.text='By GPA'
        
        else:
            self.by_input.text='By Marks'

            for i in range(12):
                self.manager.get_screen(self.pages[i]).p_input.text='By Marks'

    #.........................................................................................2: Part 9.........................................................................................#

    def result(self, *args):

        self.manager.current='first'
        
        self.all_info=[]

        self.demo_info1=self.page_problems("first", 15)
        self.demo_info2=self.page_problems("second", 18)
        self.demo_info3=self.page_problems("third", 18)
        self.demo_info4=self.page_problems("forth", 18)
        self.demo_info5=self.page_problems("fifth", 18)
        self.demo_info6=self.page_problems("sixth", 18)
        self.demo_info7=self.page_problems("seventh", 18)
        self.demo_info8=self.page_problems("eighth", 18)
        self.demo_info9=self.page_problems("ninth", 18)
        self.demo_info10=self.page_problems("tenth", 18)
        self.demo_info11=self.page_problems("eleventh", 18)
        self.demo_info12=self.page_problems("twelveth", 5)
        
        for i in range(15):
            self.all_info.append(self.demo_info1[i])

        for i in range(18):
            self.all_info.append(self.demo_info2[i])
        
        for i in range(18):
            self.all_info.append(self.demo_info3[i])
        
        for i in range(18):
            self.all_info.append(self.demo_info4[i])

        for i in range(18):
            self.all_info.append(self.demo_info5[i])

        for i in range(18):
            self.all_info.append(self.demo_info6[i])

        for i in range(18):
            self.all_info.append(self.demo_info7[i])

        for i in range(18):
            self.all_info.append(self.demo_info8[i])

        for i in range(18):
            self.all_info.append(self.demo_info9[i])

        for i in range(18):
            self.all_info.append(self.demo_info10[i])

        for i in range(18):
            self.all_info.append(self.demo_info11[i])

        for i in range(5):
            self.all_info.append(self.demo_info12[i])

        self.no_of=self.ts_input.text

        if self.no_of.isdigit() and (int(self.no_of)>=0 and int(self.no_of)<=200):
            self.no_of_students=int(self.no_of)

        else:
            self.no_of_students=0

        if self.by_input.text=='By Marks':
            self.all_info=result_page.result_by_marks_gpa(self.all_info, self.no_of_students, -3, -2)

        else:
            self.all_info=result_page.result_by_marks_gpa(self.all_info, self.no_of_students, -2, -3)

        '''
        for i in range(len(self.all_info)):
            print(self.all_info[i])
        '''    
        self.review=result_page.review_of_students(self.all_info, self.no_of_students)

        if self.no_of_students!=0:
            
            self.ps_input.text=str(self.review[0])
            self.pps_input.text=str("{:.2f}".format((self.review[0]/self.no_of_students)*100))+'%'

            self.fl_input.text=str(self.review[1])
            self.pfl_input.text=str(("{:.2f}".format((self.review[1]/self.no_of_students)*100)))+'%'

            self.ab_input.text=str(self.review[2])
            self.pab_input.text=str(("{:.2f}".format((self.review[2]/self.no_of_students)*100)))+'%'

        else:

            self.ps_input.text=''
            self.pps_input.text=''

            self.fl_input.text=''
            self.pfl_input.text=''

            self.ab_input.text=''
            self.pab_input.text=''

        self.get_position('first', 15, 0)
        self.get_position('second', 18, 15)
        self.get_position('third', 18, 33)
        self.get_position('forth', 18, 51)
        self.get_position('fifth', 18, 69)
        self.get_position('sixth', 18, 87)
        self.get_position('seventh', 18, 105)
        self.get_position('eighth', 18, 123)
        self.get_position('ninth', 18, 141)
        self.get_position('tenth', 18, 159)
        self.get_position('eleventh', 18, 177)
        self.get_position('twelveth', 5, 195)

        self.inst=self.manager.get_screen('first').ins_input.text
        self.exam=self.manager.get_screen('first').ex_input.text
        self.cls=self.manager.get_screen('first').c_input.text
        self.sec=self.manager.get_screen('first').sec_input.text
        self.clss=''.join([str(i) for i in self.cls])

        if self.no_of_students!=0:

            file_page.intro_file(self.inst, self.exam, self.clss, self.sec)

            file_page.result_file(self.all_info, self.no_of_students, 0, 42, 1, 1)

            if self.no_of_students>42:
                file_page.result_file(self.all_info, self.no_of_students, 42, 47, 2, 2)
            
            if self.no_of_students>89:
                file_page.result_file(self.all_info, self.no_of_students, 89, 47, 3, 2)

            if self.no_of_students>136:
                file_page.result_file(self.all_info, self.no_of_students, 136, 47, 4, 2)

            if self.no_of_students>183:
                file_page.result_file(self.all_info, self.no_of_students, 183, 47, 5, 2)

            self.subject_name=[]
            self.net_mark=[]
            
            for i in range(14):
                self.subject_name.append(self.manager.get_screen('first').st_input[i].text)
                self.net_mark.append(self.manager.get_screen('first').total_input[i].text)

            transcript_page.transcript_file(self.inst, self.exam, self.clss, self.sec, self.all_info, self.no_of_students, self.subject_name, self.net_mark)

    #.........................................................................................2: Part 10.........................................................................................#

    def page_problems(self, page_name, student_no):

        self.demo_info=[]

        for j in range(student_no):

            self.st_info=[]

            self.st_info.append(int(self.manager.get_screen(page_name).r_input[j].text))
            self.st_info.append(self.manager.get_screen(page_name).n_input[j].text)

            for i in range(j*14, ( j+1)*14):
                self.t=self.manager.get_screen(page_name).t_input[i].text

                if self.t.isdigit():
                    self.st_info.append(int(self.t))

                else:
                    self.st_info.append(-1)

            self.b=self.manager.get_screen(page_name).b_input[j].text

            if self.b.isdigit():
                self.st_info.append(int(self.b))

            else:
                self.st_info.append(student_no)

            self.gpa_fail=self.manager.get_screen(page_name).to_input[j].text

            if self.gpa_fail=='':
                self.f_gpa=0.00

                self.sub=self.sub_input.text

                if self.sub.isdigit():
                    self.n_gpa=int(self.sub)

                else:
                    self.n_gpa=14

            else:

                self.g_p_a=[]

                for i in range(4):
                    self.g_p_a.append(self.gpa_fail[i])

                self.f_gpa=''.join(i for i in self.g_p_a)

                self.st_info.append(float(self.f_gpa))

                self.no=[]

                for i in range(5, len(self.gpa_fail)):

                    if self.gpa_fail[i].isdigit():
                        self.no.append(self.gpa_fail[i])

                self.n_gpa=''.join(i for i in self.no)

                if self.n_gpa.isdigit():
                    self.st_info.append(int(self.n_gpa))

                else:
                    self.st_info.append(0)

            self.demo_info.append(self.st_info)

        return self.demo_info

    #.........................................................................................2: Part 11.........................................................................................#
    
    def get_position(self, page_name, page_len, total_others):

        self.len=min(page_len, len(self.all_info)-total_others)

        for i in range(max(0, self.len)):

            if self.all_info[i+total_others][-1]==-1:
                self.manager.get_screen(page_name).pos_input[i].text='Absent'

            elif self.all_info[i+total_others][-1]==1:
                self.manager.get_screen(page_name).pos_input[i].text=str(self.all_info[i+total_others][-1])+'st'

            elif self.all_info[i+total_others][-1]==2:
                self.manager.get_screen(page_name).pos_input[i].text=str(self.all_info[i+total_others][-1])+'nd'

            elif self.all_info[i+total_others][-1]==3:
                self.manager.get_screen(page_name).pos_input[i].text=str(self.all_info[i+total_others][-1])+'rd'  
                         
            else:
                self.manager.get_screen(page_name).pos_input[i].text=str(self.all_info[i+total_others][-1])+'th'
        
        for i in range(max(0, self.len), page_len):
            self.manager.get_screen(page_name).pos_input[i].text=''
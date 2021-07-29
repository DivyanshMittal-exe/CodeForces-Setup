import os
from datetime import date
import string
from shutil import copyfile
from tkinter.constants import W
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser

from logging import root
from tkinter import Button, Checkbutton, Label, Tk, Variable,messagebox,StringVar,Entry,ttk


from requests.sessions import default_headers

win = Tk()
win.title("Setup CP")
win.after(1, lambda: win.focus_force())
contest_var= StringVar()
default_url = "https://codeforces.com/"

def makeTable(contestsListTr):
    
    con_tree = ttk.Treeview(win)
    con_tree['columns'] = ("Name","Start","Length","StTime","RegTime")

    con_tree.column("#0",width=50)
    con_tree.column("Name",minwidth=30)
    con_tree.column("Start",width=120)
    con_tree.column("Length",width=50)
    con_tree.column("StTime",minwidth=30)
    con_tree.column("RegTime",minwidth=30)

    con_tree.heading("#0",text = "Contest",anchor=W)
    con_tree.heading("Name",text = "Name",anchor=W)
    con_tree.heading("Start",text = "Start",anchor=W)
    con_tree.heading("Length",text = "Length",anchor=W)
    con_tree.heading("StTime",text = "",anchor=W)
    con_tree.heading("RegTime",text = "",anchor=W)

    for con in contestsListTr[1:]:
        conNumber = con["data-contestid"]
        conData = con.find_all('td')
        print(bytes(conNumber, 'utf-8'))
        conValues = (conData[0].text[2:-6],
                     conData[2].text.replace('\n','').replace('\r',''),
                     conData[3].text.replace(' ','').replace('\n','').replace('\r',''),
                     conData[4].text.strip("\r").strip("\n").strip(" "),
                     conData[5].text.strip(" ").replace('  ','').replace('\n','').replace('\r',''),
                    )
        
        con_tree.insert(parent='',index='end',iid=conNumber,text=conNumber , values=conValues)

    con_tree.grid(row=1,column=1,padx= 12,pady=10)


def makeSetup(something = 0):
    contest = contest_var.get()
    if contest.isdigit():
        win.destroy()
        ContestSetup(contest=contest)
    elif contest[:-1].isdigit() and contest[-1].isalpha():
        win.destroy()
        qSetup(contest[:-1],contest[-1])
    else:
        MyWord = Label(win , text= "Invalid Code", font=("Arial", 10))
        MyWord.grid(row=5,column=1,pady=10)
    
def qSetup(contest,question):
    question = question.upper()
    today = date.today()
    d4 = today.strftime("%d %b %Y")
    cwd = os.getcwd() 
    folder_name =  contest + question + " " + d4
    tmplate_path = os.path.join(cwd, "Template.cpp") 
    directory = os.path.join(cwd,"Selected Questions")
    if not os.path.exists(directory):
        os.makedirs(directory)
    pth = os.path.join(directory, folder_name) 
    os.makedirs(pth)
    os.chdir(pth)
    
    file_path = os.path.join(pth, question + ".cpp") 
    
    inp_file = open("input.txt", "w")
    out_file = open("output.txt", "w")
    copyfile(tmplate_path, file_path)
    
    
    qURL = default_url + "problemset/problem/" + contest + "/" + question
    webbrowser.open(qURL, new=2)
    html_text  =  requests.get(qURL).text
    
    con_soup = BeautifulSoup(html_text,features="html.parser")
    inps = con_soup.find_all('div',class_="input")
    outs = con_soup.find_all('div',class_="output")
    if len(inps) > 1:
        qfile = open(file_path,"a")
        qfile.write('\n/*\n')
        for index,(inp,out) in enumerate(zip(inps,outs)):
                qfile.write("Case: " + str(index+1) + "\n")
                qfile.write(str(inp.pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
                qfile.write("\n****\n")
                qfile.write(str(out.pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
                qfile.write("\n*********************\n\n")
        qfile.write('\n*/')
    
    inp_file.write(str(inps[0].pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
    out_file.write(str(outs[0].pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", "")) 
            
    os.system("code " +'"' +str(pth) +'/"' )
   
   
    
    
def ContestSetup(contest):
    
    today = date.today()
    d4 = today.strftime("%d %b %Y")
    cwd = os.getcwd()  

    folder_name =  contest + " " + d4
    tmplate_path = os.path.join(cwd, "Template.cpp") 
    path = os.path.join(cwd, folder_name) 
    new_path = path
    path_made = False
    while not path_made:
        try:
            os.mkdir(path)
            path_made = True
        except:
            path += " copy"
    os.chdir(path)
    main_path = os.getcwd()  

    contestURL = default_url + "contest/" + contest
    
    webbrowser.open(contestURL, new=2)
    
    html_text  =  requests.get(contestURL).text
    # print(html_text)
    soup = BeautifulSoup(html_text,features="html.parser")
    contest_table = soup.find('table',class_="problems")
    # print(contest_table)
    contest_problems = contest_table.find_all('td',class_="id")
    for problem in contest_problems:
        problem_number = problem.text.replace(' ','').replace('\n','').replace('\r','')
        problem_path = os.path.join(main_path,problem_number)
        
        # print(problem_path)
        os.mkdir(problem_path)
        os.chdir(problem_path)
        file_path = os.path.join(problem_path, problem_number + ".cpp") 
        inp_file = open("input.txt", "w")
        out_file = open("output.txt", "w")
        copyfile(tmplate_path, file_path)
        link = problem.a['href']
        link = default_url + link
        con_text  =  requests.get(link).text

        con_soup = BeautifulSoup(con_text,features="html.parser")
        inps = con_soup.find_all('div',class_="input")
        outs = con_soup.find_all('div',class_="output")
        if len(inps) > 1:
            qfile = open(file_path,"a")
            qfile.write('\n/*\n')
            for index,(inp,out) in enumerate(zip(inps,outs)):
                    qfile.write("Case: " + str(index+1) + "\n")
                    qfile.write(str(inp.pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
                    qfile.write("\n****\n")
                    qfile.write(str(out.pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
                    qfile.write("\n*********************\n\n")
            qfile.write('\n*/')
        
        inp_file.write(str(inps[0].pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", ""))
        out_file.write(str(outs[0].pre).replace("<br/>", "\n").replace("<pre>", "").replace("</pre>", "")) 

    os.system("code " +'"' +str(new_path) +'/"' )

conListURL = default_url + "contests"

conListText  =  requests.get(conListURL).text

conListsoup = BeautifulSoup(conListText,features="html.parser")
contestListTable = conListsoup.find('table')
contestsListTr = contestListTable.find_all('tr')

makeTable(contestsListTr)



MyWord = Label(win , text= "Enter Contest Number or Question ID", font=("Arial Bold", 14))
MyWord.grid(row=2,column=1,padx= 12,pady=10)
cnts = Entry(win,textvariable = contest_var, font=('calibre',10,'normal'))
cnts.grid(row=3,column=1)
cnts.focus_set()
win.bind('<Return>', makeSetup)
SaveButton = Button(win, text= "Save" , command= makeSetup)
SaveButton.grid(row=4,column=1,pady=10)


win.mainloop()
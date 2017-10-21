from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgBox
import os
import re
import platform

class CFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Label(master, text='폴더 선택 :').grid(row=0, column=0)

        self.entryFolderText = Entry(master)
        self.entryFolderText.grid(row=0, column=1)

        Button(master, text='폴더지정', command=self.clickBtn).grid(row=0, column=2)

        Label(master, text='검색어 :').grid(row=1, column=0)

        self.entrySearchText = Entry(master)
        self.entrySearchText.grid(row=1, column=1)

        Button(master, text='검색', command=self.clickSearchBtn).grid(row=1, column=2)

        self.findFileList = Listbox(master)
        self.findFileList.bind('<Double-Button-1>', self.listItemClick)
        self.findFileList.grid(row=2, columnspan=3, sticky=W+E+S+N)

    def clickBtn(self):
        selectedDir = filedialog.askdirectory()

        self.entryFolderText.delete(0, END)
        self.entryFolderText.insert(0, selectedDir)

    def clickSearchBtn(self):

        userSearchFolder = self.entryFolderText.get()
        userSerachText = self.entrySearchText.get()

        if userSearchFolder and userSerachText:
            self.findFileList.delete(0,END) # list 초기
            self.__fileSearch__(userSearchFolder, userSerachText)
        else:
            msgBox.showerror(title='나 뜨게 하지마라^^', message='두 항목 모두 필수 값임 !!!')

    def listItemClick(self, event):

        evtWidget = event.widget

        selIndex = evtWidget.curselection()[0] # 튜플형태로 리턴됨
        selVal = evtWidget.get(selIndex)

        if platform.system().lower() == 'windows':
            os.startfile(selVal) # 윈도우에서만 정상 작동
        else:
            pTmp = r'open ' + '\'' + selVal + '\''
            os.system(pTmp)

    def __fileSearch__(self, searchDir, searchText=''):
        pattern_exp = re.compile(searchText, re.IGNORECASE)
        if searchDir:
            fileNames = os.listdir(searchDir)
            for fileName in fileNames:
                pathFileName = os.path.join(searchDir, fileName)
                if not os.path.isdir(pathFileName):
                    #print('file Name = ', pathFileName)
                    with open(pathFileName, 'r') as fileContents:
                        sObj = pattern_exp.search(fileContents.read())
                        if sObj:
                            self.findFileList.insert(END, pathFileName)
                        else:
                            msgBox.showinfo(message='데이터를 찾을 수 없습니다')


def main():
    root = Tk()
    root.title('Log File Explore')
    root.geometry('700x500')
    app = CFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
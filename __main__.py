from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
from main_view import Ui_MainWindow
from utils import get_memory_mapped_rows
class HexModdifierTool(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(HexModdifierTool , self).__init__()
        self.setupUi(self)
        self.browseFile1Btn.clicked.connect(lambda : self.choose_file(1))
        self.browseFile2Btn.clicked.connect(lambda : self.choose_file(2))
        self.getDiffBtn.clicked.connect(self.start_analysis)
        self.file1_path = ""
        self.file2_path = ""
        self.file1MemTable.cellClicked.connect(self.cellClickedAt)
        self.show()
        
    def start_analysis(self):
        if os.path.isfile(self.file1_path) and os.path.isfile(self.file2_path):
            self.load_tables()

    def choose_file(self , file_index):
        print(file_index)
        file_path , filter = QFileDialog.getOpenFileName(self, 'OpenFile' , os.getcwd() , "bin(*.bin)")
        if len(file_path) > 0:
            if file_index == 1 :
                self.file1_path = file_path
                self.browseFile1Lin.setText(file_path)
            else:
                self.file2_path = file_path
                self.browseFile2Lin.setText(file_path)
    

    
    def cellClickedAt(self , row , col ):
        if col<8:
            new_col = col + 9 
            self.file1MemTable.item(row , new_col).setSelected(True)
        elif col > 8:
            new_col = col - 9 
            self.file1MemTable.item(row , new_col).setSelected(True)

            


    def load_tables(self ):
        file1_rows = get_memory_mapped_rows(self.file1_path)
        file2_rows = get_memory_mapped_rows(self.file2_path)
        no_of_cols = max(len(file1_rows) , len(file2_rows))
        file1_bigger = True if len(file1_rows) > len(file2_rows)  else False
        self.file1MemTable.clear()
        self.file1MemTable.setRowCount(no_of_cols)
        for index ,row in enumerate(file1_rows):
            for i in range(len(row)):
                self.file1MemTable.setItem( index , i, QTableWidgetItem(row[i]))
            if file1_bigger:
                self.file1MemTable.setItem(index , 8 , QTableWidgetItem(index))

        for index,row in enumerate(file2_rows):
            has_to_compare = False
            if index < len(file1_rows):
                has_to_compare  = True
            for i in range(len(row)):
                col_off = 9+i
                self.file1MemTable.setItem(index , col_off, QTableWidgetItem(row[i]))
                if has_to_compare and row[i] != file1_rows[index][i] :
                    self.file1MemTable.item(index , col_off).setBackground(Qt.red)
            if not file1_bigger:
                self.file1MemTable.setItem(index , 8 , QTableWidgetItem(str("   ")))
                self.file1MemTable.item(index , 8).setBackground(Qt.gray)
        header = self.file1MemTable.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
    
        


app = QApplication([])
window = HexModdifierTool()
app.exec_()
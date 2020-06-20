from pandas import read_excel
import os
from shutil import copyfile
def copyFile(data):
    print("*****    开始copy文件  ******")
    print(len(data))
    for i in range(len(data)):
        source = data.loc[i][0]
        target = data.loc[i][1]
        shell ='copy '+source +" "+target;
        print("复制第 ",i+1," 个文件》》》》》》》 "+source)
        copyfile(source, target)



def readExcel(filepath,fileName):
    print("*****    开始读取文件  ******")
    filepath = os.path.join(filepath, fileName)
    print(filepath)
    if os.path.exists(filepath):
        data = read_excel(filepath,header=None)
        print(data)
        copyFile(data);
    else:
        print("文件不存在："+filepath)


if __name__ == '__main__':
    filepath=input("文件路径：");
    fileName = input("文件名：");
   # path="D:\Program\Python\copyfile"
    #fileName="新建 Microsoft Excel 工作表.xlsx"
    #print(path+fileName);
    readExcel(filepath, fileName)
    os.system("pause")

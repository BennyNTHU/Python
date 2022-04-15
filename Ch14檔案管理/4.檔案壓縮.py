#將檔案壓縮
import zipfile
import glob
import os

'''
fileZip是壓縮檔的物件,代表out.zip
out.zip是壓縮完後的檔名
'w'代表寫入模式,把"要壓縮的檔案"寫入fileZip"物件"
'''
fileZip = zipfile.ZipFile('out.zip', 'w')   #建立壓縮檔

'''
name代表檔案名稱
zipfile.ZIP_DEFLATED是壓縮方法
os.path.basename()會傳回文件名稱
'''
for name in glob.glob('zipIMG/*'):  #遍歷該目錄(資料夾)
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

fileZip.close()

#讀取zip檔案:使用namelist()與infolist()方法

file_list = fileZip.namelist() #以列表列出所以被壓縮的檔案
print(file_list, '\n')

print("檔案名稱      檔案大小(bits)  壓縮後大小(bits)")
for name in fileZip.infolist():
    print(name.filename, ' '*3, name.file_size, ' '*10, name.compress_size)

#解壓縮檔案:利用extractall()

fileUnzip = zipfile.ZipFile('out.zip')
#建立fileUnzip物件,並將資料夾內的out.zip指定給它
fileUnzip.extractall('out')
#out是解壓縮完後的目錄(資料夾)名稱
fileUnzip.close()
#關閉檔案

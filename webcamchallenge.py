import os
import time
import cv2
import dropbox
def abc():
    time.sleep(5)
    vcObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vcObject.read()
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    vcObject.release()
    cv2.destroyAllWindows()

    time.sleep(300)

    vcObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vcObject.read()
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    vcObject.release()
    cv2.destroyAllWindows()
abc()

class TransferData(object):
    def __init__(self,accesstoken):
        self.accesstoken = input("ENTER ACCESS TOKEN > ")
    def transferFiles(self,pathFrom,pathTo):
        dropboxbruh = dropbox.Dropbox(self.accesstoken)
        with open(pathFrom,"rb") as f:
            dropboxbruh.files_upload(f.read(),pathTo)
def main():
    IRDKWHATTOTRANSFER = TransferData(self.accesstoken)
    fileFrom = '/Users/kavishsingh/Desktop/NewPicture1.jpg'
    fileTo = input("ENTER THE FILE PATH TO UPLOAD TO DROPBOX > ")
    IRDKWHATTOTRANSFER.transferFiles(fileFrom,fileTo)

main()
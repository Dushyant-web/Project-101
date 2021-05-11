import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(fileFrom):
            for fileName in files :
                localPath =os.path.join(root,fileName)
                relative_path=os.path.relpath(localPath,fileFrom)
                dropbox_path=os.path.join(fileTo,relative_path)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
def main():
    access_token='sl.AwkSD_4AHNuZjfo_tv1ZV0bCpyo7mpnb74sE7-gJ6oCHhiCcGesv7mQq62CtkmJ0cPCzCvzA5-pXmM_1zrwqEg_YzioVBH0-2pAOcSHfCPti_7jjQbwANRUfUX-k4Qmqqw-0LuU'
    dataTransfer=TransferData(access_token)
    fileFrom=str(input('Enter the folder path to transfer...'))
    fileTo=input('Enter the full path to upload to dropbox')
    dataTransfer.upload_files(fileFrom,fileTo)
    print('Come out of dreamland plz, the file has been moved...')

main()
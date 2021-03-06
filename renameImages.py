import os
from argparse import ArgumentParser

def renameFiles(args):

    i = 0
    fileList = []
    for imageFile in os.listdir(args.folderName):
        if imageFile.endswith('.jpeg') or imageFile.endswith('.jpg') or imageFile.endswith('.png'):
            os.rename(imageFile, args.label + str(i) + '.jpeg')
            fileList.append(args.label + str(i) + '.jpeg')
        i += 1

if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('folderName', required=True, help='Name of folder containing all images of one class.')
    p.add_argument('label', required=True, help='renaming all files to')
    args = p.parse_args()

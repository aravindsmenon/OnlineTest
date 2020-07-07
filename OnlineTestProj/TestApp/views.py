from django.shortcuts import render, redirect
from TestApp.forms import *
from TestApp.models import *
from  django.views.generic import TemplateView
import os,json

class FileTraverse(TemplateView):

    model_name=files
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {}

        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)

                filepath = os.path.abspath(fname)
                print("path:", filepath)


                extension = os.path.splitext(fname)[1]
                print("ext:", extension)

                f=files(filename=fname,path=filepath,extension=extension)
                f.save()


            context["file"] = fname
        return render(request, self.template_name, context)

            # for (dirpath, dirnames, filenames) in os.walk('.'):
        #     print("dir name:",dirnames)
        #     print("file name:", filenames)
        #     for f in filenames:
        #         filename = os.path.join(dirpath, f)
        #         print('FILE :', filename)
        #
        #         filepath = os.path.abspath(filename)
        #         print("path:", filepath)
        #
        #         file_stats = os.stat(filename)
        #         filesize = file_stats.st_size
        #         print("filesize in bytes:", filesize)
        #
        #         extension = os.path.splitext(filename)[1]
        #         print("ext:", extension)
        #

        #         context["path"]=filepath
        #         context["size"]=filesize
        #         context["ext"]=extension
        #
        #         print(context)



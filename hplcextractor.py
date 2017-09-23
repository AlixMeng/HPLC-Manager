__author__ = 'Stephan'
import os, sys, xlsxwriter, pandas
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from datetime import datetime
from collections import OrderedDict


rootdir = "."

class DataPoint:
    def __init__(self):
        self.values = []

    def addname(self, id, name, path):

        self.id = id
        self.name = name
        self.path = path

        try: self.experiment = name.split('-')[1]
        except: self.experiment = "Exp"

        try: self.flask = int(name.split('-')[2])
        except ValueError: self.flask = name.split('-')[2]
        except IndexError: self.flask = str(id) + "-Media"

        try: self.sample = int(name.split('-')[3])
        except: self.sample = 0

    def addmethod(self, method):
        self.method = method

    def addvalue(self, value):
        self.values.append(value)

class Method:
    def __init__(self, name):
        self.name = name
        self.compounds = []

    def addcompound(self, compound):
        self.compounds.append(compound)

class Methodframe:
    def __init__(self, name, compounds):
        self.mainmethodframe = pandas.DataFrame(columns=compounds)
        self.name = name

    def appendframe(self, dpseries):
        self.mainmethodframe = self.mainmethodframe.append(dpseries)

    def sortbyexp(self):
        self.mainmethodframe = self.mainmethodframe.sort_values(['experiment', 'method', 'flask', 'sample'])

    def returnframe(self):
        return self.mainmethodframe

def dfsort(datapoints, methods):
    methodframes = []
    for method in methods:
        xcolumns = ['experiment', 'method', 'flask', 'sample']
        for compound in methods[method].compounds:
            xcolumns.append(compound)
        mainframe = Methodframe(methods[method].name[:30], xcolumns)
        methodframes.append(mainframe)
        for datapoint in datapoints:
            if datapoints[datapoint].method[:30] == methods[method].name[:30]:
                attributes = [datapoints[datapoint].experiment, datapoints[datapoint].method, datapoints[datapoint].flask, datapoints[datapoint].sample]
                for value in datapoints[datapoint].values:
                    attributes.append(value)
                dpseries = pandas.Series(attributes, index=xcolumns, name=datapoints[datapoint].name)
                mainframe.appendframe(dpseries)
        mainframe.sortbyexp()
    return methodframes

def go(rootdir):

    datapoints, methods = extract(rootdir)
    mainframes = dfsort(datapoints,methods)
    writer = pandas.ExcelWriter(os.path.join(rootdir, 'Data ' + datetime.now().strftime('%m-%d-%Y  %Ih%Mm%Ss') + ' .xlsx'), engine='xlsxwriter')
    for frame in mainframes:
        frame.mainmethodframe.to_excel(writer, sheet_name=frame.name)
        experiments = frame.mainmethodframe['flask'].unique()
    writer.save()
    messagebox.showinfo(title="Finished", message='Data extracted to:' + rootdir)
    rootdir = '.'
    del datapoints, methods

def extract(rootdir):

    datapoints = dict()
    methods = dict()
    filecounter = 0

    for root, subFolders, files in os.walk(rootdir):
        if 'Report.TXT' in files:
            filecounter += 1
            datafile = DataPoint()
            a = 0
            switch = 0
            methodswitch = 0
            methodloop = 0

            with open(os.path.join(root, 'Report.TXT'), 'r', encoding='utf-16') as vreport:
                report = vreport.read().splitlines()
                for line in report:
                    if str(line.split(' ', 1)[0]) == "Totals":
                        break

                    if methodloop == 1:
                        methodloop = 0
                        if "Last changed" not in line:
                            method = str(os.path.split(method + line.strip())[1]).split(' ')[0]
                        else:
                            method = str(os.path.split(method)[1]).split(' ')[0]

                        datafile.addmethod(method)

                        if method not in methods:
                            newmethod = Method(method)
                            methodswitch = 1

                    if line.split(' ', 1)[0] == "Sample":
                        samplename = str(line[13:43]).strip()
                        datafile.addname(filecounter, samplename, root)

                    if line.split(' ', 1)[0] in ["Method", "Analysis"]:
                        if "Method Info" not in line:
                            method = line[17:300].strip()
                            methodloop = 1

                    if "[ng/ul]" in line:
                        readloc = int(line.index('[ng/ul]') - 1)
                        switch = 1

                    if "[g/l]" in line:
                        readloc = int(line.index('[g/l]') - 1)
                        switch = 1

                    if switch == 1: a+=1
                    if a >= 3:
                        if methodswitch == 1:
                            newmethod.addcompound(str(line[(readloc+10):(readloc+40)]).strip())

                        value = str(line[readloc:(readloc+10)]).strip()
                        if value == "-":
                            value = 0.0
                        else:
                            value = float(value)
                        datafile.addvalue(value)

            datapoints[samplename + "-" + str(filecounter)] = datafile
            if methodswitch == 1: methods[method] = newmethod
    frames = dfsort(datapoints, methods)
    return frames

##Window definitions (specific size, not resizable, main loop)

def main():

    root = Tk()
    root.resizable(0,0)
    root.geometry("275x150+300+300")

    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
# Name:        ParseNames
# Purpose:
#
# Author:      OAXFARR
#
# Created:     26/02/2015
# Copyright:   (c) OAXFARR 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, zipfile, os, sys, shutil


class Toolbox(object):
    def __init__(self):
        """A toolbox that will use FGDC standards to parse road names into 7 parts."""
        self.label = "ParseNames"
        self.alias = "parsenames"

        # List of tool classes associated with this toolbox
        self.tools = [Standardize]


class Standardize(object):
    def __init__(self):
        """This tool is a wrapper for the ArcToolbox arcpy.StandardizeAddresses_geocoding tool. Instead of having to have a table with addresses, this tool
        accepts a road name and creates the input/output tables in memory. The output will be a 7 part tuple of FGDC road name parts.


        """
        self.label = "Standardize"
        self.description = "Standardize"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        # 0
        param0 = arcpy.Parameter(
            displayName="NAME_FULL",
            name="NAME_FULL",
            datatype="GPString",
            parameterType="Required",
            direction="Input")


        # 1
        param1 = arcpy.Parameter(
            displayName="standardized_names",
            name="standardized_names",
            datatype="GPString",
            parameterType="Derived",
            direction="Output")


        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        arcpy.env.overwriteOutput = True
        gpnamefile = os.path.join(os.path.dirname(__file__), 'gpnamefile.txt')

        in_name = parameters[0].valueAsText


        # wite the file for the input into the Standardize Address tool
        f= open(gpnamefile, 'w')
        f.write('NAME_FULL\n')
        f.write(in_name)
        f.close()

        # Set local variables:
        #input_feature_class = "streets"
        #address_fields = "ID;FULL_STREET_NAME"
        locator_style = "US Standards - Street Name"
        standardized_fields = "PREMOD;PREDIR;PRETYPE;STREETNAME;POSTTYPE;POSTDIR;POSTMOD"
        standardized_feature_class = r"in_memory\standardized"

        arcpy.StandardizeAddresses_geocoding(gpnamefile, "NAME_FULL", locator_style, standardized_fields, standardized_feature_class, "Static")
#["PREMOD","PREDIR","PRETYPE","STREETNAME","POSTTYPE","POSTDIR","POSTMOD"]
        # go get the parsed name out of the table
        with arcpy.da.SearchCursor(standardized_feature_class, ["*"]) as cursor:
            for row in cursor:
                name_parsed = row
                break

        #np = {'name': name_parsed[1:8]}
        #arcpy.AddMessage(str(np))
        parameters[1].value = str(name_parsed[1:8])   # "("PREMOD","PREDIR","PRETYPE","STREETNAME","POSTTYPE","POSTDIR","POSTMOD")"  "(u'', u'', u'', u'Main', u'Street', u'', u'')"

        arcpy.Delete_management("in_memory")

        return


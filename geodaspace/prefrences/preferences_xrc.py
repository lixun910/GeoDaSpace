# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcgsPrefsFrame(wx.Frame):
#!XRCED:begin-block:xrcgsPrefsFrame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcgsPrefsFrame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "gsPrefsFrame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.prefNoteBook = xrc.XRCCTRL(self, "prefNoteBook")
        self.stddev = xrc.XRCCTRL(self, "stddev")
        self.OLSNk = xrc.XRCCTRL(self, "OLSNk")
        self.OLSN = xrc.XRCCTRL(self, "OLSN")
        self.twoSLSNk = xrc.XRCCTRL(self, "twoSLSNk")
        self.twoSLSN = xrc.XRCCTRL(self, "twoSLSN")
        self.GMlagNk = xrc.XRCCTRL(self, "GMlagNk")
        self.GMlagN = xrc.XRCCTRL(self, "GMlagN")
        self.othermodelsN = xrc.XRCCTRL(self, "othermodelsN")
        self.gmm = xrc.XRCCTRL(self, "gmm")
        self.MaxIterationsLabel = xrc.XRCCTRL(self, "MaxIterationsLabel")
        self.MaxIterations = xrc.XRCCTRL(self, "MaxIterations")
        self.StoppingCriterionLabel = xrc.XRCCTRL(self, "StoppingCriterionLabel")
        self.StoppingCriterion = xrc.XRCCTRL(self, "StoppingCriterion")
        self.inferenceOnLambdaLabel = xrc.XRCCTRL(self, "inferenceOnLambdaLabel")
        self.inferenceOnLambda = xrc.XRCCTRL(self, "inferenceOnLambda")
        self.CompInverseLabel = xrc.XRCCTRL(self, "CompInverseLabel")
        self.CompInverse = xrc.XRCCTRL(self, "CompInverse")
        self.Step1cLabel = xrc.XRCCTRL(self, "Step1cLabel")
        self.Step1c = xrc.XRCCTRL(self, "Step1c")
        self.instruments = xrc.XRCCTRL(self, "instruments")
        self.NumSpatialLagsLabel = xrc.XRCCTRL(self, "NumSpatialLagsLabel")
        self.NumSpatialLags = xrc.XRCCTRL(self, "NumSpatialLags")
        self.IncludeLagsofUserInstLabel = xrc.XRCCTRL(self, "IncludeLagsofUserInstLabel")
        self.IncludeLagsofUserInst = xrc.XRCCTRL(self, "IncludeLagsofUserInst")
        self.output = xrc.XRCCTRL(self, "output")
        self.ShowVarCovarMatrixLabel = xrc.XRCCTRL(self, "ShowVarCovarMatrixLabel")
        self.ShowVarCovarMatrix = xrc.XRCCTRL(self, "ShowVarCovarMatrix")
        self.saveValuesResidualsLabel = xrc.XRCCTRL(self, "saveValuesResidualsLabel")
        self.saveValuesResiduals = xrc.XRCCTRL(self, "saveValuesResiduals")
        self.other = xrc.XRCCTRL(self, "other")
        self.OLSdiagnosticsLabel = xrc.XRCCTRL(self, "OLSdiagnosticsLabel")
        self.OLSdiagnostics = xrc.XRCCTRL(self, "OLSdiagnostics")
        self.residualMoran = xrc.XRCCTRL(self, "residualMoran")
        self.numcoresLabel = xrc.XRCCTRL(self, "numcoresLabel")
        self.numcores = xrc.XRCCTRL(self, "numcores")
        self.restoreButton = xrc.XRCCTRL(self, "restoreButton")
        self.cancelButton = xrc.XRCCTRL(self, "cancelButton")
        self.saveButton = xrc.XRCCTRL(self, "saveButton")

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_OLSNk, self.OLSNk)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_OLSN, self.OLSN)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_twoSLSNk, self.twoSLSNk)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_twoSLSN, self.twoSLSN)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_GMlagNk, self.GMlagNk)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiobutton_GMlagN, self.GMlagN)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinctrl_MaxIterations, self.MaxIterations)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_inferenceOnLambda, self.inferenceOnLambda)
        self.Bind(wx.EVT_CHOICE, self.OnChoice_CompInverse, self.CompInverse)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_Step1c, self.Step1c)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinctrl_NumSpatialLags, self.NumSpatialLags)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_IncludeLagsofUserInst, self.IncludeLagsofUserInst)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_ShowVarCovarMatrix, self.ShowVarCovarMatrix)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_saveValuesResiduals, self.saveValuesResiduals)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_OLSdiagnostics, self.OLSdiagnostics)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox_residualMoran, self.residualMoran)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinctrl_numcores, self.numcores)
        self.Bind(wx.EVT_BUTTON, self.OnButton_restoreButton, self.restoreButton)
        self.Bind(wx.EVT_BUTTON, self.OnButton_cancelButton, self.cancelButton)
        self.Bind(wx.EVT_BUTTON, self.OnButton_saveButton, self.saveButton)

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_OLSNk
    def OnRadiobutton_OLSNk(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_OLSNk()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_OLSNk        

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_OLSN
    def OnRadiobutton_OLSN(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_OLSN()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_OLSN        

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_twoSLSNk
    def OnRadiobutton_twoSLSNk(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_twoSLSNk()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_twoSLSNk        

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_twoSLSN
    def OnRadiobutton_twoSLSN(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_twoSLSN()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_twoSLSN        

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_GMlagNk
    def OnRadiobutton_GMlagNk(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_GMlagNk()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_GMlagNk        

#!XRCED:begin-block:xrcgsPrefsFrame.OnRadiobutton_GMlagN
    def OnRadiobutton_GMlagN(self, evt):
        # Replace with event handler code
        print "OnRadiobutton_GMlagN()"
#!XRCED:end-block:xrcgsPrefsFrame.OnRadiobutton_GMlagN        

#!XRCED:begin-block:xrcgsPrefsFrame.OnSpinctrl_MaxIterations
    def OnSpinctrl_MaxIterations(self, evt):
        # Replace with event handler code
        print "OnSpinctrl_MaxIterations()"
#!XRCED:end-block:xrcgsPrefsFrame.OnSpinctrl_MaxIterations        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_inferenceOnLambda
    def OnCheckbox_inferenceOnLambda(self, evt):
        # Replace with event handler code
        print "OnCheckbox_inferenceOnLambda()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_inferenceOnLambda        

#!XRCED:begin-block:xrcgsPrefsFrame.OnChoice_CompInverse
    def OnChoice_CompInverse(self, evt):
        # Replace with event handler code
        print "OnChoice_CompInverse()"
#!XRCED:end-block:xrcgsPrefsFrame.OnChoice_CompInverse        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_Step1c
    def OnCheckbox_Step1c(self, evt):
        # Replace with event handler code
        print "OnCheckbox_Step1c()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_Step1c        

#!XRCED:begin-block:xrcgsPrefsFrame.OnSpinctrl_NumSpatialLags
    def OnSpinctrl_NumSpatialLags(self, evt):
        # Replace with event handler code
        print "OnSpinctrl_NumSpatialLags()"
#!XRCED:end-block:xrcgsPrefsFrame.OnSpinctrl_NumSpatialLags        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_IncludeLagsofUserInst
    def OnCheckbox_IncludeLagsofUserInst(self, evt):
        # Replace with event handler code
        print "OnCheckbox_IncludeLagsofUserInst()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_IncludeLagsofUserInst        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_ShowVarCovarMatrix
    def OnCheckbox_ShowVarCovarMatrix(self, evt):
        # Replace with event handler code
        print "OnCheckbox_ShowVarCovarMatrix()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_ShowVarCovarMatrix        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_saveValuesResiduals
    def OnCheckbox_saveValuesResiduals(self, evt):
        # Replace with event handler code
        print "OnCheckbox_saveValuesResiduals()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_saveValuesResiduals        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_OLSdiagnostics
    def OnCheckbox_OLSdiagnostics(self, evt):
        # Replace with event handler code
        print "OnCheckbox_OLSdiagnostics()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_OLSdiagnostics        

#!XRCED:begin-block:xrcgsPrefsFrame.OnCheckbox_residualMoran
    def OnCheckbox_residualMoran(self, evt):
        # Replace with event handler code
        print "OnCheckbox_residualMoran()"
#!XRCED:end-block:xrcgsPrefsFrame.OnCheckbox_residualMoran        

#!XRCED:begin-block:xrcgsPrefsFrame.OnSpinctrl_numcores
    def OnSpinctrl_numcores(self, evt):
        # Replace with event handler code
        print "OnSpinctrl_numcores()"
#!XRCED:end-block:xrcgsPrefsFrame.OnSpinctrl_numcores        

#!XRCED:begin-block:xrcgsPrefsFrame.OnButton_restoreButton
    def OnButton_restoreButton(self, evt):
        # Replace with event handler code
        print "OnButton_restoreButton()"
#!XRCED:end-block:xrcgsPrefsFrame.OnButton_restoreButton        

#!XRCED:begin-block:xrcgsPrefsFrame.OnButton_cancelButton
    def OnButton_cancelButton(self, evt):
        # Replace with event handler code
        print "OnButton_cancelButton()"
#!XRCED:end-block:xrcgsPrefsFrame.OnButton_cancelButton        

#!XRCED:begin-block:xrcgsPrefsFrame.OnButton_saveButton
    def OnButton_saveButton(self, evt):
        # Replace with event handler code
        print "OnButton_saveButton()"
#!XRCED:end-block:xrcgsPrefsFrame.OnButton_saveButton        




# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    preferences_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxFrame" name="gsPrefsFrame">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxNotebook" name="prefNoteBook">
          <object class="notebookpage">
            <object class="wxPanel" name="stddev">
              <object class="wxBoxSizer">
                <orient>wxVERTICAL</orient>
                <object class="sizeritem">
                  <object class="wxStaticText">
                    <label>Compute Standard Deviation with N or N-K</label>
                    <font>
                      <weight>bold</weight>
                    </font>
                  </object>
                  <flag>wxALL|wxALIGN_CENTRE</flag>
                  <border>15</border>
                </object>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <object class="sizeritem">
                      <object class="wxStaticText"/>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>N-k</label>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>N</label>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>OLS</label>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="OLSNk">
                        <value>1</value>
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="OLSN">
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>2SLS</label>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="twoSLSNk">
                        <style>wxRB_GROUP</style>
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="twoSLSN">
                        <value>1</value>
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>GM-Lag</label>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="GMlagNk">
                        <style>wxRB_GROUP</style>
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="GMlagN">
                        <value>1</value>
                        <XRCED>
                          <events>EVT_RADIOBUTTON</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>All Other Models</label>
                      </object>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxRadioButton" name="othermodelsN">
                        <value>1</value>
                        <style>wxRB_GROUP</style>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <cols>3</cols>
                    <rows>5</rows>
                    <vgap>3</vgap>
                    <hgap>15</hgap>
                  </object>
                  <flag>wxALIGN_CENTRE</flag>
                </object>
              </object>
              <size>650,300</size>
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <label>Std Dev</label>
          </object>
          <object class="notebookpage">
            <object class="wxPanel" name="gmm">
              <object class="wxBoxSizer">
                <orient>wxVERTICAL</orient>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Improved Efficiency</label>
                        <font>
                          <weight>bold</weight>
                        </font>
                      </object>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="MaxIterationsLabel">
                        <label>Maximum Iterations</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxSpinCtrl" name="MaxIterations">
                        <size>100,-1</size>
                        <value>1</value>
                        <min>1</min>
                        <max>999999999</max>
                        <XRCED>
                          <events>EVT_SPINCTRL</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="StoppingCriterionLabel">
                        <label>Stopping Criterion\n(change in lambda)</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxTextCtrl" name="StoppingCriterion">
                        <value>0.00001</value>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Spatial Error Model</label>
                        <font>
                          <weight>bold</weight>
                        </font>
                      </object>
                      <flag>wxTOP</flag>
                      <border>10</border>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="inferenceOnLambdaLabel">
                        <label>Inference on Lambda</label>
                        <tooltip>inferst</tooltip>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="inferenceOnLambda">
                        <checked>1</checked>
                        <tooltip>InferCB</tooltip>
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Heteroskedasticity</label>
                        <font>
                          <weight>bold</weight>
                        </font>
                      </object>
                      <flag>wxTOP</flag>
                      <border>10</border>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="CompInverseLabel">
                        <label>Computation of Inverse</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxChoice" name="CompInverse">
                        <content>
                          <item>Power Expansion</item>
                          <item>True Inverse</item>
                        </content>
                        <XRCED>
                          <events>EVT_CHOICE</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="Step1cLabel">
                        <label>Step 1c from Arraiz et al (2010)</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="Step1c">
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <cols>2</cols>
                    <rows>8</rows>
                    <vgap>5</vgap>
                    <hgap>25</hgap>
                  </object>
                  <flag>wxALIGN_CENTRE</flag>
                </object>
              </object>
              <size>650,300</size>
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <label>GMM</label>
          </object>
          <object class="notebookpage">
            <object class="wxPanel" name="instruments">
              <object class="wxBoxSizer">
                <orient>wxVERTICAL</orient>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <object class="sizeritem">
                      <object class="wxStaticText" name="NumSpatialLagsLabel">
                        <label>Number of Spatial\nLags of Instruments</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxSpinCtrl" name="NumSpatialLags">
                        <value>1</value>
                        <min>1</min>
                        <max>5</max>
                        <XRCED>
                          <events>EVT_SPINCTRL</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="IncludeLagsofUserInstLabel">
                        <label>Include Lags of User-\nSpecified Instruments</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="IncludeLagsofUserInst">
                        <checked>1</checked>
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <cols>2</cols>
                    <rows>2</rows>
                    <vgap>20</vgap>
                    <hgap>10</hgap>
                  </object>
                  <flag>wxALL|wxALIGN_CENTRE</flag>
                  <border>15</border>
                </object>
              </object>
              <size>650,300</size>
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <label>Instruments</label>
          </object>
          <object class="notebookpage">
            <object class="wxPanel" name="output">
              <object class="wxBoxSizer">
                <orient>wxVERTICAL</orient>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <object class="sizeritem">
                      <object class="wxStaticText" name="ShowVarCovarMatrixLabel">
                        <label>Show Variance-\nCovariance Matrix</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="ShowVarCovarMatrix">
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="saveValuesResidualsLabel">
                        <label>Save Predicted Values\nand Residuals</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="saveValuesResiduals">
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <cols>2</cols>
                    <rows>2</rows>
                    <vgap>20</vgap>
                    <hgap>10</hgap>
                  </object>
                  <flag>wxALL|wxALIGN_CENTRE</flag>
                  <border>15</border>
                </object>
              </object>
              <size>650,300</size>
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <label>Output</label>
          </object>
          <object class="notebookpage">
            <object class="wxPanel" name="other">
              <object class="wxBoxSizer">
                <orient>wxVERTICAL</orient>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Diagnostics</label>
                        <font>
                          <weight>bold</weight>
                        </font>
                      </object>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="OLSdiagnosticsLabel">
                        <label>OLS Diagnostics</label>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="OLSdiagnostics">
                        <checked>1</checked>
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Moran's I of the\nResiduals</label>
                      </object>
                      <flag>wxLEFT</flag>
                      <border>10</border>
                    </object>
                    <object class="sizeritem">
                      <object class="wxCheckBox" name="residualMoran">
                        <XRCED>
                          <events>EVT_CHECKBOX</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticText">
                        <label>Computation</label>
                        <font>
                          <weight>bold</weight>
                        </font>
                        <hidden>1</hidden>
                      </object>
                      <flag>wxTOP</flag>
                      <border>15</border>
                    </object>
                    <object class="spacer"/>
                    <object class="sizeritem">
                      <object class="wxStaticText" name="numcoresLabel">
                        <label>Multi-Core</label>
                        <hidden>1</hidden>
                        <XRCED>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                    </object>
                    <object class="sizeritem">
                      <object class="wxSpinCtrl" name="numcores">
                        <value>1</value>
                        <min>1</min>
                        <hidden>1</hidden>
                        <XRCED>
                          <events>EVT_SPINCTRL</events>
                          <assign_var>1</assign_var>
                        </XRCED>
                      </object>
                      <flag>wxALIGN_CENTRE</flag>
                    </object>
                    <cols>2</cols>
                    <rows>5</rows>
                    <vgap>7</vgap>
                    <hgap>25</hgap>
                  </object>
                  <flag>wxALL|wxALIGN_CENTRE</flag>
                  <border>10</border>
                </object>
              </object>
              <size>650,300</size>
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <label>Other</label>
          </object>
          <size>450,300</size>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxButton" name="restoreButton">
              <label>Restore Defaults</label>
              <XRCED>
                <events>EVT_BUTTON</events>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
          </object>
          <object class="spacer">
            <option>1</option>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="cancelButton">
              <label>Cancel</label>
              <XRCED>
                <events>EVT_BUTTON</events>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <flag>wxRIGHT</flag>
            <border>15</border>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="saveButton">
              <label>Save</label>
              <default>1</default>
              <XRCED>
                <events>EVT_BUTTON</events>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxEXPAND</flag>
        <border>15</border>
      </object>
    </object>
    <size>650,400</size>
    <title>GeoDaSpace Preferences</title>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/preferences/preferences_xrc', preferences_xrc)
    __res.Load('memory:XRC/preferences/preferences_xrc')


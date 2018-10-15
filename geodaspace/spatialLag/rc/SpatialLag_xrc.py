# This file was automatically generated by pywxrc, do not edit by hand.
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


class xrcCreateSpatialLag(wx.Dialog):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "CreateSpatialLag")
        self.PostCreate(pre)

        # create attributes for the named items in this container
        self.panel = xrc.XRCCTRL(self, "panel")
        self.dataFile = xrc.XRCCTRL(self, "dataFile")
        self.dataFileWarn = xrc.XRCCTRL(self, "dataFileWarn")
        self.dataFileButton = xrc.XRCCTRL(self, "dataFileButton")
        self.weights = xrc.XRCCTRL(self, "weights")
        self.openWeights = xrc.XRCCTRL(self, "openWeights")
        self.VariablesPeer = xrc.XRCCTRL(self, "VariablesPeer")
        self.fakeVarsChoice = xrc.XRCCTRL(self, "fakeVarsChoice")
        self.cancelButton = xrc.XRCCTRL(self, "cancelButton")
        self.okButton = xrc.XRCCTRL(self, "okButton")


class xrcSpLagVariable(wx.Panel):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "SpLagVariable")
        self.PostCreate(pre)

        # create attributes for the named items in this container
        self.newVarNameCtrl = xrc.XRCCTRL(self, "newVarNameCtrl")
        self.warn = xrc.XRCCTRL(self, "warn")
        self.varsChoice = xrc.XRCCTRL(self, "varsChoice")



# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    SpatialLag_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxDialog" name="CreateSpatialLag">
    <title>Create Spatial Lag</title>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxPanel" name="panel">
          <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
              <object class="wxStaticBoxSizer">
                <label>Data File</label>
                <orient>wxHORIZONTAL</orient>
                <object class="sizeritem">
                  <object class="wxTextCtrl" name="dataFile">
                    <size>75,-1d</size>
                  </object>
                  <option>1</option>
                  <flag>wxALL|wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                  <border>5</border>
                </object>
                <object class="sizeritem">
                  <object class="wxFlexGridSizer">
                    <cols>1</cols>
                    <rows>2</rows>
                    <object class="spacer">
                      <size>20,0</size>
                    </object>
                    <object class="sizeritem">
                      <object class="wxStaticBitmap" name="dataFileWarn">
                        <bitmap stock_id="wxART_WARNING"/>
                        <size>20,20</size>
                        <tooltip>File does not exist, please enter a valid filename.</tooltip>
                      </object>
                      <flag>wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                    </object>
                  </object>
                  <flag>wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                </object>
                <object class="sizeritem">
                  <object class="wxBitmapButton" name="dataFileButton">
                    <bitmap stock_id="wxART_FILE_OPEN"/>
                    <size>15,13d</size>
                    <style>wxBU_AUTODRAW</style>
                  </object>
                  <flag>wxALL|wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                  <border>5</border>
                </object>
              </object>
              <option>0</option>
              <flag>wxALL|wxEXPAND|wxALIGN_CENTRE_HORIZONTAL</flag>
              <border>5</border>
            </object>
            <object class="sizeritem">
              <object class="wxStaticBoxSizer">
                <orient>wxHORIZONTAL</orient>
                <object class="spacer">
                  <size>20,20</size>
                </object>
                <object class="sizeritem">
                  <object class="wxStaticText">
                    <label>W = </label>
                    <style>wxALIGN_CENTRE</style>
                  </object>
                  <option>0</option>
                  <flag>wxTOP|wxBOTTOM</flag>
                  <border>5</border>
                </object>
                <object class="sizeritem">
                  <object class="wxChoice" name="weights">
                    <content/>
                  </object>
                  <option>1</option>
                  <flag>wxTOP|wxBOTTOM|wxEXPAND|wxGROW|wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                  <border>5</border>
                </object>
                <object class="sizeritem">
                  <object class="wxBitmapButton" name="openWeights">
                    <bitmap stock_id="wxART_FILE_OPEN"/>
                    <size>25,25</size>
                  </object>
                  <option>0</option>
                  <flag>wxALL|wxEXPAND</flag>
                  <border>3</border>
                </object>
                <object class="spacer">
                  <size>20,20</size>
                </object>
                <label>Weights</label>
              </object>
              <option>0</option>
              <flag>wxLEFT|wxRIGHT|wxGROW|wxADJUST_MINSIZE</flag>
              <border>5</border>
            </object>
            <object class="sizeritem">
              <object class="wxStaticBoxSizer" name="VPeerContainer">
                <orient>wxVERTICAL</orient>
                <label>Variables</label>
                <object class="sizeritem">
                  <object class="wxBoxSizer">
                    <orient>wxVERTICAL</orient>
                    <object class="sizeritem">
                      <object class="wxPanel" name="VariablesPeer">
                        <size>0,0</size>
                        <style/>
                      </object>
                      <flag>wxALL|wxEXPAND|wxADJUST_MINSIZE</flag>
                    </object>
                  </object>
                </object>
                <object class="sizeritem">
                  <object class="wxBoxSizer">
                    <orient>wxVERTICAL</orient>
                    <object class="sizeritem">
                      <object class="wxPanel" name="">
                        <object class="wxBoxSizer">
                          <orient>wxHORIZONTAL</orient>
                          <object class="sizeritem">
                            <object class="wxGridBagSizer">
                              <object class="sizeritem">
                                <object class="wxFlexGridSizer">
                                  <cols>1</cols>
                                  <rows>0</rows>
                                  <object class="sizeritem">
                                    <object class="wxTextCtrl" name="">
                                      <value/>
                                      <size>93,-1</size>
                                      <font>
                                        <size>14</size>
                                        <style>normal</style>
                                        <weight>normal</weight>
                                        <underlined>0</underlined>
                                        <face>Courier</face>
                                      </font>
                                      <enabled>0</enabled>
                                    </object>
                                    <option>0</option>
                                    <cellpos>0,0</cellpos>
                                  </object>
                                  <object class="spacer">
                                    <size>63,0</size>
                                    <cellpos>1,0</cellpos>
                                  </object>
                                </object>
                                <cellpos>0,0</cellpos>
                              </object>
                              <object class="sizeritem">
                                <object class="wxFlexGridSizer">
                                  <cols>1</cols>
                                  <rows>2</rows>
                                  <object class="sizeritem">
                                    <object class="wxStaticBitmap" name="">
                                      <bitmap stock_id="wxART_WARNING"/>
                                      <size>20,20</size>
                                      <hidden>1</hidden>
                                      <tooltip>This has a tooltip</tooltip>
                                    </object>
                                    <cellpos>0,1</cellpos>
                                    <cellspan/>
                                  </object>
                                  <object class="spacer">
                                    <size>20,0</size>
                                    <cellpos>1,1</cellpos>
                                  </object>
                                </object>
                                <cellpos>0,1</cellpos>
                              </object>
                            </object>
                            <option>0</option>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label> = W *</label>
                            </object>
                            <flag>wxRIGHT</flag>
                          </object>
                          <object class="sizeritem">
                            <object class="wxChoice" name="fakeVarsChoice">
                              <content/>
                            </object>
                            <option>1</option>
                            <flag>wxLEFT|wxRIGHT|wxEXPAND</flag>
                          </object>
                          <object class="spacer">
                            <size>51,20</size>
                            <flag>wxLEFT|wxRIGHT</flag>
                          </object>
                        </object>
                      </object>
                    </object>
                  </object>
                </object>
              </object>
              <option>1</option>
              <flag>wxALL|wxEXPAND|wxGROW</flag>
              <border>5</border>
            </object>
            <object class="sizeritem">
              <object class="wxBoxSizer">
                <orient>wxHORIZONTAL</orient>
                <object class="sizeritem">
                  <object class="wxButton" name="cancelButton">
                    <label>Close</label>
                    <default>0</default>
                    <style/>
                  </object>
                </object>
                <object class="spacer">
                  <size>50,10</size>
                </object>
                <object class="sizeritem">
                  <object class="wxButton" name="okButton">
                    <label>OK</label>
                    <default>1</default>
                  </object>
                </object>
              </object>
              <option>0</option>
              <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
              <border>5</border>
            </object>
          </object>
        </object>
        <option>1</option>
        <flag>wxALL|wxEXPAND|wxADJUST_MINSIZE</flag>
      </object>
    </object>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxRESIZE_BORDER|wxCLOSE_BOX</style>
  </object>
  <object class="wxPanel" name="SpLagVariable">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <object class="wxGridBagSizer">
          <object class="sizeritem">
            <object class="wxFlexGridSizer">
              <cols>1</cols>
              <rows>0</rows>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="newVarNameCtrl">
                  <value>W_var1</value>
                  <size>93,-1</size>
                  <font>
                    <size>14</size>
                    <weight>normal</weight>
                    <underlined>0</underlined>
                    <face>Courier</face>
                  </font>
                </object>
                <option>0</option>
                <cellpos>0,0</cellpos>
              </object>
              <object class="spacer">
                <size>63,0</size>
                <cellpos>1,0</cellpos>
              </object>
            </object>
            <cellpos>0,0</cellpos>
          </object>
          <object class="sizeritem">
            <object class="wxFlexGridSizer">
              <cols>1</cols>
              <rows>2</rows>
              <object class="sizeritem">
                <object class="wxStaticBitmap" name="warn">
                  <bitmap stock_id="wxART_WARNING"/>
                  <size>20,20</size>
                  <hidden>1</hidden>
                  <tooltip>This has a tooltip</tooltip>
                </object>
                <cellpos>0,1</cellpos>
                <cellspan/>
              </object>
              <object class="spacer">
                <size>20,0</size>
                <cellpos>1,1</cellpos>
              </object>
            </object>
            <cellpos>0,1</cellpos>
          </object>
        </object>
        <option>0</option>
      </object>
      <object class="sizeritem">
        <object class="wxStaticText">
          <label> = W *</label>
        </object>
        <flag>wxRIGHT</flag>
      </object>
      <object class="sizeritem">
        <object class="wxChoice" name="varsChoice">
          <content/>
        </object>
        <option>1</option>
        <flag>wxLEFT|wxRIGHT|wxEXPAND</flag>
      </object>
      <object class="spacer">
        <size>51,20</size>
        <flag>wxLEFT|wxRIGHT</flag>
      </object>
    </object>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/SpatialLag/SpatialLag_xrc', SpatialLag_xrc)
    __res.Load('memory:XRC/SpatialLag/SpatialLag_xrc')


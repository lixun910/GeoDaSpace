import os.path
import StringIO
import sys
import traceback
import wx
import geodaspace
from geodaspace import textwindow
from geodaspace.icons import icons
from geodaspace.regression.rc import OGRegression_xrc
from geodaspace import weights
from geodaspace.weights.control import ENABLE_CONTIGUITY_WEIGHTS, \
    ENABLE_DISTANCE_WEIGHTS, ENABLE_KERNEL_WEIGHTS, WEIGHT_TYPES_FILTER, \
    WEIGHT_FILTER_TO_HANDLER
from geodaspace import spatialLag
from geodaspace.preferences import preferencesDialog
import variableTools
import M_regression
import pysal

gear_png = [
    "24 24 232 2 ",
    "   c gray11",
    ".  c #262625",
    "X  c #292927",
    "o  c #3D3C36",
    "O  c #3D3D36",
    "+  c #4B4D52",
    "@  c #4C4C51",
    "#  c #4E4F52",
    "$  c #595A61",
    "%  c #595A62",
    "&  c #5C5C61",
    "*  c #5C5D65",
    "=  c #5C5D66",
    "-  c #5C5E69",
    ";  c #5D5F6A",
    ":  c #5C5E6D",
    ">  c #5D5F6E",
    ",  c #63646C",
    "<  c #64656E",
    "1  c #606274",
    "2  c #646677",
    "3  c #646678",
    "4  c #646679",
    "5  c #6F7174",
    "6  c #757573",
    "7  c #717174",
    "8  c #727274",
    "9  c #72727A",
    "0  c #78797A",
    "q  c #7A7A7E",
    "w  c #6E7181",
    "e  c #6F7182",
    "r  c #6E718C",
    "t  c #767883",
    "y  c #7B7B80",
    "u  c #7D7D82",
    "i  c #7B7C86",
    "p  c #757889",
    "a  c #7C7E88",
    "s  c #717490",
    "d  c #727593",
    "f  c #727695",
    "g  c #7A7D9A",
    "h  c #7B7E9A",
    "j  c #7A7E9D",
    "k  c #7A7F9E",
    "l  c #7B80A2",
    "z  c #7C80A1",
    "x  c #7F84A6",
    "c  c #7F84A7",
    "v  c #828489",
    "b  c #85858B",
    "n  c #8B8B8B",
    "m  c #8D8B8D",
    "M  c #838794",
    "N  c #848895",
    "B  c #8A8B91",
    "V  c #8A8A92",
    "C  c #898A95",
    "Z  c #888A96",
    "A  c #8E8F96",
    "S  c #80849F",
    "D  c #909197",
    "F  c #919197",
    "G  c #9C9D9D",
    "H  c #8185A0",
    "J  c #8186A7",
    "K  c #8388A8",
    "L  c #8489AA",
    "P  c #888CAD",
    "I  c #8E93A0",
    "U  c #9498A7",
    "Y  c #9599A7",
    "T  c #9398A8",
    "R  c #989AA9",
    "E  c #989BA9",
    "W  c #9A9DAA",
    "Q  c #9A9EAA",
    "!  c #9C9EAB",
    "~  c #999EAF",
    "^  c #9094B2",
    "/  c #9194B2",
    "(  c #9095B3",
    ")  c #9397B6",
    "_  c #9398B6",
    "`  c #9599B4",
    "'  c #9498B5",
    "]  c #969AB5",
    "[  c #9599B6",
    "{  c #969AB7",
    "}  c #969BB7",
    "|  c #9A9FBA",
    " . c #9B9FBB",
    ".. c #9EA0AA",
    "X. c #9FA1AD",
    "o. c #9DA1AE",
    "O. c #9BA0B0",
    "+. c #9EA4B5",
    "@. c #9FA4B6",
    "#. c #9DA1BD",
    "$. c #9DA2BD",
    "%. c #9FA3BC",
    "&. c #9FA3BD",
    "*. c #9DA2BE",
    "=. c #9EA3BF",
    "-. c #9FA4BE",
    ";. c #A0A1A3",
    ":. c #A5A5A6",
    ">. c #A5A5A8",
    ",. c #A7A7A9",
    "<. c #A6A6AA",
    "1. c #A8A8AB",
    "2. c #A9A9AD",
    "3. c #AAAAAD",
    "4. c #ACADAD",
    "5. c #A3A6B2",
    "6. c #A4A6B3",
    "7. c #A8A9B3",
    "8. c #AAADB1",
    "9. c #ABADB2",
    "0. c #ACACB3",
    "q. c #ACADB4",
    "w. c #ACAEB7",
    "e. c #A0A4B9",
    "r. c #A2A6BB",
    "t. c #A0A3BD",
    "y. c #A1A6BC",
    "u. c #A1A6BD",
    "i. c #A2A5BF",
    "p. c #A6ABBB",
    "a. c #A3A9BF",
    "s. c #A6A9BF",
    "d. c #A6ABBF",
    "f. c #AFB1BA",
    "g. c #B0B0B2",
    "h. c #B3B4B6",
    "j. c #9EA3C0",
    "k. c #9FA3C0",
    "l. c #A0A5C0",
    "z. c #A1A6C1",
    "x. c #A4A7C0",
    "c. c #A3A8C2",
    "v. c #A4A8C0",
    "b. c #A6AAC3",
    "n. c #A4A9C4",
    "m. c #A5AAC5",
    "M. c #A5ABC5",
    "N. c #A7ABC4",
    "B. c #A5ABC6",
    "V. c #A7ADC7",
    "C. c #A9ACC3",
    "Z. c #A8ADC4",
    "A. c #A9ADC5",
    "S. c #AAADC5",
    "D. c #AAAEC5",
    "F. c #AAAEC7",
    "G. c #A8ADC8",
    "H. c #A9AEC8",
    "J. c #ACB1C5",
    "K. c #AEB2C7",
    "L. c #AFB2C7",
    "P. c #ABB0C8",
    "I. c #ADB1C8",
    "U. c #ADB2C9",
    "Y. c #AFB2C8",
    "T. c #ACB1CA",
    "R. c #ACB2CC",
    "E. c #B0B5C6",
    "W. c #B7BBC6",
    "Q. c #B9BAC1",
    "!. c #B8BAC2",
    "~. c #BCBEC6",
    "^. c #BDBFC6",
    "/. c #B0B5C8",
    "(. c #B1B4C9",
    "). c #B4B6CB",
    "_. c #B2B7CF",
    "`. c #B4B7CC",
    "'. c #B9BDC9",
    "]. c #BABCCE",
    "[. c #B4B8D1",
    "{. c #B5BAD3",
    "}. c #B7BCD0",
    "|. c #BBBCD0",
    " X c #B9BED5",
    ".X c #B9BED6",
    "XX c #BABFD6",
    "oX c #BABFD7",
    "OX c #BCC0D6",
    "+X c #BEC2D8",
    "@X c #C4C5CA",
    "#X c #C0C2D3",
    "$X c #C2C4D3",
    "%X c #C2C5D3",
    "&X c #C2C5D5",
    "*X c #CBCED5",
    "=X c #C1C7DD",
    "-X c #C3C7DD",
    ";X c #C2C8DF",
    ":X c #C6CBDC",
    ">X c #C4C9DE",
    ",X c #C4CADE",
    "<X c #C4CADF",
    "1X c #C5CBDF",
    "2X c #C7CDDF",
    "3X c #CBCED9",
    "4X c #CCCED9",
    "5X c #CFD1DB",
    "6X c #D0D2DC",
    "7X c #D4D6DD",
    "8X c #C3C9E0",
    "9X c #C5CBE1",
    "0X c #CDD1E2",
    "qX c #CBD1E4",
    "wX c #D1D4E0",
    "eX c #D2D5E2",
    "rX c #D4D8E5",
    "tX c #D6DAE5",
    "yX c #D4D9EA",
    "uX c #D4D9EB",
    "iX c #D7DCE8",
    "pX c #DADDEC",
    "aX c #DADFED",
    "sX c #DDE0EB",
    "dX c #DBE0EF",
    "fX c #DEE2ED",
    "gX c #DEE1EE",
    "hX c #DCE0F0",
    "jX c #DEE2F0",
    "kX c #DFE5F4",
    "lX c #DFE5F5",
    "zX c None",
    "zXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzX",
    "zXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzX",
    "zXzXzXzXzXzXzXzXzXzXzX*X7XzXzXzXzXzXzXzXzXzXzXzX",
    "zXzXzXzXzXzX<.@X1.zXzXrXpXzXzX1.@X<.zXzXzXzXzXzX",
    "zXzXzXzXzXzXq.kXOX4.h.tXiXg.,.~.jX9.zXzXzXzXzXzX",
    "zXzXzXzXzXzXzX'.sXfXjXyXuXfXsXhXW.zXzXzXzXzXzXzX",
    "zXzXzXG 3.zX<.wX:Xp.I M N Y L.qX*X..zX3.G zXzXzX",
    "zXzXzXw.pX!.wX:XU o.}.9X9XK.T o.qX5XQ.pXw.zXzXzX",
    "zXzXzXF 5.;X;X+.J.;X;X;X+X,X;Xd.e.:X;X5.A zXzXzX",
    "zXzXzXzXB }.K.r.OXOX..v b +.OXOX+.P.|.B zXzXzXzX",
    "zXzXzXzXA OXb.Z.[...8 zXzX8 E [.C.a.+XA zXzXzXzX",
    "zXzXf.6X%X[.$.N.T.y zXzXzXzXq T.P.$._.%X5X7.zXzX",
    "zXzXE d.r.m.$.m.N.y zXzXzXzX0 N.m.$.m.i.b.E zXzX",
    "zXzXzXzXi *.z.b.H.X.n zXzXm ..T.b.z.j.a zXzXzXzX",
    "zXzXzXzX9 { *.b.*.`.9.:.:.q.`.$.b.*.{ 9 zXzXzXzX",
    "zXzXzX7 C  .) C.x.{ D.&X&XD.} a.D._ | C 7 zXzXzX",
    "zXzXzXt / p H / K.(.) L L { (.I.) z p / t zXzXzX",
    "zXzXzX& , zX, h P i.].#X#X].t.P h , zX, & zXzXzX",
    "zXzXzXzXzXzXzXe l k c K J x k k w zXzXzXzXzXzXzX",
    "zXzXzXzXzXzX= z 4 % ; d d ; % 2 z & zXzXzXzXzXzX",
    "zXzXzXzXzXzX@ : + zXO r s O zX+ > # zXzXzXzXzXzX",
    "zXzXzXzXzXzXzX  zXzX. 1 4 X zXzXzXzXzXzXzXzXzXzX",
    "zXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzX",
    "zXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzX"
]

WHITE_TOOL_TIP = "White, H. (1980), Econometrica"
HAC_TOOL_TIP = "Kelejian, H. and Prucha, I. (2007), Journal of Econometrics"
HET_TOOL_TIP = "Kelejian, H. and Prucha, I. (2010), Journal of Econometrics"
# ML_TOOL_TIP = "(Coming soon)"
# R_TOOL_TIP = "Regime indicators"

myEVT_LIST_BOX_UPDATE = wx.NewEventType()
EVT_LIST_BOX_UPDATE = wx.PyEventBinder(myEVT_LIST_BOX_UPDATE, 1)


class MyStringIO(StringIO.StringIO):
    def close(self):
        pass


class TextCtrlDropTarget(wx.TextDropTarget):
    def __init__(self, target):
        wx.TextDropTarget.__init__(self)
        self.target = target
        self.target.SetEditable(False)

        self.text_obj = wx.CustomDataObject('py_str')
        self.SetDataObject(self.text_obj)

    def OnData(self, x, y, default):  # Called on drop
        self.GetData()
        text = self.text_obj.GetData()

        main_ui = self.target
        while main_ui.Parent:
            main_ui = main_ui.Parent

        if isinstance(main_ui, geodaspace.regression.V_regression.guiRegView):
            if main_ui.spacetimeKeyDown:
                # multi-variables (SUR -- e.g. HR80, HR90)
                old_txt = self.target.GetValue()
                old_items = old_txt.split(',') if len(old_txt) > 0 else []
                if len(text) > 0:
                    old_items += text.split(',')
                new_txt = ','.join(old_items)
                self.target.SetValue(new_txt)
                return default

        self.target.SetValue(text.split(',')[0])
        return default


class NullDropTarget(wx.TextDropTarget):
    def __init__(self, targetListBox):
        wx.TextDropTarget.__init__(self)
        self.targetListBox = targetListBox
        self.text_obj = wx.CustomDataObject('py_str')
        self.SetDataObject(self.text_obj)

    def OnData(self, x, y, default):
        return False

    def OnEnter(self, x, y, default):
        return wx.DragNone

    def OnDragOver(self, x, y, default):
        return wx.DragNone


class ListBoxDropTarget(wx.TextDropTarget):
    def __init__(self, targetListBox):
        wx.TextDropTarget.__init__(self)
        self.targetListBox = targetListBox

        self.text_obj = wx.CustomDataObject('py_str')
        self.SetDataObject(self.text_obj)

    def OnData(self, x, y, default):  # Called on drop
        if self.targetListBox.IsEnabled():
            # Find index to insert Drop Item(s)
            hitidx = self.targetListBox.HitTest((x, y))
            if hitidx == wx.NOT_FOUND:
                hitidx = self.targetListBox.GetCount()
            # Get Drop Item(s)
            self.GetData()
            text = self.text_obj.GetData()
            itms = text.split(',')
            # n = len(itms)  # not called
            # Remove duplicates items to make way to new items.
            for itm in itms:
                idx = self.targetListBox.FindString(itm)
                if idx != wx.NOT_FOUND:
                    self.targetListBox.Delete(idx)
                    if idx < hitidx:
                        hitidx -= 1

            # # multi-variables (SUR -- e.g. HR80, HR90)
            time_variable = False
            main_ui = self.targetListBox
            while main_ui.Parent:
                main_ui = main_ui.Parent
            if isinstance(main_ui, geodaspace.regression.V_regression.guiRegView):
                if main_ui.spacetimeKeyDown:
                    if hitidx > -1:
                        old_txt = self.targetListBox.GetString(hitidx) if hitidx < self.targetListBox.Count else ''
                        old_items = old_txt.split(',') if len(old_txt) > 0 else []
                        if len(text) > 0:
                            old_items += text.split(',')
                        new_txt = ','.join(old_items)
                        if hitidx < self.targetListBox.Count:
                            self.targetListBox.Delete(hitidx)
                        self.targetListBox.InsertItems([new_txt], hitidx)
                        time_variable = True

            if time_variable == False:
                # Insert Drop Item(s).
                self.targetListBox.InsertItems(itms, hitidx)

            # Fire my custom event type
            evt = ListBoxUpdateEvent(
                myEVT_LIST_BOX_UPDATE, self.targetListBox.GetId())
            self.targetListBox.GetEventHandler().ProcessEvent(evt)
            return default
        else:
            return False

    def OnEnter(self, x, y, default):
        if self.targetListBox.IsEnabled():
            return wx.DragCopy
        else:
            return wx.DragNone

    def OnDragOver(self, x, y, default):
        if self.targetListBox.IsEnabled():
            return wx.DragCopy
        else:
            return wx.DragNone


class ListBoxUpdateEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        """ A custom event type """
        wx.PyCommandEvent.__init__(self, evtType, id)


class guiRegView(OGRegression_xrc.xrcGMM_REGRESSION):
    def __init__(self, parent=None, results=None):
        self.results = results
        OGRegression_xrc.xrcGMM_REGRESSION.__init__(self, parent)
        self.SendSizeEvent()

        # Linux Fix for Drag and Drop
        # wxWidgets issue #2764
        if sys.platform.startswith('linux'):
            drop_target_parent = self.X_ListBox.GetParent()
            box = drop_target_parent.FindWindowByLabel('Specification')
            tmpParent = wx.Panel(drop_target_parent)
            box.Reparent(tmpParent)
            box.Reparent(drop_target_parent)
            # moves the box to the bottom of the stack
            tmpParent.Destroy()
        # end fix
        self.config = preferencesDialog(self)
        self.config.model.addListener(self.updateModelType)  # pas tik 149,156
        self.SetIcon(icons.getGeoDaIcon())
        self.modelFileName = None
        self.BASE_TITLE = self.GetTitle()
        # print "BASE_TITLE: ",self.BASE_TITLE
        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText(
            "GeoDaSpace " + geodaspace.version.get_long_version())

        # initialize the scrollbars, fix for issue #48
        w, h = self.Size
        self.scroll.SetScrollbars(1, 1, w, h)

        # NOTE: Tooltips are also set in the XRC for windows platforms, these
        # only work on MAC
        self.SEHACCheckBox.SetToolTipString(HAC_TOOL_TIP)
        self.SEHETCheckBox.SetToolTipString(HET_TOOL_TIP)
        self.SEWhiteCheckBox.SetToolTipString(WHITE_TOOL_TIP)

        self.wQueue = []
        self.modelWeightsDialog = weights.control.weightsDialog(
            self, requireSave=True,
            style=ENABLE_CONTIGUITY_WEIGHTS | ENABLE_DISTANCE_WEIGHTS)
        self.kernelWeightsDialog = weights.control.weightsDialog(
            self, requireSave=True, style=ENABLE_KERNEL_WEIGHTS)
        self.weightsPropDlg = weights.control.weightsPropertiesDialog(self)
        self.textFrame = textwindow.TextWindow(self)

        self.varSelector = None
        self.createSpatialLag = None

        # Setup Drop Targets
        self.Y_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.Y_TextCtrl))
        self.YE_ListBox.SetDropTarget(ListBoxDropTarget(self.YE_ListBox))
        self.H_ListBox.SetDropTarget(ListBoxDropTarget(self.H_ListBox))

        self.R_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.R_TextCtrl))
        self.S_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.S_TextCtrl))
        self.T_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.T_TextCtrl))

        self.X_ListBox.SetDropTarget(ListBoxDropTarget(self.X_ListBox))

        # SUR: space-time key down (Alt)
        self.spacetimeKeyDown = False

        # The Model
        self.model = M_regression.guiRegModel()
        self.model.data['config'] = self.config.GetPrefs()
        self.model.addListener(self.populate)
        # self.model.addListener(self.verbose)
        # The Bindings
        self.Bind(wx.EVT_BUTTON, self.DataOpenButtonClick, self.DATA_INPUTFILE)
        self.Bind(wx.EVT_BUTTON, self.OpenWeightsButtonClick,
                  self.OpenMWeightsButton)
        self.Bind(wx.EVT_BUTTON, self.OpenWeightsButtonClick,
                  self.OpenKWeightsButton)
        self.Bind(wx.EVT_BUTTON, self.CreateMWeightsButtonClick,
                  self.CreateMWeightsButton)
        self.Bind(wx.EVT_BUTTON, self.CreateKWeightsButtonClick,
                  self.CreateKWeightsButton)
        self.Bind(wx.EVT_BUTTON, self.run, self.RunButton)
        # self.Bind(wx.EVT_BUTTON, self.saveModel, self.SaveButton)
        # self.Bind(wx.EVT_BUTTON, self.close, self.CloseButton)
        # self.DATAFILE.Bind(wx.EVT_COMBOBOX,self.setDataFile)
        # self.DATAFILE.Bind(wx.EVT_TEXT_ENTER,self.setDataFile)
        # self.IDVAR.Bind(wx.EVT_CHOICE,self.setIDVar)

        self.Y_TextCtrl.Bind(wx.EVT_TEXT, self.updateSpec)
        self.Y_TextCtrl.Bind(wx.EVT_LEFT_DCLICK, self.clearTextBox)
        self.Y_TextCtrl.Bind(wx.EVT_CHAR, self.clearTextBox)
        self.YE_ListBox.Bind(EVT_LIST_BOX_UPDATE, self.updateSpec)
        self.YE_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.removeSelected)
        self.YE_ListBox.Bind(wx.EVT_CHAR, self.removeSelected)
        self.YE_ListBox.Bind(wx.EVT_MOUSE_EVENTS, self._startDrag)
        self.H_ListBox.Bind(EVT_LIST_BOX_UPDATE, self.updateSpec)
        self.H_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.removeSelected)
        self.H_ListBox.Bind(wx.EVT_CHAR, self.removeSelected)
        self.H_ListBox.Bind(wx.EVT_MOUSE_EVENTS, self._startDrag)
        self.R_TextCtrl.Bind(wx.EVT_TEXT, self.updateSpec)
        self.R_TextCtrl.Bind(wx.EVT_LEFT_DCLICK, self.clearTextBox)
        # self.R_TextCtrl.SetToolTipString(R_TOOL_TIP)
        self.S_TextCtrl.Bind(wx.EVT_TEXT, self.updateSpec)
        self.S_TextCtrl.Bind(wx.EVT_LEFT_DCLICK, self.clearTextBox)
        self.T_TextCtrl.Bind(wx.EVT_TEXT, self.updateSpec)
        self.T_TextCtrl.Bind(wx.EVT_LEFT_DCLICK, self.clearTextBox)
        self.X_ListBox.Bind(EVT_LIST_BOX_UPDATE, self.updateSpec)
        self.X_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.removeSelected)
        self.X_ListBox.Bind(wx.EVT_CHAR, self.removeSelected)
        self.X_ListBox.Bind(wx.EVT_MOUSE_EVENTS, self._startDrag)

        # The next 2 lines are commented out to disable removing weights files.
        # TODO: the removal mechanism doesn't work with w objs, need to fix
        self.MWeights_ListBox.Bind(wx.EVT_CHECKLISTBOX, self.updateWeights)
        self.MWeights_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.updateWeights)
        self.MWeights_ListBox.Bind(wx.EVT_CHAR, self.updateWeights)
        self.Bind(wx.EVT_BUTTON, self.updateWeights, self.PropMWeightsButton)
        self.KWeights_ListBox.Bind(wx.EVT_CHECKLISTBOX, self.updateWeights)
        self.KWeights_ListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.updateWeights)
        self.KWeights_ListBox.Bind(wx.EVT_CHAR, self.updateWeights)
        self.Bind(wx.EVT_BUTTON, self.updateWeights, self.PropKWeightsButton)

        # self.Bind(wx.EVT_RADIOBUTTON,self.updateModelType)

        self.MT_STD.Bind(wx.EVT_RADIOBUTTON, self.updateModelType)
        self.MT_LAG.Bind(wx.EVT_RADIOBUTTON, self.updateModelType)
        self.MT_ERR.Bind(wx.EVT_RADIOBUTTON, self.updateModelType)
        self.MT_LAGERR.Bind(wx.EVT_RADIOBUTTON, self.updateModelType)
        self.OLS_radiobutton.Bind(
            wx.EVT_RADIOBUTTON, self.updateModelType)  # pas
        self.GMM_radiobutton.Bind(
            wx.EVT_RADIOBUTTON, self.updateModelType)  # pas
        self.ML_radiobutton.Bind(
            wx.EVT_RADIOBUTTON, self.updateModelType)  # pas
        # self.ML_radiobutton.SetToolTipString(ML_TOOL_TIP)

        # self.ModelTypeRadioBox.Bind(wx.EVT_RADIOBOX, self.updateModelType)
        # self.ENDO_CHECK.Bind(wx.EVT_CHECKBOX, self.updateModelType)
        # self.EndogenousRadioBox.Bind(wx.EVT_RADIOBOX, self.updateModelType)
        # self.MethodsRadioBox.Bind(wx.EVT_RADIOBOX, self.updateModelType)
        # self.SEClassicCheckBox.Bind(wx.EVT_CHECKBOX, self.updateModelType)

        # self.gm_checkbox.Bind(wx.EVT_CHECKBOX, self.updateModelType)
        # self.ml_checkbox.Bind(wx.EVT_CHECKBOX, self.updateModelType)

        # self.MethodsRadioBox.Bind(wx.EVT_RADIOBOX, self.updateMethodType)

        self.SEWhiteCheckBox.Bind(wx.EVT_CHECKBOX, self.updateModelType)
        self.SEHACCheckBox.Bind(wx.EVT_CHECKBOX, self.updateModelType)
        self.SEHETCheckBox.Bind(wx.EVT_CHECKBOX, self.updateModelType)
        self.ST_LM.Bind(wx.EVT_CHECKBOX, self.updateModelType)

        self.SetToolBar(None)
        self.RegressionToolBar = self.CreateToolBar()
        bmp_new = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_OTHER)
        bmp_open = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER)
        bmp_save = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER)
        bmp_saveas = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_OTHER)
        bmp_report = wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER)
        bmp_page = wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE, wx.ART_OTHER)
        bmp_adv = wx.BitmapFromXPMData(gear_png)

        self.RegressionToolBar.SetToolBitmapSize((24, 24))
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolNewModel"), bmp_new,
                                       shortHelpString='Create New Model: Choose data file')
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolOpenModel"), bmp_open,
                                       shortHelpString='Open Existing Model: Choose .mdl File')
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolSaveModel"), bmp_save, shortHelpString='Save Model..')
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolSaveModelAs"), bmp_saveas, shortHelpString='Save Model As...')
        self.RegressionToolBar.AddSeparator()
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolVariableSelector"), bmp_report,
                                       shortHelpString='Open the Variable List')
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolResultsWindow"), bmp_page,
                                       shortHelpString='Show the Results Window')
        self.RegressionToolBar.AddSeparator()
        self.RegressionToolBar.AddTool(wx.xrc.XRCID("ToolAdvanced"), bmp_adv, shortHelpString='Show Advanced Settings')

        self.RegressionToolBar.Realize()

        self.RegressionToolBar.Bind(wx.EVT_MENU, self.newModel,
                                    id=wx.xrc.XRCID("ToolNewModel"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.openModel,
                                    id=wx.xrc.XRCID("ToolOpenModel"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.saveModel,
                                    id=wx.xrc.XRCID("ToolSaveModel"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.saveModelAs,
                                    id=wx.xrc.XRCID("ToolSaveModelAs"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.showVarSelector,
                                    id=wx.xrc.XRCID("ToolVariableSelector"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.openResultsWindow,
                                    id=wx.xrc.XRCID("ToolResultsWindow"))
        self.RegressionToolBar.Bind(wx.EVT_MENU, self.openConfig,
                                    id=wx.xrc.XRCID("ToolAdvanced"))

        self.textFrame.Bind(wx.EVT_CLOSE, self.openResultsWindow)
        self.Bind(wx.EVT_CLOSE, self.close)

        self.MODELTYPES = [self.MT_STD,
                           self.MT_LAG,
                           self.MT_ERR,
                           self.MT_LAGERR]

        self.METHOD = [
            self.OLS_radiobutton, self.GMM_radiobutton, self.ML_radiobutton]
        self.populate(None)

    def _startDrag(self, evt):
        if evt.Dragging():
            to_drag = None
            if type(evt.EventObject) == wx.ListBox:
                if evt.EventObject.GetSelection() != wx.NOT_FOUND:
                    to_drag = evt.EventObject.GetSelection()
                if to_drag not in [wx.NOT_FOUND, None]:
                    data = wx.CustomDataObject('py_str')
                    data.SetData(evt.EventObject.GetString(
                        to_drag).encode('utf8'))
                    var2del = evt.EventObject.GetString(to_drag)
                    to_del = evt.EventObject.FindString(var2del)
                    evt.EventObject.Delete(to_del)
                    dropSource = wx.DropSource(evt.EventObject)
                    dropSource.SetData(data)
                    res = dropSource.DoDragDrop(flags=wx.Drag_DefaultMove)
                    if res == wx.DragMove or res == wx.DragCopy:
                        self.updateSpec(None)
                    else:
                        evt.EventObject.Insert(var2del, to_del)

        evt.Skip()

    def close(self, evt=None):
        # print "close"
        if self.textFrame.Close():
            self.Destroy()

    def able(self):
        # self.tooltips()
        """ Disables and/or Enables parts of the form, based on the status
        of the model """
        if self.model.state == self.model.STATE_EMPTY:
            # self.Panel.Disable()
            self.Panel_Weights.Disable()
            self.Panel_Spec.Disable()
            self.Panel_Estimation.Disable()
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolVariableSelector"), False)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolResultsWindow"), False)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolSaveModel"), False)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolSaveModelAs"), False)
        else:
            # self.Panel.Enable()
            self.Panel_Weights.Enable()
            self.Panel_Spec.Enable()
            self.Panel_Estimation.Enable()
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolVariableSelector"), True)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolResultsWindow"), True)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolSaveModel"), True)
            self.RegressionToolBar.EnableTool(
                wx.xrc.XRCID("ToolSaveModelAs"), True)
            # Not implemented yet
            # self.ModelTypeRadioBox.EnableItem(4,False) #Regimes.Disable()
            # self.R_TextCtrl.Disable()
            # self.S_TextCtrl.Disable()
            # self.T_TextCtrl.Disable()

            # Fixed, always on.
            # self.SEClassicCheckBox.Disable()
            # self.SEWhiteCheckBox.Disable()

            # self.EnableMethods()
            m = self.model.data
            if m['fname']:
                m['config'] = self.config.GetPrefs()  # tik 149
                # if m['modelType']['endogenous'] == True: #Yes
                #    self.YE_ListBox.Enable()
                #    self.H_ListBox.Enable()
                # else: #No
                #    self.YE_ListBox.Disable()
                #    self.H_ListBox.Disable()

                # SUR model for panel data
                is_SUR = False
                if m['spec']['S'] and m['spec']['T'] and \
                        len(m['spec']['S']) > 0 and len(m['spec']['T']) > 0:
                    is_SUR = True
                elif m['spec']['y'].find(',') >= 0:
                    is_SUR = True
                    if len(self.T_TextCtrl.GetValue()) > 0:
                        self.T_TextCtrl.Clear()
                    if len(self.S_TextCtrl.GetValue()) > 0:
                        self.S_TextCtrl.Clear()
                    self.T_TextCtrl.Disable()
                    self.S_TextCtrl.Disable()
                    self.T_TextCtrl.SetDropTarget(NullDropTarget(self.T_TextCtrl))
                    self.S_TextCtrl.SetDropTarget(NullDropTarget(self.S_TextCtrl))
                    for spec_x in m['spec']['X']:
                        if spec_x.find(',') < 0:
                            is_SUR = False
                else:
                    self.T_TextCtrl.Enable()
                    self.S_TextCtrl.Enable()
                    self.T_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.T_TextCtrl))
                    self.S_TextCtrl.SetDropTarget(TextCtrlDropTarget(self.S_TextCtrl))

                if m['modelType']['mType'] == 2 or \
                        m['modelType']['mType'] == 3:
                    # an error model
                    # No White in Error Models
                    self.SEWhiteCheckBox.Disable()
                    self.SEWhiteCheckBox.SetValue(False)
                    m['modelType']['error']['white'] = False
                    # allow HET only in Error models
                    self.SEHETCheckBox.Enable()
                    self.ST_LM.Disable()
                    self.ST_LM.SetValue(False)
                    if is_SUR and m['modelType']['mType'] == 3:
                        # combo 3 not avaible for SUR
                        self.MT_LAGERR.Disable()
                        m['modelType']['mType'] = 2
                        self.MT_ERR.SetValue(True)
                else:
                    self.ST_LM.Enable()
                    self.SEWhiteCheckBox.Enable()
                    self.SEHETCheckBox.Disable()
                    self.SEHETCheckBox.SetValue(False)
                    m['modelType']['error']['het'] = False

                if m['config']['gmm_inferenceOnLambda'] is False:
                    self.SEHETCheckBox.Disable()
                    self.SEHETCheckBox.SetValue(False)
                    m['modelType']['error']['het'] = False

                # HAC
                # issue 163 here
                if m['config']['regimes_regime_error'] is True and \
                        m['spec']['R']:
                    self.SEHACCheckBox.Disable()
                    self.SEHACCheckBox.SetValue(False)
                    m['modelType']['error']['hac'] = False

                if m['spec']['R'] and m['modelType']['mType'] == 2:
                    m['config']['regimes_regime_error'] is False

                # Standard or SpatialLag
                elif m['modelType']['mType'] == 0 or \
                        m['modelType']['mType'] == 1:
                    self.SEHACCheckBox.Enable()
                else:
                    self.SEHACCheckBox.SetValue(False)
                    m['modelType']['error']['hac'] = False
                    self.SEHACCheckBox.Disable()

                # max likelihood, ml
                if m['modelType']['method'] == 2:
                    self.SEWhiteCheckBox.SetValue(False)
                    self.SEWhiteCheckBox.Disable()
                    self.SEHETCheckBox.SetValue(False)
                    self.SEHETCheckBox.Disable()
                    self.SEHACCheckBox.SetValue(False)
                    self.SEHACCheckBox.Disable()

                # the matrix
                if len(m['spec']['H']) > 0 or len(m['spec']['YE']) > 0 \
                        or m['modelType']['mType'] != 0:

                    if m['modelType']['method'] == 0:  # set GMM default
                        m['modelType']['method'] = 1

                    self.OLS_radiobutton.SetValue(False)
                    self.OLS_radiobutton.Disable()
                    self.GMM_radiobutton.Enable()
                    self.GMM_radiobutton.SetValue(True)

                    if m['modelType']['mType'] != 3 and len(m['spec']['H']) == 0 \
                            and len(m['spec']['YE']) == 0:
                        self.ML_radiobutton.Enable()
                        if is_SUR and m['modelType']['mType'] != 2:
                            self.ML_radiobutton.SetValue(False)
                            self.ML_radiobutton.Disable()
                            m['modelType']['method'] = 1
                    else:
                        self.ML_radiobutton.Disable()
                        self.ML_radiobutton.SetValue(False)
                        self.GMM_radiobutton.SetValue(True)
                        m['modelType']['method'] = 1
                        if m['modelType']['mType'] == 3:
                            self.SEHETCheckBox.Enable()
                    if m['modelType']['method'] == 1:
                        self.GMM_radiobutton.SetValue(True)
                    if m['modelType']['method'] == 2:
                        self.ML_radiobutton.SetValue(True)
                else:
                    self.OLS_radiobutton.SetValue(True)
                    self.OLS_radiobutton.Enable()
                    m['modelType']['method'] = 0
                    self.GMM_radiobutton.Disable()
                    self.GMM_radiobutton.SetValue(False)
                    if is_SUR:
                        self.GMM_radiobutton.SetValue(True)
                        self.GMM_radiobutton.Enable()
                        m['modelType']['method'] = 1
                        self.OLS_radiobutton.Disable()
                        self.OLS_radiobutton.SetValue(False)
                    self.ML_radiobutton.Disable()
                    self.ML_radiobutton.SetValue(False)

                if is_SUR:
                    self.SEWhiteCheckBox.SetValue(False)
                    self.SEHACCheckBox.SetValue(False)
                    self.SEHETCheckBox.SetValue(False)
                    self.SEWhiteCheckBox.Disable()
                    self.SEHACCheckBox.Disable()
                    self.SEHETCheckBox.Disable()
                    # combo not avaible for SUR
                    self.MT_LAGERR.Disable()
                    """
		    if len(m['spec']['H']) > 0 or len(m['spec']['YE']) > 0:
			self.MT_ERR.Disable()
			m['modelType']['mType'] = 0 if len(m['mWeights']) == 0 else 1
		    else:
			self.MT_ERR.Enable()
			
		    if m['modelType']['mType'] == 2: # spatial error
			self.ML_radiobutton.Enable()
		    else:
			self.ML_radiobutton.Disable()
			self.OLS_radiobutton.Disable()
			self.GMM_radiobutton.Enable()
                        self.GMM_radiobutton.SetValue(True)
		    """
                else:
                    self.SEWhiteCheckBox.Enable()
                    self.SEHACCheckBox.Enable()
                    self.SEHETCheckBox.Enable()

                    self.MT_ERR.Enable()
                    self.MT_LAGERR.Enable()

    def setTitle(self):
        if self.modelFileName:
            fname = os.path.split(self.modelFileName)[1]
            if self.model.state == self.model.STATE_CHANGED:
                fname += "*"
            self.SetTitle(self.BASE_TITLE + ": %s" % fname)
        elif self.model.state == self.model.STATE_CHANGED:
            self.SetTitle(self.BASE_TITLE + ": untitled*")

    def newModel(self, evt):
        self.model.reset()
        self.modelFileName = None
        self.setTitle()
        self.DataOpenButtonClick(evt)

    def saveWeights(self):
        for w in self.model.data['mWeights'] + self.model.data['kWeights']:
            if not w.saved:
                dialog = wx.MessageDialog(
                    self, "Would you like to save the weights file now?",
                    'Weights object (%s) must be saved to disk or removed\
                    to continue saving model.' % (w.name),
                    style=wx.YES_NO | wx.CENTRE)
                result = dialog.ShowModal()
                if result == wx.ID_YES:
                    self.modelWeightsDialog.SetW(w.w)
                    if not self.modelWeightsDialog.save():
                        return False
                else:
                    return False
        return True

    def saveModelAs(self, evt):
        if not self.saveWeights():
            return False
        fname = self.model.data['fname']
        suggestion = os.path.split(fname)[1].split('.')[0] + '.mdl'
        fileDialog = wx.FileDialog(
            self, defaultFile=suggestion, message="Save Model As...",
            wildcard="*.mdl", style=wx.SAVE + wx.OVERWRITE_PROMPT)
        result = fileDialog.ShowModal()
        if result == wx.ID_OK:
            path = fileDialog.GetPath()
            if not path[-4:] == '.mdl':
                path += '.mdl'
            f = open(path, 'w')
            self.model.save(f)
            f.close()
            self.modelFileName = path
            self.setTitle()
        else:
            pass

    def saveModel(self, evt):
        if self.modelFileName:
            if not self.saveWeights():
                return False
            f = open(self.modelFileName, 'w')
            self.model.save(f)
            f.close()
            self.setTitle()
        else:
            self.saveModelAs(evt)

    def locateMissingFile(self, oldPath):
        confirmDialog = wx.MessageDialog(
            self, "%s does not exist, would you like to locate the correct\
            file?" % oldPath, 'The file could not be located!',
            style=wx.YES_NO | wx.CENTRE)
        result = confirmDialog.ShowModal()
        if result == wx.ID_YES:
            if '\\' in oldPath:
                basename = oldPath.split('\\')[-1]
            elif '/' in oldPath:
                basename = oldPath.split('/')[-1]
            else:
                basename = os.path.basename(oldPath)
            filter = "%s|%s" % (basename, basename)
            fileDialog = wx.FileDialog(self, message="Please locate %s" %
                                                     basename, wildcard=filter)
            fdResult = fileDialog.ShowModal()
            if fdResult == wx.ID_OK:
                path = fileDialog.GetPath()
                return path
        else:
            return False

    def openModel(self, evt):
        try:
            fileDialog = wx.FileDialog(self, message="Select Model To Open...",
                                       wildcard="*.mdl")
            result = fileDialog.ShowModal()
            if result == wx.ID_OK:
                path = fileDialog.GetPath()
                location = os.path.dirname(path)
                f = open(path, 'r')
                dat = f.read()
                changed = False
                dataDict = eval(dat)
                dataDict['fname'] = os.path.normpath(
                    os.path.join(location, dataDict['fname']))
                if not os.path.exists(dataDict['fname']):
                    print "no such file!"
                    newPath = self.locateMissingFile(dataDict['fname'])
                    if newPath:
                        dataDict['fname'] = newPath
                        changed = True
                    else:
                        return False
                for i, mw in enumerate(dataDict['mWeights']):
                    mw = os.path.normpath(os.path.join(location, mw))
                    dataDict['mWeights'][i] = mw
                    if not os.path.exists(mw):
                        print "no such file!"
                        newPath = self.locateMissingFile(mw)
                        if newPath:
                            dataDict['mWeights'][i] = newPath
                            changed = True
                        else:
                            return False
                for i, kw in enumerate(dataDict['kWeights']):
                    kw = os.path.normpath(os.path.join(location, kw))
                    dataDict['kWeights'][i] = kw
                    if not os.path.exists(kw):
                        print "no such file!"
                        newPath = self.locateMissingFile(kw)
                        if newPath:
                            dataDict['kWeights'][i] = newPath
                            changed = True
                        else:
                            return False

                dat = str(dataDict)
                self.model.open(dat)
                f.close()
                self.modelFileName = path
                self.setTitle()
                self.newVarSelector()
                if changed:
                    self.model.update()  # sets modified flag
                # print "openModel, path... ",path
            else:
                print "canceled"
        except:
            confirmDialog = wx.MessageDialog(
                self, "The model file could not be loaded.",
                'Invalid Model File!', style=wx.OK | wx.CENTRE)
            result = confirmDialog.ShowModal()
            self.model.reset()
            self.populate(self.model)
            raise

    def updateModelType(self, evt):
        modelSetup = {}
        # return element that is true -- only one can be true
        modelSetup['mType'] = [m.GetValue()
                               for m in self.MODELTYPES].index(True)

        try:
            modelSetup['method'] = [m.GetValue()
                                    for m in self.METHOD].index(True)
        except ValueError as e:
            print(e)
            modelSetup['method'] = 1
            pass
        # modelSetup['method'] = self.ml_checkbox.GetValue()
        # modelSetup['mType'] = self.ModelTypeRadioBox.GetSelection()
        # modelSetup['endogenous'] = self.EndogenousRadioBox.GetSelection()
        # modelSetup['endogenous'] = self.ENDO_CHECK.GetValue()
        # modelSetup['method'] = self.MethodsRadioBox.GetSelection()
        modelSetup['error'] = {}
        modelSetup['error']['classic'] = True
        modelSetup['error']['white'] = self.SEWhiteCheckBox.GetValue()
        modelSetup['error']['hac'] = self.SEHACCheckBox.GetValue()
        modelSetup['error']['het'] = self.SEHETCheckBox.GetValue()
        modelSetup['spatial_tests'] = {}
        modelSetup['spatial_tests']['lm'] = self.ST_LM.GetValue()
        self.model.setModelType(modelSetup)
        print modelSetup

    # TODO: add 'method' check here
    def setModelType(self, setup):
        """ Compares the ModelType settings in self.model with the settings
        in the GUI form. These should only differ when model is loaded from
        file or changed programatically."""
        if not setup['mType'] == [m.GetValue()
                                  for m in self.MODELTYPES].index(True):
            self.MODELTYPES[setup['mType']].SetValue(True)

        try:
            if not setup['method'] == [m.GetValue()
                                       for m in self.METHOD].index(True):
                self.METHOD[setup['method']].SetValue(True)
        except ValueError as e:
            print(e)
            pass

        if not setup['error']['white'] == self.SEWhiteCheckBox.GetValue():
            self.SEWhiteCheckBox.SetValue(setup['error']['white'])
        if not setup['error']['hac'] == self.SEHACCheckBox.GetValue():
            self.SEHACCheckBox.SetValue(setup['error']['hac'])
        if not setup['error']['het'] == self.SEHETCheckBox.GetValue():
            self.SEHETCheckBox.SetValue(setup['error']['het'])
        if not setup['spatial_tests']['lm'] == self.ST_LM.GetValue():
            self.ST_LM.SetValue(setup['spatial_tests']['lm'])

    def updateSpec(self, evt):
        spec = {}
        spec['y'] = self.Y_TextCtrl.GetValue()

        ## YE
        YE = []
        for var in self.YE_ListBox.GetItems():
            if var not in YE:
                YE.append(var)
        spec['YE'] = YE

        ## H
        H = []
        for var in self.H_ListBox.GetItems():
            if var not in H:
                H.append(var)
        spec['H'] = H

        spec['R'] = self.R_TextCtrl.GetValue()
        spec['S'] = self.S_TextCtrl.GetValue()
        spec['T'] = self.T_TextCtrl.GetValue()

        ## X
        X = []
        for var in self.X_ListBox.GetItems():
            if var not in X:
                X.append(var)
        spec['X'] = X

        # print "Setting Model Spec as... ",spec
        # print "form X_ListBox contains, ",self.X_ListBox.GetItems()
        # print "form X_ListBox contains Strings, ",self.X_ListBox.GetStrings()

        # This code block was used to support removing weights objects...
        # mwFiles = self.MWeights_ListBox.GetItems()
        # newWeights = []
        # for p in mwFiles:
        #    tmp = [w for w in self.model.data['mWeights'] if p in w]
        #    if tmp:
        #        newWeights.append(tmp[0])
        # self.model.data['mWeights'] = newWeights

        # kwFiles = self.KWeights_ListBox.GetItems()
        # newWeights = []
        # for p in kwFiles:
        #    tmp = [w for w in self.model.data['kWeights'] if p in w]
        #    if tmp:
        #        newWeights.append(tmp[0])
        # self.model.data['kWeights'] = newWeights

        self.model.setSpec(spec)

    def setSpec(self, spec):
        # print "Setting Form Spec as... ",spec
        if not spec['y'] == self.Y_TextCtrl.GetValue():
            # TextCtrl.SetValue triggers an event, which interupts the form
            # update.
            self.Y_TextCtrl.SetEvtHandlerEnabled(False)
            self.Y_TextCtrl.SetValue(spec['y'])
            self.Y_TextCtrl.SetEvtHandlerEnabled(True)
        if not spec['YE'] == self.YE_ListBox.GetItems():
            self.YE_ListBox.SetItems(spec['YE'])
        if not spec['H'] == self.H_ListBox.GetItems():
            self.H_ListBox.SetItems(spec['H'])
        if not spec['R'] == self.R_TextCtrl.GetValue():
            self.R_TextCtrl.SetValue(spec['R'])
        if not spec['S'] == self.S_TextCtrl.GetValue():
            self.S_TextCtrl.SetValue(spec['S'])
        if not spec['T'] == self.T_TextCtrl.GetValue():
            self.T_TextCtrl.SetValue(spec['T'])
        if not spec['X'] == self.X_ListBox.GetItems():
            self.X_ListBox.SetItems(spec['X'])

    def updateWeights(self, evt):
        if evt.GetEventType() == wx.EVT_CHECKLISTBOX.typeId:
            if evt.EventObject == self.MWeights_ListBox:
                names = self.MWeights_ListBox.GetCheckedStrings()
                for w in self.model.getMWeightsFiles():
                    if w.name in names:
                        w.enabled = True
                    else:
                        w.enabled = False
            if evt.EventObject == self.KWeights_ListBox:
                names = self.KWeights_ListBox.GetCheckedStrings()
                for w in self.model.getKWeightsFiles():
                    if w.name in names:
                        w.enabled = True
                    else:
                        w.enabled = False
        elif evt.GetEventType() == wx.EVT_LISTBOX_DCLICK.typeId:
            if evt.EventObject == self.MWeights_ListBox:
                self.model.removeMW(evt.Selection)
            if evt.EventObject == self.KWeights_ListBox:
                self.model.removeKW(evt.Selection)
        elif type(evt) == wx.KeyEvent:
            code = evt.GetKeyCode()
            selection = None
            if code in [wx.WXK_BACK, wx.WXK_DELETE]:
                selection = evt.EventObject.GetSelection()
            if evt.EventObject == self.MWeights_ListBox and selection:
                self.model.removeMW(selection)
            if evt.EventObject == self.KWeights_ListBox and selection:
                self.model.removeKW(selection)
        elif evt.GetEventType() == wx.EVT_BUTTON.typeId:
            if evt.EventObject == self.PropMWeightsButton:
                w_objs = self.model.getMWeightsFiles()
                sel = self.MWeights_ListBox.GetSelection()
                count = self.MWeights_ListBox.GetCount()
            elif evt.EventObject == self.PropKWeightsButton:
                w_objs = self.model.getKWeightsFiles()
                sel = self.KWeights_ListBox.GetSelection()
                count = self.KWeights_ListBox.GetCount()
            else:
                print "We shouldn't be here"
                return
            if count == 0:
                dialog = wx.MessageDialog(
                    self, "Please open or create a weights object first.",
                    "Weights Properties...", wx.OK | wx.ICON_ERROR)
                dialog.ShowModal()
                return
            else:
                self.weightsPropDlg.ShowModal(w_objs, sel)
        else:
            print evt

    def openResultsWindow(self, evt=None):
        if self.textFrame.IsShown():
            self.textFrame.Hide()
        else:
            self.textFrame.Show()
            self.textFrame.Raise()

    def openConfig(self, evt=None):
        rs = self.config.ShowModal()
        self.model.data['config'] = self.config.GetPrefs()

    def newVarSelector(self, evt=None):
        """ Util function, recreates the Variable Selector as needed """
        if self.varSelector:
            self.varSelector.Hide()
            self.varSelector.Destroy()
        self.varSelector = variableTools.vVariableSelector(
            self, values=self.model.getVariables())
        self.varSelector.Bind(wx.EVT_CLOSE, self.showVarSelector)
        self.varSelector.panel.ToolBar.Bind(wx.EVT_MENU,
                                            self.spatialLag,
                                            id=wx.xrc.XRCID("ToolSpatialLag"))
        self.varSelector.panel.ToolBar.EnableTool(
            wx.xrc.XRCID("ToolSpatialLag"), True)
        # self.varSelector.populate(self.model.getVariables())
        self.varSelector.CenterOnParent()
        self.varSelector.Show()

    def spatialLag(self, evt):
        if self.createSpatialLag:
            self.createSpatialLag.Hide()
            self.createSpatialLag.Destroy()
        # print self.varSelector.getSelected()
        weights = set(self.model.data['mWeights'])
        weights = weights.union(set(self.model.data['kWeights']))
        # print weights
        vars = self.model.getVariables()
        self.spLagQueue = []
        self.createSpatialLag = spatialLag.C_CreateSpatialLag(
            dataFile=self.model.data['fname'], wtFiles=weights, vars=vars,
            results=self.spLagQueue, dialogMode=True)
        for var in self.varSelector.getSelected():
            self.createSpatialLag.addRow(varIDX=vars.index(var))

        if self.varSelector.IsShown():
            self.showVarSelector()
            self.createSpatialLag.ShowModal()
            self.showVarSelector()
        else:
            self.createSpatialLag.ShowModal()

        if len(self.spLagQueue) >= 1:
            if os.path.exists(self.spLagQueue[-1]):
                self.setDataFile(self.spLagQueue[-1], True)

    def showVarSelector(self, evt=None):
        """ Util function, hides/shows the Variable Selector as needed """
        if not self.varSelector:
            self.newVarSelector()
            self.varSelector.Hide()
        if self.varSelector.IsShown():
            self.varSelector.Hide()
        else:
            self.varSelector.Show()
            self.varSelector.Raise()

    def clearTextBox(self, evt):
        " Clears a textbox, bind to double click "
        if type(evt) == wx.KeyEvent:
            code = evt.GetKeyCode()
            if code in [wx.WXK_BACK, wx.WXK_DELETE]:
                evt.EventObject.Clear()
        else:
            target = evt.EventObject
            target.Clear()
        self.updateSpec(evt)

    def removeSelected(self, evt):
        """Removes a selected item from listbox,
        bind to double click and evt_char."""
        if type(evt) == wx.KeyEvent:
            code = evt.GetKeyCode()
            if code in [wx.WXK_BACK, wx.WXK_DELETE]:
                selection = evt.EventObject.GetSelection()
                if selection != wx.NOT_FOUND:
                    evt.EventObject.Delete(selection)
        else:
            target = evt.EventObject
            target.Delete(evt.Selection)
        self.updateSpec(evt)

    def CreateMWeightsButtonClick(self, evt):
        f = self.model.data['fname']
        f = f[:-3] + 'shp'
        if os.path.exists(f):
            try:
                self.modelWeightsDialog.model.inShp = f
            except:
                raise
        if self.modelWeightsDialog.ShowModal() == wx.ID_OK:
            self.model.addMWeightsFile(obj=self.modelWeightsDialog.GetW())

    def CreateKWeightsButtonClick(self, evt):
        f = self.model.data['fname']
        f = f[:-3] + 'shp'
        if os.path.exists(f):
            try:
                self.kernelWeightsDialog.model.inShp = f
            except:
                raise
        if self.kernelWeightsDialog.ShowModal() == wx.ID_OK:
            self.model.addKWeightsFile(obj=self.kernelWeightsDialog.GetW())
        #    print "added"
        # else:
        #    print "failed"

    def OpenWeightsButtonClick(self, evt):
        if evt.EventObject == self.OpenMWeightsButton:
            target = 'model_w'
        elif evt.EventObject == self.OpenKWeightsButton:
            target = 'kernel_w'
        else:
            raise RuntimeError("Unexpected evt object")
        pathHint = os.path.split(self.model.data['fname'])[0]
        # filter = "Weights File (*.gal; *.gwt)|*.gal;*.gwt" #"|*.gal|GWT
        # file|*.gwt|XML Weights|*.xml"
        filter = "Common Weights Types|"
        filter += ';'.join([x for i, x in enumerate(WEIGHT_TYPES_FILTER.split(
            '|')[1::2]) if WEIGHT_FILTER_TO_HANDLER[i] is None])
        fileDialog = wx.FileDialog(
            self, defaultDir=pathHint, message="Choose Weights File",
            wildcard=filter + '|' + WEIGHT_TYPES_FILTER)
        if target == 'model_w':
            fileDialog.SetFilterIndex(0)  # default to gal
        elif target == 'kernel_w':
            fileDialog.SetFilterIndex(7 + 1)  # default to kwt
        result = fileDialog.ShowModal()
        if result == wx.ID_OK:
            path = fileDialog.GetPath()
            try:
                idx = fileDialog.GetFilterIndex() - 1
                if idx == -1:
                    handler = None
                else:
                    handler = WEIGHT_FILTER_TO_HANDLER[
                        fileDialog.GetFilterIndex() - 1]
                W = pysal.open(path, 'r', handler).read()
                W.meta = {'shape file': 'unknown', 'method':
                    os.path.basename(path), 'savedAs': path}
                assert type(W) == pysal.W
                if target == 'model_w':
                    self.model.addMWeightsFile(obj=W)
                elif target == 'kernel_w':
                    self.model.addKWeightsFile(obj=W)
            except:
                dialog = wx.MessageDialog(
                    self, "An error occurred while trying to read your weights\
                    object, please check the file: %s" %
                          path, "Could not extract weights object:",
                          wx.OK | wx.ICON_ERROR)
                dialog.ShowModal()
                raise
        else:
            print "canceled"

    def KernelWeightsWarning(self, obj):
        if self.model.checkKW(obj):
            pass
        else:
            dialog = wx.MessageDialog(
                self, "Please use distance based weights with sufficient\
                # of neighbors (see manual).",
                "Kernel Weights Warning:", wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()

    def DataOpenButtonClick(self, evt):
        filter = "dBase file (*.dbf)|*.dbf|Comma Separated Values\
                (*.csv)|*.csv"
        fileDialog = wx.FileDialog(
            self, message="Choose File", wildcard=filter)
        result = fileDialog.ShowModal()
        if result == wx.ID_OK:
            path = fileDialog.GetPath()
            self.setDataFile(path)
        else:
            print "canceled"

    def setDataFile(self, path, passive=False):
        # if not path:
        #    path = self.model.dataFiles[self.DATAFILE.GetSelection()]
        self.model.setDataFile(path, passive)
        self.newVarSelector()

    def populate(self, model):
        m = self.model
        dfile = m.getDataFile()
        # if self.DATAFILE.FindString(dfile) == wx.NOT_FOUND and dfile:
        #    self.DATAFILE.Append(dfile)
        self.DATAFILE.SetValue(dfile)
        # vars = m.getVariables()
        # vars.insert(0,'Use Record Order')
        # if vars:
        #    self.IDVAR.Clear()
        #    self.IDVAR.AppendItems(vars)
        #    self.IDVAR.SetSelection(m.getIDVar())
        # vars.pop(0)
        self.setModelType(m.getModelType())
        mw = m.getMWeightsFiles()
        # if mw:
        self.MWeights_ListBox.SetItems([w.name for w in mw])
        self.MWeights_ListBox.SetCheckedStrings(
            [w.name for w in mw if w.enabled])
        kw = m.getKWeightsFiles()
        # if kw:
        self.KWeights_ListBox.SetItems([w.name for w in kw])
        self.KWeights_ListBox.SetCheckedStrings(
            [w.name for w in kw if w.enabled])
        self.setSpec(m.getSpec())
        self.setTitle()
        self.able()

    def notyet(self, e=None):
        print "Sorry, this feature is not yet implemented."

    def verbose(self, model):
        print self.model.data

    def run(self, evt):
        num_fixed = self.model.setMWeightsTransform('R')
        if num_fixed > 0:
            dialog = wx.MessageDialog(
                self, "The transform of %d model weights object(s) was set to\
                \"R: Row-standardization (global sum=n)\"" % num_fixed,
                "Model Weights Changed:",
                      wx.OK | wx.ICON_INFORMATION).ShowModal()
        self.model.data['config'] = self.config.GetPrefs()
        if self.config.model.output_save_pred_residuals:
            fname = self.model.data['fname']
            suggestion = os.path.split(
                fname)[1].split('.')[0] + '_predY_resid.csv'
            fileDialog = wx.FileDialog(
                self, defaultFile=suggestion, message="Save Predicted Values\
                and Residuals As...", wildcard="*.csv", style=wx.SAVE
                                                              + wx.OVERWRITE_PROMPT)
            if fileDialog.ShowModal() == wx.ID_OK:
                predy_resid = fileDialog.GetPath()
                print predy_resid
            else:
                return
        else:
            predy_resid = None
        try:
            pos = self.textFrame.Text.GetLastPosition()
            try:
                result = self.model.run(self.textFrame, predy_resid)
            except MemoryError:
                dialog = wx.MessageDialog(
                    self, "Your dataset is too large to perform this computation."
                          "Memory Error:", wx.OK | wx.ICON_ERROR)
                res = dialog.ShowModal()
                return False
            except Exception:
                et, e, tb = sys.exc_info()
                dialog = wx.MessageDialog(
                    self, "\"%s\"\nDisplay detailed error message in results\
                    window?" % str(e), "Model Error:",
                          wx.YES_NO | wx.ICON_ERROR)
                res = dialog.ShowModal()
                if res == wx.ID_YES:
                    traceback.print_tb(tb, file=self.textFrame)
                    self.textFrame.Text.SetInsertionPoint(pos)
                    self.textFrame.Show()
                    self.textFrame.Raise()
                return False
            if not result:  # model.verify failed
                cause = self.model.verify()[1]
                dialog = wx.MessageDialog(self, cause,
                                          "Model Error", wx.OK | wx.ICON_ERROR)
                dialog.ShowModal()
                return False
            self.results.extend(result)
            # self.textFrame.write(50*'='+'\n')
            # self.resultText.seek(0)
            # self.textFrame.Text.SetValue(self.resultText.read())
            self.textFrame.Text.SetInsertionPoint(pos)
            # self.textFrame.SetModified(True)
            self.textFrame.Show()
            self.textFrame.Raise()
        except KeyError:
            # commonly caused by no or incorrectly set ID Var.
            dialog = wx.MessageDialog(
                self, "Please check that the ID variable of your weights file\
                matches your data file or create a new weights file in\
                GeoDaWeights.", "The model failed to run. ",
                wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()
            raise
        except AttributeError:
            # commonly caused by no weights.
            if self.model.data['modelType']['error']['hac'] and not \
                    self.model.data['kWeights']:
                dialog = wx.MessageDialog(
                    self, "Kernel weights are required for HAC Standard\
                    Errors, please specify your kernel weights and try again.",
                    "The model failed to run.", wx.OK | wx.ICON_ERROR)
                dialog.ShowModal()
            else:
                dialog = wx.MessageDialog(
                    self, "Please be sure that you have specified your weights\
                    files correctly.", "The model failed to run. ",
                    wx.OK | wx.ICON_ERROR)
                dialog.ShowModal()
            raise
        except:
            dialog = wx.MessageDialog(
                self, "The model failed to run. Please Try Again.",
                "Error", wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()
            raise

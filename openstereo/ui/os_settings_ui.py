# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\os_settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 562)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.prop_projection_gcspacing = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.prop_projection_gcspacing.setObjectName("prop_projection_gcspacing")
        self.gridLayout_2.addWidget(self.prop_projection_gcspacing, 1, 4, 1, 1)
        self.prop_color_SC_colors = QtWidgets.QPushButton(self.groupBox_2)
        self.prop_color_SC_colors.setText("")
        self.prop_color_SC_colors.setObjectName("prop_color_SC_colors")
        self.gridLayout_2.addWidget(self.prop_color_SC_colors, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.prop_GC_linewidths = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.prop_GC_linewidths.setObjectName("prop_GC_linewidths")
        self.gridLayout_2.addWidget(self.prop_GC_linewidths, 1, 3, 1, 1)
        self.prop_color_GC_colors = QtWidgets.QPushButton(self.groupBox_2)
        self.prop_color_GC_colors.setText("")
        self.prop_color_GC_colors.setObjectName("prop_color_GC_colors")
        self.gridLayout_2.addWidget(self.prop_color_GC_colors, 1, 1, 1, 1)
        self.prop_GC_linestyles = QtWidgets.QComboBox(self.groupBox_2)
        self.prop_GC_linestyles.setObjectName("prop_GC_linestyles")
        self.prop_GC_linestyles.addItem("")
        self.prop_GC_linestyles.addItem("")
        self.prop_GC_linestyles.addItem("")
        self.prop_GC_linestyles.addItem("")
        self.gridLayout_2.addWidget(self.prop_GC_linestyles, 1, 2, 1, 1)
        self.prop_projection_scspacing = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.prop_projection_scspacing.setObjectName("prop_projection_scspacing")
        self.gridLayout_2.addWidget(self.prop_projection_scspacing, 2, 4, 1, 1)
        self.prop_SC_linestyles = QtWidgets.QComboBox(self.groupBox_2)
        self.prop_SC_linestyles.setObjectName("prop_SC_linestyles")
        self.prop_SC_linestyles.addItem("")
        self.prop_SC_linestyles.addItem("")
        self.prop_SC_linestyles.addItem("")
        self.prop_SC_linestyles.addItem("")
        self.gridLayout_2.addWidget(self.prop_SC_linestyles, 2, 2, 1, 1)
        self.prop_SC_linewidths = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.prop_SC_linewidths.setObjectName("prop_SC_linewidths")
        self.gridLayout_2.addWidget(self.prop_SC_linewidths, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prop_check_grid = QtWidgets.QCheckBox(self.groupBox_2)
        self.prop_check_grid.setObjectName("prop_check_grid")
        self.horizontalLayout_2.addWidget(self.prop_check_grid)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.prop_check_rotate = QtWidgets.QCheckBox(self.groupBox)
        self.prop_check_rotate.setObjectName("prop_check_rotate")
        self.gridLayout.addWidget(self.prop_check_rotate, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.prop_rotation_plng = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_rotation_plng.setMinimum(-90.0)
        self.prop_rotation_plng.setMaximum(90.0)
        self.prop_rotation_plng.setObjectName("prop_rotation_plng")
        self.gridLayout.addWidget(self.prop_rotation_plng, 1, 2, 1, 1)
        self.prop_rotation_azim = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_rotation_azim.setMinimum(-360.0)
        self.prop_rotation_azim.setMaximum(360.0)
        self.prop_rotation_azim.setObjectName("prop_rotation_azim")
        self.gridLayout.addWidget(self.prop_rotation_azim, 1, 1, 1, 1)
        self.prop_rotation_rake = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_rotation_rake.setMinimum(-360.0)
        self.prop_rotation_rake.setMaximum(360.0)
        self.prop_rotation_rake.setObjectName("prop_rotation_rake")
        self.gridLayout.addWidget(self.prop_rotation_rake, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.prop_check_cardinal = QtWidgets.QCheckBox(self.groupBox)
        self.prop_check_cardinal.setObjectName("prop_check_cardinal")
        self.horizontalLayout_6.addWidget(self.prop_check_cardinal)
        self.prop_check_cardinalborder = QtWidgets.QCheckBox(self.groupBox)
        self.prop_check_cardinalborder.setObjectName("prop_check_cardinalborder")
        self.horizontalLayout_6.addWidget(self.prop_check_cardinalborder)
        self.prop_projection_cardinalborder = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_projection_cardinalborder.setObjectName("prop_projection_cardinalborder")
        self.horizontalLayout_6.addWidget(self.prop_projection_cardinalborder)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.prop_check_colorbar = QtWidgets.QCheckBox(self.groupBox_4)
        self.prop_check_colorbar.setObjectName("prop_check_colorbar")
        self.gridLayout_4.addWidget(self.prop_check_colorbar, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 1, 1, 1)
        self.prop_general_colorbar = QtWidgets.QLineEdit(self.groupBox_4)
        self.prop_general_colorbar.setObjectName("prop_general_colorbar")
        self.gridLayout_4.addWidget(self.prop_general_colorbar, 0, 2, 1, 1)
        self.prop_check_colorbarpercentage = QtWidgets.QCheckBox(self.groupBox_4)
        self.prop_check_colorbarpercentage.setObjectName("prop_check_colorbarpercentage")
        self.gridLayout_4.addWidget(self.prop_check_colorbarpercentage, 1, 0, 1, 3)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)
        self.prop_color_mLine_color = QtWidgets.QPushButton(self.groupBox_5)
        self.prop_color_mLine_color.setText("")
        self.prop_color_mLine_color.setObjectName("prop_color_mLine_color")
        self.gridLayout_6.addWidget(self.prop_color_mLine_color, 1, 1, 1, 1)
        self.prop_mLine_linestyle = QtWidgets.QComboBox(self.groupBox_5)
        self.prop_mLine_linestyle.setObjectName("prop_mLine_linestyle")
        self.prop_mLine_linestyle.addItem("")
        self.prop_mLine_linestyle.addItem("")
        self.prop_mLine_linestyle.addItem("")
        self.prop_mLine_linestyle.addItem("")
        self.gridLayout_6.addWidget(self.prop_mLine_linestyle, 1, 2, 1, 1)
        self.prop_mLine_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.prop_mLine_linewidth.setObjectName("prop_mLine_linewidth")
        self.gridLayout_6.addWidget(self.prop_mLine_linewidth, 1, 3, 1, 1)
        self.prop_check_measurelinegc = QtWidgets.QCheckBox(self.groupBox_5)
        self.prop_check_measurelinegc.setObjectName("prop_check_measurelinegc")
        self.gridLayout_6.addWidget(self.prop_check_measurelinegc, 2, 0, 1, 1)
        self.prop_color_mGC_color = QtWidgets.QPushButton(self.groupBox_5)
        self.prop_color_mGC_color.setText("")
        self.prop_color_mGC_color.setObjectName("prop_color_mGC_color")
        self.gridLayout_6.addWidget(self.prop_color_mGC_color, 2, 1, 1, 1)
        self.prop_mGC_linestyle = QtWidgets.QComboBox(self.groupBox_5)
        self.prop_mGC_linestyle.setObjectName("prop_mGC_linestyle")
        self.prop_mGC_linestyle.addItem("")
        self.prop_mGC_linestyle.addItem("")
        self.prop_mGC_linestyle.addItem("")
        self.prop_mGC_linestyle.addItem("")
        self.gridLayout_6.addWidget(self.prop_mGC_linestyle, 2, 2, 1, 1)
        self.prop_mGC_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.prop_mGC_linewidth.setObjectName("prop_mGC_linewidth")
        self.gridLayout_6.addWidget(self.prop_mGC_linewidth, 2, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_11.addWidget(self.label_22)
        self.prop_general_projection = QtWidgets.QComboBox(self.tab)
        self.prop_general_projection.setObjectName("prop_general_projection")
        self.prop_general_projection.addItem("")
        self.prop_general_projection.addItem("")
        self.horizontalLayout_11.addWidget(self.prop_general_projection)
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_11.addWidget(self.label_23)
        self.prop_general_hemisphere = QtWidgets.QComboBox(self.tab)
        self.prop_general_hemisphere.setObjectName("prop_general_hemisphere")
        self.prop_general_hemisphere.addItem("")
        self.prop_general_hemisphere.addItem("")
        self.horizontalLayout_11.addWidget(self.prop_general_hemisphere)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.roseDiagram = QtWidgets.QWidget()
        self.roseDiagram.setObjectName("roseDiagram")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.roseDiagram)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_29 = QtWidgets.QLabel(self.groupBox_8)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 0, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_8)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 0, 3, 1, 1)
        self.prop_rose_check_outer = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_rose_check_outer.setObjectName("prop_rose_check_outer")
        self.gridLayout_5.addWidget(self.prop_rose_check_outer, 1, 0, 1, 1)
        self.prop_rose_outerperc = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_outerperc.setMaximum(100.0)
        self.prop_rose_outerperc.setObjectName("prop_rose_outerperc")
        self.gridLayout_5.addWidget(self.prop_rose_outerperc, 1, 1, 1, 1)
        self.prop_rose_outerwidth = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_outerwidth.setObjectName("prop_rose_outerwidth")
        self.gridLayout_5.addWidget(self.prop_rose_outerwidth, 1, 2, 1, 1)
        self.prop_color_rose_outerc = QtWidgets.QPushButton(self.groupBox_8)
        self.prop_color_rose_outerc.setText("")
        self.prop_color_rose_outerc.setObjectName("prop_color_rose_outerc")
        self.gridLayout_5.addWidget(self.prop_color_rose_outerc, 1, 3, 1, 1)
        self.prop_rose_check_rings = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_rose_check_rings.setObjectName("prop_rose_check_rings")
        self.gridLayout_5.addWidget(self.prop_rose_check_rings, 2, 0, 1, 1)
        self.prop_color_rose_ringsc = QtWidgets.QPushButton(self.groupBox_8)
        self.prop_color_rose_ringsc.setText("")
        self.prop_color_rose_ringsc.setObjectName("prop_color_rose_ringsc")
        self.gridLayout_5.addWidget(self.prop_color_rose_ringsc, 2, 3, 1, 1)
        self.prop_rose_diagonalswidth = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_diagonalswidth.setObjectName("prop_rose_diagonalswidth")
        self.gridLayout_5.addWidget(self.prop_rose_diagonalswidth, 3, 2, 1, 1)
        self.prop_rose_diagonalsang = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_diagonalsang.setMaximum(360.0)
        self.prop_rose_diagonalsang.setObjectName("prop_rose_diagonalsang")
        self.gridLayout_5.addWidget(self.prop_rose_diagonalsang, 3, 1, 1, 1)
        self.prop_rose_ringswidth = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_ringswidth.setObjectName("prop_rose_ringswidth")
        self.gridLayout_5.addWidget(self.prop_rose_ringswidth, 2, 2, 1, 1)
        self.prop_rose_diagonalsoff = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_diagonalsoff.setObjectName("prop_rose_diagonalsoff")
        self.gridLayout_5.addWidget(self.prop_rose_diagonalsoff, 4, 1, 1, 1)
        self.prop_color_rose_diagonalsc = QtWidgets.QPushButton(self.groupBox_8)
        self.prop_color_rose_diagonalsc.setText("")
        self.prop_color_rose_diagonalsc.setObjectName("prop_color_rose_diagonalsc")
        self.gridLayout_5.addWidget(self.prop_color_rose_diagonalsc, 3, 3, 1, 1)
        self.prop_rose_check_diagonals = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_rose_check_diagonals.setObjectName("prop_rose_check_diagonals")
        self.gridLayout_5.addWidget(self.prop_rose_check_diagonals, 3, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_8)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 4, 0, 1, 1)
        self.prop_rose_ringsperc = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_ringsperc.setMaximum(100.0)
        self.prop_rose_ringsperc.setObjectName("prop_rose_ringsperc")
        self.gridLayout_5.addWidget(self.prop_rose_ringsperc, 2, 1, 1, 1)
        self.prop_rose_check_autoscale = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_rose_check_autoscale.setObjectName("prop_rose_check_autoscale")
        self.gridLayout_5.addWidget(self.prop_rose_check_autoscale, 5, 0, 1, 2)
        self.prop_rose_check_scaletxt = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_rose_check_scaletxt.setObjectName("prop_rose_check_scaletxt")
        self.gridLayout_5.addWidget(self.prop_rose_check_scaletxt, 5, 2, 1, 1)
        self.prop_rose_scaleaz = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_scaleaz.setMinimum(-360.0)
        self.prop_rose_scaleaz.setMaximum(360.0)
        self.prop_rose_scaleaz.setObjectName("prop_rose_scaleaz")
        self.gridLayout_5.addWidget(self.prop_rose_scaleaz, 5, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.prop_rose_check_360d = QtWidgets.QRadioButton(self.groupBox_8)
        self.prop_rose_check_360d.setObjectName("prop_rose_check_360d")
        self.verticalLayout_5.addWidget(self.prop_rose_check_360d)
        self.prop_rose_check_180d = QtWidgets.QRadioButton(self.groupBox_8)
        self.prop_rose_check_180d.setObjectName("prop_rose_check_180d")
        self.verticalLayout_5.addWidget(self.prop_rose_check_180d)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.prop_rose_check_interval = QtWidgets.QRadioButton(self.groupBox_8)
        self.prop_rose_check_interval.setObjectName("prop_rose_check_interval")
        self.horizontalLayout_9.addWidget(self.prop_rose_check_interval)
        self.prop_rose_from = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_from.setMinimum(-360.0)
        self.prop_rose_from.setMaximum(360.0)
        self.prop_rose_from.setObjectName("prop_rose_from")
        self.horizontalLayout_9.addWidget(self.prop_rose_from)
        self.prop_rose_to = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.prop_rose_to.setMinimum(-360.0)
        self.prop_rose_to.setMaximum(360.0)
        self.prop_rose_to.setObjectName("prop_rose_to")
        self.horizontalLayout_9.addWidget(self.prop_rose_to)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 199, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.groupBox_8.raise_()
        self.tabWidget.addTab(self.roseDiagram, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, -1, 6)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.prop_general_title = QtWidgets.QLineEdit(self.tab_2)
        self.prop_general_title.setObjectName("prop_general_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prop_general_title)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.prop_general_description = QtWidgets.QTextEdit(self.tab_2)
        self.prop_general_description.setObjectName("prop_general_description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prop_general_description)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.prop_general_author = QtWidgets.QLineEdit(self.tab_2)
        self.prop_general_author.setObjectName("prop_general_author")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prop_general_author)
        self.show_file_name = QtWidgets.QLineEdit(self.tab_2)
        self.show_file_name.setReadOnly(True)
        self.show_file_name.setObjectName("show_file_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.show_file_name)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.prop_general_lastsave = QtWidgets.QLabel(self.tab_2)
        self.prop_general_lastsave.setObjectName("prop_general_lastsave")
        self.horizontalLayout_4.addWidget(self.prop_general_lastsave)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.prop_general_packeddata = QtWidgets.QLabel(self.tab_2)
        self.prop_general_packeddata.setObjectName("prop_general_packeddata")
        self.horizontalLayout_3.addWidget(self.prop_general_packeddata)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.do_actions_unpack = QtWidgets.QPushButton(self.tab_2)
        self.do_actions_unpack.setObjectName("do_actions_unpack")
        self.horizontalLayout_3.addWidget(self.do_actions_unpack)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setObjectName("apply")
        self.horizontalLayout.addWidget(self.apply)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.ok_button.clicked.connect(Dialog.accept)
        self.cancel_button.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.prop_color_GC_colors)
        Dialog.setTabOrder(self.prop_color_GC_colors, self.prop_GC_linestyles)
        Dialog.setTabOrder(self.prop_GC_linestyles, self.prop_GC_linewidths)
        Dialog.setTabOrder(self.prop_GC_linewidths, self.prop_projection_gcspacing)
        Dialog.setTabOrder(self.prop_projection_gcspacing, self.prop_color_SC_colors)
        Dialog.setTabOrder(self.prop_color_SC_colors, self.prop_SC_linestyles)
        Dialog.setTabOrder(self.prop_SC_linestyles, self.prop_SC_linewidths)
        Dialog.setTabOrder(self.prop_SC_linewidths, self.prop_projection_scspacing)
        Dialog.setTabOrder(self.prop_projection_scspacing, self.prop_check_grid)
        Dialog.setTabOrder(self.prop_check_grid, self.prop_check_rotate)
        Dialog.setTabOrder(self.prop_check_rotate, self.prop_rotation_azim)
        Dialog.setTabOrder(self.prop_rotation_azim, self.prop_rotation_plng)
        Dialog.setTabOrder(self.prop_rotation_plng, self.prop_rotation_rake)
        Dialog.setTabOrder(self.prop_rotation_rake, self.prop_check_cardinal)
        Dialog.setTabOrder(self.prop_check_cardinal, self.prop_check_cardinalborder)
        Dialog.setTabOrder(self.prop_check_cardinalborder, self.prop_projection_cardinalborder)
        Dialog.setTabOrder(self.prop_projection_cardinalborder, self.prop_check_colorbar)
        Dialog.setTabOrder(self.prop_check_colorbar, self.prop_general_colorbar)
        Dialog.setTabOrder(self.prop_general_colorbar, self.prop_check_colorbarpercentage)
        Dialog.setTabOrder(self.prop_check_colorbarpercentage, self.prop_color_mLine_color)
        Dialog.setTabOrder(self.prop_color_mLine_color, self.prop_mLine_linestyle)
        Dialog.setTabOrder(self.prop_mLine_linestyle, self.prop_mLine_linewidth)
        Dialog.setTabOrder(self.prop_mLine_linewidth, self.prop_check_measurelinegc)
        Dialog.setTabOrder(self.prop_check_measurelinegc, self.prop_color_mGC_color)
        Dialog.setTabOrder(self.prop_color_mGC_color, self.prop_mGC_linestyle)
        Dialog.setTabOrder(self.prop_mGC_linestyle, self.prop_mGC_linewidth)
        Dialog.setTabOrder(self.prop_mGC_linewidth, self.prop_general_projection)
        Dialog.setTabOrder(self.prop_general_projection, self.prop_general_hemisphere)
        Dialog.setTabOrder(self.prop_general_hemisphere, self.prop_rose_check_rings)
        Dialog.setTabOrder(self.prop_rose_check_rings, self.prop_rose_ringsperc)
        Dialog.setTabOrder(self.prop_rose_ringsperc, self.prop_color_rose_ringsc)
        Dialog.setTabOrder(self.prop_color_rose_ringsc, self.prop_rose_check_diagonals)
        Dialog.setTabOrder(self.prop_rose_check_diagonals, self.prop_rose_diagonalsang)
        Dialog.setTabOrder(self.prop_rose_diagonalsang, self.prop_color_rose_diagonalsc)
        Dialog.setTabOrder(self.prop_color_rose_diagonalsc, self.prop_rose_check_360d)
        Dialog.setTabOrder(self.prop_rose_check_360d, self.prop_rose_check_180d)
        Dialog.setTabOrder(self.prop_rose_check_180d, self.prop_rose_check_interval)
        Dialog.setTabOrder(self.prop_rose_check_interval, self.prop_rose_from)
        Dialog.setTabOrder(self.prop_rose_from, self.prop_rose_to)
        Dialog.setTabOrder(self.prop_rose_to, self.show_file_name)
        Dialog.setTabOrder(self.show_file_name, self.prop_general_title)
        Dialog.setTabOrder(self.prop_general_title, self.prop_general_description)
        Dialog.setTabOrder(self.prop_general_description, self.prop_general_author)
        Dialog.setTabOrder(self.prop_general_author, self.do_actions_unpack)
        Dialog.setTabOrder(self.do_actions_unpack, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.ok_button)
        Dialog.setTabOrder(self.ok_button, self.prop_color_rose_outerc)
        Dialog.setTabOrder(self.prop_color_rose_outerc, self.prop_rose_outerperc)
        Dialog.setTabOrder(self.prop_rose_outerperc, self.apply)
        Dialog.setTabOrder(self.apply, self.prop_rose_check_outer)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Grid"))
        self.label_20.setText(_translate("Dialog", "Small Circles"))
        self.label_17.setText(_translate("Dialog", "Great Circles"))
        self.label_10.setText(_translate("Dialog", "Spacing"))
        self.label_4.setText(_translate("Dialog", "Symbol"))
        self.label_6.setText(_translate("Dialog", "Width"))
        self.label_5.setText(_translate("Dialog", "Color"))
        self.prop_GC_linestyles.setItemText(0, _translate("Dialog", "-"))
        self.prop_GC_linestyles.setItemText(1, _translate("Dialog", ":"))
        self.prop_GC_linestyles.setItemText(2, _translate("Dialog", "--"))
        self.prop_GC_linestyles.setItemText(3, _translate("Dialog", "-."))
        self.prop_SC_linestyles.setItemText(0, _translate("Dialog", "-"))
        self.prop_SC_linestyles.setItemText(1, _translate("Dialog", ":"))
        self.prop_SC_linestyles.setItemText(2, _translate("Dialog", "--"))
        self.prop_SC_linestyles.setItemText(3, _translate("Dialog", "-."))
        self.prop_check_grid.setText(_translate("Dialog", "Plot Grid"))
        self.groupBox.setTitle(_translate("Dialog", "Rotation"))
        self.label_2.setText(_translate("Dialog", "Plunge"))
        self.prop_check_rotate.setText(_translate("Dialog", "Rotate Grid"))
        self.label_3.setText(_translate("Dialog", "Rake"))
        self.label.setText(_translate("Dialog", "Azimuth"))
        self.prop_check_cardinal.setText(_translate("Dialog", "Cardinal Points"))
        self.prop_check_cardinalborder.setText(_translate("Dialog", "Border width:"))
        self.groupBox_4.setTitle(_translate("Dialog", "Contouring"))
        self.prop_check_colorbar.setText(_translate("Dialog", "Plot Colorbar"))
        self.label_21.setText(_translate("Dialog", "Colorbar Label:"))
        self.prop_check_colorbarpercentage.setText(_translate("Dialog", "Plot as Percentage"))
        self.groupBox_5.setTitle(_translate("Dialog", "Measure Line"))
        self.label_26.setText(_translate("Dialog", "Color"))
        self.label_28.setText(_translate("Dialog", "Symbol"))
        self.label_25.setText(_translate("Dialog", "Width"))
        self.label_24.setText(_translate("Dialog", "Line"))
        self.prop_mLine_linestyle.setItemText(0, _translate("Dialog", "-"))
        self.prop_mLine_linestyle.setItemText(1, _translate("Dialog", ":"))
        self.prop_mLine_linestyle.setItemText(2, _translate("Dialog", "--"))
        self.prop_mLine_linestyle.setItemText(3, _translate("Dialog", "-."))
        self.prop_check_measurelinegc.setText(_translate("Dialog", "Great Circle"))
        self.prop_mGC_linestyle.setItemText(0, _translate("Dialog", "-"))
        self.prop_mGC_linestyle.setItemText(1, _translate("Dialog", ":"))
        self.prop_mGC_linestyle.setItemText(2, _translate("Dialog", "--"))
        self.prop_mGC_linestyle.setItemText(3, _translate("Dialog", "-."))
        self.label_22.setText(_translate("Dialog", "Projection:"))
        self.prop_general_projection.setItemText(0, _translate("Dialog", "Equal-Area"))
        self.prop_general_projection.setItemText(1, _translate("Dialog", "Equal-Angle"))
        self.label_23.setText(_translate("Dialog", "Hemisphere:"))
        self.prop_general_hemisphere.setItemText(0, _translate("Dialog", "Lower"))
        self.prop_general_hemisphere.setItemText(1, _translate("Dialog", "Upper"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Projection"))
        self.groupBox_8.setTitle(_translate("Dialog", "Rose grid"))
        self.label_29.setText(_translate("Dialog", "Width"))
        self.label_27.setText(_translate("Dialog", "Color"))
        self.prop_rose_check_outer.setText(_translate("Dialog", "Outer (%)"))
        self.prop_rose_check_rings.setText(_translate("Dialog", "Rings (%)"))
        self.prop_rose_check_diagonals.setText(_translate("Dialog", "Diagonals"))
        self.label_30.setText(_translate("Dialog", "Offset"))
        self.prop_rose_check_autoscale.setText(_translate("Dialog", "Set Outer Limit from data"))
        self.prop_rose_check_scaletxt.setText(_translate("Dialog", "Plot Scale at:"))
        self.prop_rose_check_360d.setText(_translate("Dialog", "360 degrees"))
        self.prop_rose_check_180d.setText(_translate("Dialog", "180 degrees"))
        self.prop_rose_check_interval.setText(_translate("Dialog", "Interval:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.roseDiagram), _translate("Dialog", "Rose Diagram"))
        self.label_7.setText(_translate("Dialog", "File:"))
        self.label_8.setText(_translate("Dialog", "Title:"))
        self.label_9.setText(_translate("Dialog", "Description:"))
        self.label_11.setText(_translate("Dialog", "Author:"))
        self.label_14.setText(_translate("Dialog", "Last Saved:"))
        self.prop_general_lastsave.setText(_translate("Dialog", "savetime"))
        self.label_12.setText(_translate("Dialog", "Packed Data:"))
        self.prop_general_packeddata.setText(_translate("Dialog", "packed"))
        self.do_actions_unpack.setText(_translate("Dialog", "Unpack to..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Project"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.apply.setText(_translate("Dialog", "Apply"))


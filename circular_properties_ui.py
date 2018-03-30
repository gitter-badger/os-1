# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'circular_properties.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 502)
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
        self.roseDiagram = QtWidgets.QWidget()
        self.roseDiagram.setObjectName("roseDiagram")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.roseDiagram)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_16 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.prop_rose_check_standard = QtWidgets.QRadioButton(self.groupBox_16)
        self.prop_rose_check_standard.setObjectName("prop_rose_check_standard")
        self.gridLayout_5.addWidget(self.prop_rose_check_standard, 0, 0, 1, 1)
        self.prop_rose_binwidth = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_binwidth.setMaximum(360.0)
        self.prop_rose_binwidth.setObjectName("prop_rose_binwidth")
        self.gridLayout_5.addWidget(self.prop_rose_binwidth, 0, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_16)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 1, 1, 1)
        self.prop_rose_offset = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_offset.setMinimum(-360.0)
        self.prop_rose_offset.setMaximum(360.0)
        self.prop_rose_offset.setObjectName("prop_rose_offset")
        self.gridLayout_5.addWidget(self.prop_rose_offset, 0, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_16)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_16)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 1, 1, 1, 1)
        self.prop_rose_check_continuous = QtWidgets.QRadioButton(self.groupBox_16)
        self.prop_rose_check_continuous.setObjectName("prop_rose_check_continuous")
        self.gridLayout_5.addWidget(self.prop_rose_check_continuous, 1, 0, 1, 1)
        self.prop_rose_aperture = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_aperture.setMaximum(360.0)
        self.prop_rose_aperture.setObjectName("prop_rose_aperture")
        self.gridLayout_5.addWidget(self.prop_rose_aperture, 1, 2, 1, 1)
        self.prop_rose_weightmunro = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_weightmunro.setMaximum(1.0)
        self.prop_rose_weightmunro.setSingleStep(0.01)
        self.prop_rose_weightmunro.setObjectName("prop_rose_weightmunro")
        self.gridLayout_5.addWidget(self.prop_rose_weightmunro, 1, 4, 1, 1)
        self.prop_rose_check_weightmunro = QtWidgets.QCheckBox(self.groupBox_16)
        self.prop_rose_check_weightmunro.setObjectName("prop_rose_check_weightmunro")
        self.gridLayout_5.addWidget(self.prop_rose_check_weightmunro, 1, 3, 1, 1)
        self.prop_rose_spacing = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_spacing.setMaximum(360.0)
        self.prop_rose_spacing.setObjectName("prop_rose_spacing")
        self.gridLayout_5.addWidget(self.prop_rose_spacing, 2, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_16)
        self.label_38.setObjectName("label_38")
        self.gridLayout_5.addWidget(self.label_38, 2, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_16)
        self.label_39.setObjectName("label_39")
        self.gridLayout_5.addWidget(self.label_39, 2, 3, 1, 1)
        self.prop_rose_offsetcont = QtWidgets.QDoubleSpinBox(self.groupBox_16)
        self.prop_rose_offsetcont.setMinimum(-360.0)
        self.prop_rose_offsetcont.setMaximum(360.0)
        self.prop_rose_offsetcont.setObjectName("prop_rose_offsetcont")
        self.gridLayout_5.addWidget(self.prop_rose_offsetcont, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_16, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.prop_rose_check_petalsfill = QtWidgets.QCheckBox(self.groupBox_7)
        self.prop_rose_check_petalsfill.setObjectName("prop_rose_check_petalsfill")
        self.gridLayout_8.addWidget(self.prop_rose_check_petalsfill, 0, 1, 1, 1)
        self.prop_rose_check_petalsoutline = QtWidgets.QCheckBox(self.groupBox_7)
        self.prop_rose_check_petalsoutline.setObjectName("prop_rose_check_petalsoutline")
        self.gridLayout_8.addWidget(self.prop_rose_check_petalsoutline, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_7)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 0, 3, 1, 1)
        self.prop_rose_check_petals = QtWidgets.QRadioButton(self.groupBox_7)
        self.prop_rose_check_petals.setObjectName("prop_rose_check_petals")
        self.gridLayout_8.addWidget(self.prop_rose_check_petals, 1, 0, 1, 1)
        self.prop_color_petals_facecolor = QtWidgets.QPushButton(self.groupBox_7)
        self.prop_color_petals_facecolor.setText("")
        self.prop_color_petals_facecolor.setObjectName("prop_color_petals_facecolor")
        self.gridLayout_8.addWidget(self.prop_color_petals_facecolor, 1, 1, 1, 1)
        self.prop_color_petals_edgecolor = QtWidgets.QPushButton(self.groupBox_7)
        self.prop_color_petals_edgecolor.setText("")
        self.prop_color_petals_edgecolor.setObjectName("prop_color_petals_edgecolor")
        self.gridLayout_8.addWidget(self.prop_color_petals_edgecolor, 1, 2, 1, 1)
        self.prop_petals_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.prop_petals_linewidth.setObjectName("prop_petals_linewidth")
        self.gridLayout_8.addWidget(self.prop_petals_linewidth, 1, 3, 1, 1)
        self.prop_rose_check_kitefill = QtWidgets.QCheckBox(self.groupBox_7)
        self.prop_rose_check_kitefill.setObjectName("prop_rose_check_kitefill")
        self.gridLayout_8.addWidget(self.prop_rose_check_kitefill, 2, 1, 1, 1)
        self.prop_rose_check_kiteoutline = QtWidgets.QCheckBox(self.groupBox_7)
        self.prop_rose_check_kiteoutline.setObjectName("prop_rose_check_kiteoutline")
        self.gridLayout_8.addWidget(self.prop_rose_check_kiteoutline, 2, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_7)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 2, 3, 1, 1)
        self.prop_rose_check_kite = QtWidgets.QRadioButton(self.groupBox_7)
        self.prop_rose_check_kite.setObjectName("prop_rose_check_kite")
        self.gridLayout_8.addWidget(self.prop_rose_check_kite, 3, 0, 1, 1)
        self.prop_color_kite_facecolor = QtWidgets.QPushButton(self.groupBox_7)
        self.prop_color_kite_facecolor.setText("")
        self.prop_color_kite_facecolor.setObjectName("prop_color_kite_facecolor")
        self.gridLayout_8.addWidget(self.prop_color_kite_facecolor, 3, 1, 1, 1)
        self.prop_color_kite_edgecolor = QtWidgets.QPushButton(self.groupBox_7)
        self.prop_color_kite_edgecolor.setText("")
        self.prop_color_kite_edgecolor.setObjectName("prop_color_kite_edgecolor")
        self.gridLayout_8.addWidget(self.prop_color_kite_edgecolor, 3, 2, 1, 1)
        self.prop_kite_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.prop_kite_linewidth.setObjectName("prop_kite_linewidth")
        self.gridLayout_8.addWidget(self.prop_kite_linewidth, 3, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setObjectName("label_29")
        self.gridLayout_8.addWidget(self.label_29, 4, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 4, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 4, 3, 1, 1)
        self.prop_rose_check_lines = QtWidgets.QRadioButton(self.groupBox_7)
        self.prop_rose_check_lines.setObjectName("prop_rose_check_lines")
        self.gridLayout_8.addWidget(self.prop_rose_check_lines, 5, 0, 1, 1)
        self.prop_lines_linestyle = QtWidgets.QComboBox(self.groupBox_7)
        self.prop_lines_linestyle.setObjectName("prop_lines_linestyle")
        self.prop_lines_linestyle.addItem("")
        self.prop_lines_linestyle.addItem("")
        self.prop_lines_linestyle.addItem("")
        self.prop_lines_linestyle.addItem("")
        self.gridLayout_8.addWidget(self.prop_lines_linestyle, 5, 1, 1, 1)
        self.prop_color_lines_color = QtWidgets.QPushButton(self.groupBox_7)
        self.prop_color_lines_color.setText("")
        self.prop_color_lines_color.setObjectName("prop_color_lines_color")
        self.gridLayout_8.addWidget(self.prop_color_lines_color, 5, 2, 1, 1)
        self.prop_lines_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.prop_lines_linewidth.setObjectName("prop_lines_linewidth")
        self.gridLayout_8.addWidget(self.prop_lines_linewidth, 5, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.prop_rose_check_meandeviation = QtWidgets.QCheckBox(self.groupBox_7)
        self.prop_rose_check_meandeviation.setObjectName("prop_rose_check_meandeviation")
        self.horizontalLayout_11.addWidget(self.prop_rose_check_meandeviation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 1, 2, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.prop_rose_check_diraxial = QtWidgets.QCheckBox(self.groupBox_5)
        self.prop_rose_check_diraxial.setObjectName("prop_rose_check_diraxial")
        self.verticalLayout_3.addWidget(self.prop_rose_check_diraxial)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.prop_rose_check_weightcolumn = QtWidgets.QCheckBox(self.groupBox_5)
        self.prop_rose_check_weightcolumn.setObjectName("prop_rose_check_weightcolumn")
        self.horizontalLayout_8.addWidget(self.prop_rose_check_weightcolumn)
        self.prop_rose_weightcolumn = QtWidgets.QSpinBox(self.groupBox_5)
        self.prop_rose_weightcolumn.setMaximum(16384)
        self.prop_rose_weightcolumn.setObjectName("prop_rose_weightcolumn")
        self.horizontalLayout_8.addWidget(self.prop_rose_weightcolumn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 0, 2, 1, 1)
        self.prop_rose_mean_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.prop_rose_mean_linewidth.setObjectName("prop_rose_mean_linewidth")
        self.gridLayout_7.addWidget(self.prop_rose_mean_linewidth, 1, 3, 1, 1)
        self.prop_color_rose_mean_color = QtWidgets.QPushButton(self.groupBox_9)
        self.prop_color_rose_mean_color.setText("")
        self.prop_color_rose_mean_color.setObjectName("prop_color_rose_mean_color")
        self.gridLayout_7.addWidget(self.prop_color_rose_mean_color, 1, 2, 1, 1)
        self.prop_rose_check_mean = QtWidgets.QCheckBox(self.groupBox_9)
        self.prop_rose_check_mean.setObjectName("prop_rose_check_mean")
        self.gridLayout_7.addWidget(self.prop_rose_check_mean, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 0, 3, 1, 1)
        self.prop_rose_mean_linestyle = QtWidgets.QComboBox(self.groupBox_9)
        self.prop_rose_mean_linestyle.setObjectName("prop_rose_mean_linestyle")
        self.prop_rose_mean_linestyle.addItem("")
        self.prop_rose_mean_linestyle.addItem("")
        self.prop_rose_mean_linestyle.addItem("")
        self.prop_rose_mean_linestyle.addItem("")
        self.gridLayout_7.addWidget(self.prop_rose_mean_linestyle, 1, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 0, 1, 1, 1)
        self.prop_rose_check_confidence = QtWidgets.QCheckBox(self.groupBox_9)
        self.prop_rose_check_confidence.setObjectName("prop_rose_check_confidence")
        self.gridLayout_7.addWidget(self.prop_rose_check_confidence, 2, 1, 1, 2)
        self.prop_rose_confidence = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.prop_rose_confidence.setMaximum(100.0)
        self.prop_rose_confidence.setObjectName("prop_rose_confidence")
        self.gridLayout_7.addWidget(self.prop_rose_confidence, 2, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_7)
        self.gridLayout_2.addWidget(self.groupBox_9, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.roseDiagram)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.prop_rose_check_360d = QtWidgets.QRadioButton(self.groupBox_6)
        self.prop_rose_check_360d.setObjectName("prop_rose_check_360d")
        self.verticalLayout_4.addWidget(self.prop_rose_check_360d)
        self.prop_rose_check_180d = QtWidgets.QRadioButton(self.groupBox_6)
        self.prop_rose_check_180d.setObjectName("prop_rose_check_180d")
        self.verticalLayout_4.addWidget(self.prop_rose_check_180d)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.prop_rose_check_interval = QtWidgets.QRadioButton(self.groupBox_6)
        self.prop_rose_check_interval.setObjectName("prop_rose_check_interval")
        self.horizontalLayout_9.addWidget(self.prop_rose_check_interval)
        self.prop_rose_intervalfrom = QtWidgets.QSpinBox(self.groupBox_6)
        self.prop_rose_intervalfrom.setMinimum(-360)
        self.prop_rose_intervalfrom.setMaximum(360)
        self.prop_rose_intervalfrom.setObjectName("prop_rose_intervalfrom")
        self.horizontalLayout_9.addWidget(self.prop_rose_intervalfrom)
        self.prop_rose_intervalto = QtWidgets.QSpinBox(self.groupBox_6)
        self.prop_rose_intervalto.setMinimum(-360)
        self.prop_rose_intervalto.setMaximum(360)
        self.prop_rose_intervalto.setObjectName("prop_rose_intervalto")
        self.horizontalLayout_9.addWidget(self.prop_rose_intervalto)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addWidget(self.groupBox_6, 2, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.tabWidget.addTab(self.roseDiagram, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.show_auttitude_data_statistics = QtWidgets.QTextEdit(self.tab_3)
        self.show_auttitude_data_statistics.setObjectName("show_auttitude_data_statistics")
        self.horizontalLayout_6.addWidget(self.show_auttitude_data_statistics)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.show_auttitude_data_source = QtWidgets.QTextEdit(self.tab_4)
        self.show_auttitude_data_source.setObjectName("show_auttitude_data_source")
        self.horizontalLayout_7.addWidget(self.show_auttitude_data_source)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        Dialog.setTabOrder(self.show_auttitude_data_source, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.apply)
        Dialog.setTabOrder(self.apply, self.show_auttitude_data_statistics)
        Dialog.setTabOrder(self.show_auttitude_data_statistics, self.ok_button)
        Dialog.setTabOrder(self.ok_button, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.prop_rose_check_standard)
        Dialog.setTabOrder(self.prop_rose_check_standard, self.prop_rose_binwidth)
        Dialog.setTabOrder(self.prop_rose_binwidth, self.prop_rose_offset)
        Dialog.setTabOrder(self.prop_rose_offset, self.prop_rose_check_continuous)
        Dialog.setTabOrder(self.prop_rose_check_continuous, self.prop_rose_aperture)
        Dialog.setTabOrder(self.prop_rose_aperture, self.prop_rose_check_weightmunro)
        Dialog.setTabOrder(self.prop_rose_check_weightmunro, self.prop_rose_weightmunro)
        Dialog.setTabOrder(self.prop_rose_weightmunro, self.prop_rose_spacing)
        Dialog.setTabOrder(self.prop_rose_spacing, self.prop_rose_offsetcont)
        Dialog.setTabOrder(self.prop_rose_offsetcont, self.prop_rose_check_diraxial)
        Dialog.setTabOrder(self.prop_rose_check_diraxial, self.prop_rose_check_weightcolumn)
        Dialog.setTabOrder(self.prop_rose_check_weightcolumn, self.prop_rose_weightcolumn)
        Dialog.setTabOrder(self.prop_rose_weightcolumn, self.prop_rose_check_mean)
        Dialog.setTabOrder(self.prop_rose_check_mean, self.prop_rose_mean_linestyle)
        Dialog.setTabOrder(self.prop_rose_mean_linestyle, self.prop_color_rose_mean_color)
        Dialog.setTabOrder(self.prop_color_rose_mean_color, self.prop_rose_mean_linewidth)
        Dialog.setTabOrder(self.prop_rose_mean_linewidth, self.prop_rose_check_confidence)
        Dialog.setTabOrder(self.prop_rose_check_confidence, self.prop_rose_confidence)
        Dialog.setTabOrder(self.prop_rose_confidence, self.prop_rose_check_petals)
        Dialog.setTabOrder(self.prop_rose_check_petals, self.prop_rose_check_petalsfill)
        Dialog.setTabOrder(self.prop_rose_check_petalsfill, self.prop_rose_check_petalsoutline)
        Dialog.setTabOrder(self.prop_rose_check_petalsoutline, self.prop_color_petals_facecolor)
        Dialog.setTabOrder(self.prop_color_petals_facecolor, self.prop_color_petals_edgecolor)
        Dialog.setTabOrder(self.prop_color_petals_edgecolor, self.prop_petals_linewidth)
        Dialog.setTabOrder(self.prop_petals_linewidth, self.prop_rose_check_kite)
        Dialog.setTabOrder(self.prop_rose_check_kite, self.prop_rose_check_kitefill)
        Dialog.setTabOrder(self.prop_rose_check_kitefill, self.prop_rose_check_kiteoutline)
        Dialog.setTabOrder(self.prop_rose_check_kiteoutline, self.prop_color_kite_facecolor)
        Dialog.setTabOrder(self.prop_color_kite_facecolor, self.prop_color_kite_edgecolor)
        Dialog.setTabOrder(self.prop_color_kite_edgecolor, self.prop_kite_linewidth)
        Dialog.setTabOrder(self.prop_kite_linewidth, self.prop_rose_check_lines)
        Dialog.setTabOrder(self.prop_rose_check_lines, self.prop_lines_linestyle)
        Dialog.setTabOrder(self.prop_lines_linestyle, self.prop_color_lines_color)
        Dialog.setTabOrder(self.prop_color_lines_color, self.prop_lines_linewidth)
        Dialog.setTabOrder(self.prop_lines_linewidth, self.prop_rose_check_meandeviation)
        Dialog.setTabOrder(self.prop_rose_check_meandeviation, self.prop_rose_check_360d)
        Dialog.setTabOrder(self.prop_rose_check_360d, self.prop_rose_check_180d)
        Dialog.setTabOrder(self.prop_rose_check_180d, self.prop_rose_check_interval)
        Dialog.setTabOrder(self.prop_rose_check_interval, self.prop_rose_intervalfrom)
        Dialog.setTabOrder(self.prop_rose_intervalfrom, self.prop_rose_intervalto)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_16.setTitle(_translate("Dialog", "Counting Method"))
        self.prop_rose_check_standard.setText(_translate("Dialog", "Standard"))
        self.label_18.setText(_translate("Dialog", "Bin Width"))
        self.label_24.setText(_translate("Dialog", "Offset"))
        self.label_19.setText(_translate("Dialog", "Aperture"))
        self.prop_rose_check_continuous.setText(_translate("Dialog", "Continuous"))
        self.prop_rose_check_weightmunro.setText(_translate("Dialog", "Weight"))
        self.label_38.setText(_translate("Dialog", "Spacing"))
        self.label_39.setText(_translate("Dialog", "Offset"))
        self.groupBox_7.setTitle(_translate("Dialog", "Graphic Properties"))
        self.prop_rose_check_petalsfill.setText(_translate("Dialog", "Fill"))
        self.prop_rose_check_petalsoutline.setText(_translate("Dialog", "Outline"))
        self.label_20.setText(_translate("Dialog", "Width"))
        self.prop_rose_check_petals.setText(_translate("Dialog", "Petals"))
        self.prop_rose_check_kitefill.setText(_translate("Dialog", "Fill"))
        self.prop_rose_check_kiteoutline.setText(_translate("Dialog", "Outline"))
        self.label_22.setText(_translate("Dialog", "Width"))
        self.prop_rose_check_kite.setText(_translate("Dialog", "Kite"))
        self.label_29.setText(_translate("Dialog", "Style"))
        self.label_28.setText(_translate("Dialog", "Color"))
        self.label_27.setText(_translate("Dialog", "Size"))
        self.prop_rose_check_lines.setText(_translate("Dialog", "Lines"))
        self.prop_lines_linestyle.setItemText(0, _translate("Dialog", ":"))
        self.prop_lines_linestyle.setItemText(1, _translate("Dialog", "-"))
        self.prop_lines_linestyle.setItemText(2, _translate("Dialog", "--"))
        self.prop_lines_linestyle.setItemText(3, _translate("Dialog", "-."))
        self.prop_rose_check_meandeviation.setText(_translate("Dialog", "Mean Deviation"))
        self.groupBox_5.setTitle(_translate("Dialog", "Data"))
        self.prop_rose_check_diraxial.setText(_translate("Dialog", "Axial"))
        self.prop_rose_check_weightcolumn.setText(_translate("Dialog", "Weight by column:"))
        self.groupBox_9.setTitle(_translate("Dialog", "Mean direction"))
        self.label_25.setText(_translate("Dialog", "Color"))
        self.prop_rose_check_mean.setText(_translate("Dialog", "Show"))
        self.label_26.setText(_translate("Dialog", "Size"))
        self.prop_rose_mean_linestyle.setItemText(0, _translate("Dialog", "-"))
        self.prop_rose_mean_linestyle.setItemText(1, _translate("Dialog", ":"))
        self.prop_rose_mean_linestyle.setItemText(2, _translate("Dialog", "--"))
        self.prop_rose_mean_linestyle.setItemText(3, _translate("Dialog", "-."))
        self.label_37.setText(_translate("Dialog", "Style"))
        self.prop_rose_check_confidence.setText(_translate("Dialog", "Confidence Interval (%)"))
        self.groupBox_6.setTitle(_translate("Dialog", "Type"))
        self.prop_rose_check_360d.setText(_translate("Dialog", "360 degrees"))
        self.prop_rose_check_180d.setText(_translate("Dialog", "180 degrees"))
        self.prop_rose_check_interval.setText(_translate("Dialog", "Interval:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.roseDiagram), _translate("Dialog", "Rose Diagram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Data Source"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.apply.setText(_translate("Dialog", "Apply"))

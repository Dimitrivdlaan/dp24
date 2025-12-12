from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout, QTextEdit,QSizePolicy 
from PyQt6.QtCore import *
from PyQt6.QtGui import QFont, QPixmap
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as QFigureCanvas
from sqlalchemy import create_engine
import sys
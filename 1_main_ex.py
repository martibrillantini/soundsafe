# Only needed for access to command line arguments
import sys
import logging
import random
import csv
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QCalendarWidget, QDialog, QHBoxLayout, QListWidget, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QCalendarWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt
import csv
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
# We import the PyQt5 classes that we need for the application
# from the QtWidgets module
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QCalendarWidget, QListWidget, QMessageBox, QInputDialog, QDialog
)
from PyQt5.QtCore import QDate, Qt
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPainter, QPdfWriter, QPixmap, QRegExpValidator, QFont
from PyQt5.QtWidgets import QDialog, QCalendarWidget
from PyQt5.QtCore import (
    QObject,
    Qt, 
    QMetaObject, 
    QSettings,
    QThread,
    QThreadPool, 
    QRunnable, 
    pyqtSignal, 
    QRegExp,
    pyqtSlot
)

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QGraphicsScene,
    QGraphicsView, 
    QTabWidget, 
    QMenu, 
    QLineEdit,
    QFileDialog, 
    QDialog, 
    QSlider, 
    QMessageBox, 
    QDoubleSpinBox, 
    QDialogButtonBox,
    QMenuBar,
    QAction,
    QMainWindow,
    QPushButton,
    QComboBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

# Logging config
logging.basicConfig(format="%(message)s", level=logging.INFO)

# Path to files to store data
file_path = r'C:\Users\marty\OneDrive\Desktop\POLIMI\quinto\lab cerveri\user_data.csv'
appointments_file_path = r'C:\Users\marty\OneDrive\Desktop\POLIMI\quinto\lab cerveri\bookings.csv'

# Class for DOCTORS 
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QListWidget, QMessageBox, QHBoxLayout
import csv

import csv
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QListWidget, QMessageBox, QLabel

appointments_file_path = r'C:\Users\marty\OneDrive\Desktop\POLIMI\quinto\lab cerveri\bookings.csv'  # Replace with your actual file path


from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QListWidget, QMessageBox, QLabel
)
import csv

class LinkLetterClass(QDialog):
    def __init__(self, main_window=None):
        super().__init__()
        self.setWindowTitle('Dr. Grant Linkletter')
        self.setGeometry(100, 100, 600, 400)
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.view_confirmed_appointments_button = QPushButton('View Confirmed Appointments')
        self.view_confirmed_appointments_button.clicked.connect(self.view_confirmed_appointments)

        self.view_unconfirmed_appointments_button = QPushButton('View Appointments to be Confirmed')
        self.view_unconfirmed_appointments_button.clicked.connect(self.view_unconfirmed_appointments)

        self.logout_button = QPushButton('Log Out')
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.view_confirmed_appointments_button)
        self.layout.addWidget(self.view_unconfirmed_appointments_button)
        self.layout.addWidget(self.logout_button)

        self.appointments_file_path = 'appointments.csv'
        self.booked_appointments = self.load_appointments()

    def load_appointments(self):
        appointments = {}
        try:
            with open(self.appointments_file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        date_str, doctor, operation, time, confirmed, patient_name = row[:6]  # Adjust to match your CSV structure
                        if doctor.strip().lower() == 'dr. linkletter':
                            if date_str not in appointments:
                                appointments[date_str] = {}
                            appointments[date_str][doctor] = {
                                'operation': operation,
                                'time': time,
                                'confirmed': confirmed == 'True',
                                'patient_name': patient_name
                            }
                    except ValueError as e:
                        print(f"Error parsing row: {row}. Error: {e}")
        except FileNotFoundError:
            print(f"File not found: {self.appointments_file_path}")
        return appointments

    def save_appointments(self):
        with open(self.appointments_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for date_str, doctors in self.booked_appointments.items():
                for doctor, details in doctors.items():
                    writer.writerow([
                        date_str,
                        doctor,
                        details['operation'],
                        details['time'],
                        'True' if details['confirmed'] else 'False',
                        details['patient_name']
                    ])

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def view_confirmed_appointments(self):
        self.clear_layout(self.layout)

        self.confirmed_list = QListWidget()

        for date, doctors in self.booked_appointments.items():
            for doctor, details in doctors.items():
                if doctor == 'Dr. Linkletter' and details['confirmed']:
                    operation = details['operation']
                    time = details['time']
                    patient_name = details['patient_name']
                    self.confirmed_list.addItem(f"{date} - {operation} - {time} - Patient: {patient_name}")

        self.confirmed_list.itemClicked.connect(self.show_confirmed_appointment_details)

        self.layout.addWidget(QLabel("Confirmed Appointments"))
        self.layout.addWidget(self.confirmed_list)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.back_button)



    def view_unconfirmed_appointments(self):
        self.clear_layout(self.layout)

        self.unconfirmed_list = QListWidget()

        for date, doctors in self.booked_appointments.items():
            for doctor, details in doctors.items():
                if not details['confirmed']:
                    operation = details['operation']
                    time = details['time']
                    patient_name = details['patient_name']
                    self.unconfirmed_list.addItem(f"{date} - {operation} - {time} - Patient: {patient_name}")

        self.unconfirmed_list.itemClicked.connect(self.show_unconfirmed_appointment_details)

        self.layout.addWidget(QLabel("Unconfirmed Appointments"))
        self.layout.addWidget(self.unconfirmed_list)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.back_button)

    def show_confirmed_appointment_details(self, item):
        appointment_str = item.text()
        try:
            date_str, operation, time, patient_str = appointment_str.split(' - ')
            patient_name = patient_str.split(': ')[1]  # Extract patient name
            confirm_dialog = QMessageBox.question(self, 'Delete Appointment', f'Are you sure you want to delete the appointment on {date_str} at {time} for {operation} for patient {patient_name}?',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                del self.booked_appointments[date_str]['Dr. Linkletter']
                if not self.booked_appointments[date_str]:
                    del self.booked_appointments[date_str]
                self.save_appointments()
                QMessageBox.information(self, 'Deleted', f'Appointment on {date_str} at {time} deleted.')
                self.view_confirmed_appointments()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Error parsing appointment details.')

    def show_unconfirmed_appointment_details(self, item):
        appointment_str = item.text()
        try:
            date_str, operation, time, patient_str = appointment_str.split(' - ')
            patient_name = patient_str.split(': ')[1]  # Extract patient name
            confirm_dialog = QMessageBox.question(self, 'Confirm Appointment', f'Do you want to confirm the appointment on {date_str} at {time} for {operation} for patient {patient_name}?',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                self.booked_appointments[date_str]['Dr. Linkletter']['confirmed'] = True
                self.save_appointments()
                QMessageBox.information(self, 'Confirmed', f'Appointment on {date_str} at {time} confirmed.')
                self.view_unconfirmed_appointments()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Error parsing appointment details.')

    def show_main_options(self):
        self.clear_layout(self.layout)

        self.view_confirmed_appointments_button = QPushButton('View Confirmed Appointments')
        self.view_unconfirmed_appointments_button = QPushButton('View Appointments to be Confirmed')
        self.logout_button = QPushButton('Log Out')

        self.view_confirmed_appointments_button.clicked.connect(self.view_confirmed_appointments)
        self.view_unconfirmed_appointments_button.clicked.connect(self.view_unconfirmed_appointments)
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.view_confirmed_appointments_button)
        self.layout.addWidget(self.view_unconfirmed_appointments_button)
        self.layout.addWidget(self.logout_button)

    def logout(self):
        self.hide()
        self.main_window.show()

    def closeEvent(self, event):
        self.logout()


class SturgisClass(QDialog):
    def __init__(self, main_window=None):
        super().__init__()
        self.setWindowTitle('Dr. John Sturgis')
        self.setGeometry(100, 100, 600, 400)
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.view_confirmed_appointments_button = QPushButton('View Confirmed Appointments')
        self.view_confirmed_appointments_button.clicked.connect(self.view_confirmed_appointments)

        self.view_unconfirmed_appointments_button = QPushButton('View Appointments to be Confirmed')
        self.view_unconfirmed_appointments_button.clicked.connect(self.view_unconfirmed_appointments)

        self.logout_button = QPushButton('Log Out')
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.view_confirmed_appointments_button)
        self.layout.addWidget(self.view_unconfirmed_appointments_button)
        self.layout.addWidget(self.logout_button)

        self.appointments_file_path = 'appointments.csv'
        self.booked_appointments = self.load_appointments()

    def load_appointments(self):
        appointments = {}
        try:
            with open(self.appointments_file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        date_str, doctor, operation, time, confirmed, patient_name = row[:6]  # Adjust to match your CSV structure
                        if doctor.strip().lower() == 'dr. sturgis':
                            if date_str not in appointments:
                                appointments[date_str] = {}
                            appointments[date_str][doctor] = {
                                'operation': operation,
                                'time': time,
                                'confirmed': confirmed == 'True',
                                'patient_name': patient_name
                            }
                    except ValueError as e:
                        print(f"Error parsing row: {row}. Error: {e}")
        except FileNotFoundError:
            print(f"File not found: {self.appointments_file_path}")
        return appointments

    def save_appointments(self):
        with open(self.appointments_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for date_str, doctors in self.booked_appointments.items():
                for doctor, details in doctors.items():
                    writer.writerow([
                        date_str,
                        doctor,
                        details['operation'],
                        details['time'],
                        'True' if details['confirmed'] else 'False',
                        details['patient_name']
                    ])

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def view_confirmed_appointments(self):
        self.clear_layout(self.layout)

        self.confirmed_list = QListWidget()

        for date, doctors in self.booked_appointments.items():
            for doctor, details in doctors.items():
                if doctor == 'Dr. Sturgis' and details['confirmed']:
                    operation = details['operation']
                    time = details['time']
                    patient_name = details['patient_name']
                    self.confirmed_list.addItem(f"{date} - {operation} - {time} - Patient: {patient_name}")

        self.confirmed_list.itemClicked.connect(self.show_confirmed_appointment_details)

        self.layout.addWidget(QLabel("Confirmed Appointments"))
        self.layout.addWidget(self.confirmed_list)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.back_button)

    def view_unconfirmed_appointments(self):
        self.clear_layout(self.layout)

        self.unconfirmed_list = QListWidget()

        for date, doctors in self.booked_appointments.items():
            for doctor, details in doctors.items():
                if not details['confirmed']:
                    operation = details['operation']
                    time = details['time']
                    patient_name = details['patient_name']
                    self.unconfirmed_list.addItem(f"{date} - {operation} - {time} - Patient: {patient_name}")

        self.unconfirmed_list.itemClicked.connect(self.show_unconfirmed_appointment_details)

        self.layout.addWidget(QLabel("Unconfirmed Appointments"))
        self.layout.addWidget(self.unconfirmed_list)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.back_button)

    def show_confirmed_appointment_details(self, item):
        appointment_str = item.text()
        try:
            date_str, operation, time, patient_str = appointment_str.split(' - ')
            patient_name = patient_str.split(': ')[1]  # Extract patient name
            confirm_dialog = QMessageBox.question(self, 'Delete Appointment', f'Are you sure you want to delete the appointment on {date_str} at {time} for {operation} for patient {patient_name}?',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                del self.booked_appointments[date_str]['Dr. Sturgis']
                if not self.booked_appointments[date_str]:
                    del self.booked_appointments[date_str]
                self.save_appointments()
                QMessageBox.information(self, 'Deleted', f'Appointment on {date_str} at {time} deleted.')
                self.view_confirmed_appointments()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Error parsing appointment details.')

    def show_unconfirmed_appointment_details(self, item):
        appointment_str = item.text()
        try:
            date_str, operation, time, patient_str = appointment_str.split(' - ')
            patient_name = patient_str.split(': ')[1]  # Extract patient name
            confirm_dialog = QMessageBox.question(self, 'Confirm Appointment', f'Do you want to confirm the appointment on {date_str} at {time} for {operation} for patient {patient_name}?',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                self.booked_appointments[date_str]['Dr. Sturgis']['confirmed'] = True
                self.save_appointments()
                QMessageBox.information(self, 'Confirmed', f'Appointment on {date_str} at {time} confirmed.')
                self.view_unconfirmed_appointments()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Error parsing appointment details.')

    def show_main_options(self):
        self.clear_layout(self.layout)

        self.view_confirmed_appointments_button = QPushButton('View Confirmed Appointments')
        self.view_unconfirmed_appointments_button = QPushButton('View Appointments to be Confirmed')
        self.logout_button = QPushButton('Log Out')

        self.view_confirmed_appointments_button.clicked.connect(self.view_confirmed_appointments)
        self.view_unconfirmed_appointments_button.clicked.connect(self.view_unconfirmed_appointments)
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.view_confirmed_appointments_button)
        self.layout.addWidget(self.view_unconfirmed_appointments_button)
        self.layout.addWidget(self.logout_button)

    def logout(self):
        self.hide()
        self.main_window.show()

    def closeEvent(self, event):
        self.logout()


# Class for PATIENTS (booking / canceling / confirming appointments) --> CalendarWindow
import csv
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QCalendarWidget,
    QMessageBox, QListWidget, QLineEdit, QInputDialog, QDateEdit, QDateTimeEdit
)
from PyQt5.QtCore import QDate

import csv
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QCalendarWidget,
    QMessageBox, QListWidget, QLineEdit, QInputDialog, QDateEdit, QDateTimeEdit
)
from PyQt5.QtCore import QDate

import csv
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QCalendarWidget,
    QMessageBox, QListWidget, QLineEdit, QInputDialog, QDateEdit, QDateTimeEdit
)
from PyQt5.QtCore import QDate

class CalendarWindow(QDialog):
    def __init__(self, main_window=None, patient_email=None):
        super().__init__()
        self.setWindowTitle('Patient Calendar')
        self.setGeometry(100, 100, 600, 400)
        self.main_window = main_window
        self.patient_email = patient_email

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.book_appointment_button = QPushButton('Book an Appointment')
        self.book_appointment_button.clicked.connect(self.book_appointment)

        self.view_appointments_button = QPushButton('See Booked Appointments')
        self.view_appointments_button.clicked.connect(self.view_appointments)

        self.search_appointments_button = QPushButton('Search Available Appointments')
        self.search_appointments_button.clicked.connect(self.search_appointments)

        self.logout_button = QPushButton('Log Out')
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.book_appointment_button)
        self.layout.addWidget(self.view_appointments_button)
        self.layout.addWidget(self.search_appointments_button)
        self.layout.addWidget(self.logout_button)

        self.booked_appointments = self.load_appointments()

    def load_appointments(self):
        appointments = {}
        try:
            with open('appointments.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    date_str, doctor, operation, time, confirmed, patient_email = row
                    if date_str not in appointments:
                        appointments[date_str] = {}
                    if doctor not in appointments[date_str]:
                        appointments[date_str][doctor] = {}
                    appointments[date_str][doctor][time] = {
                        'operation': operation,
                        'confirmed': confirmed == 'True',
                        'patient_email': patient_email
                    }
        except FileNotFoundError:
            pass
        return appointments

    def save_appointments(self):
        with open('appointments.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for date_str, doctors in self.booked_appointments.items():
                for doctor, times in doctors.items():
                    for time, details in times.items():
                        confirmed_str = 'True' if details['confirmed'] else 'False'
                        writer.writerow([date_str, doctor, details['operation'], time, confirmed_str, details['patient_email']])

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def book_appointment(self):
        self.clear_layout(self.layout)

        self.setup_doctor_selection()
        self.setup_operation_selection()

        self.go_on_button = QPushButton('Go On')
        self.go_on_button.clicked.connect(self.show_calendar)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.go_on_button)
        self.layout.addWidget(self.back_button)

    def setup_doctor_selection(self):
        self.doctor_combo_box = QComboBox()
        self.doctor_combo_box.addItem('Select Doctor')
        self.doctor_combo_box.addItem('Dr. Sturgis')
        self.doctor_combo_box.addItem('Dr. Linkletter')
        self.doctor_combo_box.currentIndexChanged.connect(self.doctor_selected)
        self.layout.addWidget(self.doctor_combo_box)

    def setup_operation_selection(self):
        self.operation_combo_box = QComboBox()
        self.operation_combo_box.addItem('Select Operation')
        self.operation_combo_box.addItem('Bypass Surgery')
        self.operation_combo_box.addItem('Balloon Angioplasty')
        self.operation_combo_box.addItem('Heart Valve Surgery')
        self.operation_combo_box.currentIndexChanged.connect(self.operation_selected)
        self.layout.addWidget(self.operation_combo_box)

    def doctor_selected(self, index):
        self.selected_doctor = self.doctor_combo_box.currentText()

    def operation_selected(self, index):
        self.selected_operation = self.operation_combo_box.currentText()

    def show_calendar(self):
        if self.doctor_combo_box.currentIndex() == 0 or self.operation_combo_box.currentIndex() == 0:
            QMessageBox.warning(self, 'Selection Required', 'Please select both a doctor and an operation.')
            return

        self.clear_layout(self.layout)

        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.clicked[QDate].connect(self.date_selected)
        self.layout.addWidget(self.calendar_widget)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.book_appointment)
        self.layout.addWidget(self.back_button)

    def date_selected(self, date):
        current_date = QDate.currentDate()
        if date < current_date:
            QMessageBox.warning(self, 'Invalid Date', 'You cannot select a past date.')
            return

        date_str = date.toString("yyyy-MM-dd")

        times = ['9:00 am', '3:00 pm'] if self.selected_doctor == 'Dr. Sturgis' else ['10:00 am', '2:00 pm']
        time, ok = QInputDialog.getItem(self, 'Select Time', f'Select a time for {self.selected_doctor} on {date_str}:', times, 0, False)

        if ok:
            if self.is_appointment_slot_available(date_str, self.selected_doctor, time):
                confirm_dialog = QMessageBox.question(self, 'Confirm Appointment', f'Book {self.selected_doctor} for {self.selected_operation} on {date_str} at {time}?',
                                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if confirm_dialog == QMessageBox.Yes:
                    if date_str not in self.booked_appointments:
                        self.booked_appointments[date_str] = {}
                    if self.selected_doctor not in self.booked_appointments[date_str]:
                        self.booked_appointments[date_str][self.selected_doctor] = {}
                    self.booked_appointments[date_str][self.selected_doctor][time] = {
                        'operation': self.selected_operation,
                        'confirmed': False,
                        'patient_email': self.patient_email
                    }
                    self.save_appointments()
                    QMessageBox.information(self, 'Success', f'Appointment booked for {self.selected_doctor} on {date_str} at {time}.')
                    self.show_main_options()
                else:
                    QMessageBox.information(self, 'Cancelled', 'Appointment booking cancelled.')
            else:
                QMessageBox.warning(self, 'Error', 'The selected date, time, and doctor are already booked. Please select another slot.')

    def is_appointment_slot_available(self, date_str, doctor, time):
        return date_str not in self.booked_appointments or doctor not in self.booked_appointments[date_str] or time not in self.booked_appointments[date_str][doctor]

    def view_appointments(self):
        self.clear_layout(self.layout)

        self.appointments_list = QListWidget()
        for date, doctors in self.booked_appointments.items():
            for doctor, times in doctors.items():
                for time, details in times.items():
                    if details['patient_email'] == self.patient_email:
                        operation = details['operation']
                        confirmed = details['confirmed']
                        confirmed_str = 'Yes' if confirmed else 'No'
                        self.appointments_list.addItem(f"{date} - {doctor} - {operation} - {time} - Confirmed: {confirmed_str}")
        self.appointments_list.itemClicked.connect(self.show_appointment_details)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(self.appointments_list)
        self.layout.addWidget(self.back_button)

    def show_appointment_details(self, item):
        appointment_str = item.text()
        try:
            date_str, doctor, operation, time, confirmed_str = appointment_str.split(' - ')
            confirmed = 'Yes' in confirmed_str

            detail_msg = f'Appointment on {date_str}\nDoctor: {doctor}\nOperation: {operation}\nTime: {time}\nConfirmed: {"Yes" if confirmed else "No"}'
            detail_dialog = QMessageBox.question(self, 'Appointment Details', f'{detail_msg}\n\nDo you want to delete this appointment?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if detail_dialog == QMessageBox.Yes:
                del self.booked_appointments[date_str][doctor][time]
                if not self.booked_appointments[date_str][doctor]:
                    del self.booked_appointments[date_str][doctor]
                if not self.booked_appointments[date_str]:
                    del self.booked_appointments[date_str]
                self.save_appointments()
                QMessageBox.information(self, 'Deleted', f'Appointment on {date_str} with {doctor} at {time} deleted.')
                self.view_appointments()  # Refresh the list
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Error parsing appointment details.')

    def search_appointments(self):
        self.clear_layout(self.layout)

        self.date_edit = QDateEdit(calendarPopup=True)
        self.date_edit.setDate(QDate.currentDate())
        self.doctor_line_edit = QLineEdit()
        self.doctor_line_edit.setPlaceholderText('Enter doctor')

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.perform_search)

        self.search_results_list = QListWidget()

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_options)

        self.layout.addWidget(QLabel('Search by Date:'))
        self.layout.addWidget(self.date_edit)
        self.layout.addWidget(QLabel('Search by Doctor:'))
        self.layout.addWidget(self.doctor_line_edit)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.search_results_list)
        self.layout.addWidget(self.back_button)

    def perform_search(self):
        search_date = self.date_edit.date().toString("yyyy-MM-dd")
        search_doctor = self.doctor_line_edit.text()

        self.search_results_list.clear()

        available_slots = self.get_available_slots(search_date, search_doctor)

        if available_slots:
            for slot in available_slots:
                self.search_results_list.addItem(slot)
        else:
            self.search_results_list.addItem('No available slots found.')

    def get_available_slots(self, search_date, search_doctor):
        available_slots = []

        # Define possible slots for doctors
        all_slots = {
            'Dr. Sturgis': ['9:00 am', '3:00 pm'],
            'Dr. Linkletter': ['10:00 am', '2:00 pm']
        }

        # Read appointments from the CSV file
        booked_appointments = self.load_appointments()

        for doctor, slots in all_slots.items():
            if search_doctor and search_doctor != doctor:
                continue
            for time in slots:
                if search_date and not self.is_appointment_slot_available(search_date, doctor, time):
                    continue
                available_slots.append(f"{search_date} - {doctor} - {time}")

        return available_slots

    def show_main_options(self):
        self.clear_layout(self.layout)

        self.layout.addWidget(QLabel(f'Logged in as: {self.patient_email}'))

        self.book_appointment_button = QPushButton('Book an Appointment')
        self.book_appointment_button.clicked.connect(self.book_appointment)
        self.view_appointments_button = QPushButton('See Booked Appointments')
        self.view_appointments_button.clicked.connect(self.view_appointments)
        self.search_appointments_button = QPushButton('Search Available Appointments')
        self.search_appointments_button.clicked.connect(self.search_appointments)
        self.logout_button = QPushButton('Log Out')
        self.logout_button.clicked.connect(self.logout)

        self.layout.addWidget(self.book_appointment_button)
        self.layout.addWidget(self.view_appointments_button)
        self.layout.addWidget(self.search_appointments_button)
        self.layout.addWidget(self.logout_button)

    def logout(self):
        self.close()
        self.main_window.show()

    def closeEvent(self, event):
        self.logout()




 

# First Window: LOGIN or SIGNIN --> InitialWindow        
class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')
        width = 400
        height = 200
        self.setMinimumSize(width, height)

        # Create widgets
        self.register_button = QPushButton('Register')
        self.login_button = QPushButton('Login')

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Connect buttons to slots
        self.register_button.clicked.connect(self.open_register_window)
        self.login_button.clicked.connect(self.open_login_window)

    def open_register_window(self):
        self.data_entry_window = DataEntryWindow(self)
        self.data_entry_window.show()
        self.close()

    def open_login_window(self):
        self.login_window = LoginWindow(self) ##########
        self.login_window.show()
        self.close()

# Sign in --> DataEntryWindow
        
class DataEntryWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('Registration')
        width = 600
        height = 600
        self.setMinimumSize(width,height)
        self.main_window = main_window #############

        # Create widgets
        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()
        self.surname_label = QLabel('Surname:')
        self.surname_edit = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_edit = QLineEdit()
        self.sex_label = QLabel('Sex:')
        self.sex_combo_box = QComboBox()
        self.sex_combo_box.addItem("")  #
        self.sex_combo_box.addItem("Man")
        self.sex_combo_box.addItem("Woman")
        self.age_label = QLabel('Age:')
        self.age_combo = QComboBox()
        self.age_combo.addItem("")  # 
        self.age_combo.addItems([str(i) for i in range(1, 100)])
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_label = QLabel('Confirm Password:')
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)
        self.user_type_label = QLabel('User Type:')
        self.user_type_combo_box = QComboBox()
        self.user_type_combo_box.addItem("")
        self.user_type_combo_box.addItem("Patient")
        self.user_type_combo_box.addItem("Doctor")       
        self.send_button = QPushButton('Send')
        self.send_button.setEnabled(False)
        self.back_button = QPushButton('Back') 

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_edit)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.sex_label)
        layout.addWidget(self.sex_combo_box)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_combo)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_edit)
        layout.addWidget(self.user_type_label)
        layout.addWidget(self.user_type_combo_box)
        layout.addWidget(self.send_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        
        # Create a validator to check the email format
        #email_validator = QRegExpValidator(QRegExp(".+@.+"))  
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.email_validator = QRegExpValidator(QRegExp(email_regex))
        
        # Set the validator for the email edit field
        #self.email_edit.setValidator(email_validator)
        self.email_edit.setValidator(self.email_validator)
        
        # Connect the textChanged signal of the email edit field to a slot
        self.email_edit.textChanged.connect(self.validate_fields)
        
        # Connect the textChanged signal of the name / surname edit field to a slot
        self.name_edit.textChanged.connect(self.validate_fields)
        self.surname_edit.textChanged.connect(self.validate_fields)
        
        # Connect the currentIndexChanged signal of the sex and age combo boxes to a slot
        self.sex_combo_box.currentIndexChanged.connect(self.validate_fields)
        self.age_combo.currentIndexChanged.connect(self.validate_fields)

        # Connect the textChanged signal of the password and confirm password fields to a slot
        self.password_edit.textChanged.connect(self.validate_fields)
        self.confirm_password_edit.textChanged.connect(self.validate_fields)

        # Connect the currentIndexChanged signal of the user type combo box to a slot
        self.user_type_combo_box.currentIndexChanged.connect(self.validate_fields)
           
        self.name_edit.textChanged.connect(self.capitalized_text_changed)
        self.surname_edit.textChanged.connect(self.capitalized_text_changed)
        
        # Connect button signal to slot
        #self.send_button.clicked.connect(self.openMainWindow)
        self.send_button.clicked.connect(self.register_user)  
        self.back_button.clicked.connect(self.go_back)  

    def go_back(self):
        self.close()
        self.main_window.show()
        
    def register_user(self):
        # Code to register the user and store their information in a CSV file
        user_type = self.user_type_combo_box.currentText()
        email = self.email_edit.text()
        password = self.password_edit.text()
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        sex = self.sex_combo_box.currentText()
        age = self.age_combo.currentText()
        
        # Write user information to a CSV file
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([email, password, name, surname, sex, age, user_type])
        
        #self.openLogin()
        self.close()
        self.openNextWindow(user_type, email)  # Pass user_email to openNextWindow

                    
    def capitalized_text_changed(self, text):
        # Capitalize the first letter of the text
        capitalized_text = text.capitalize()

        # Update the text in the corresponding QLineEdit widget
        sender = self.sender()
        if isinstance(sender, QLineEdit):
            sender.setText(capitalized_text)
            
    def validate_fields(self):
        # Enable or disable the Send button based on the field validity
        is_name_valid = bool(self.name_edit.text())
        is_surname_valid = bool(self.surname_edit.text())
        #is_email_valid = self.email_edit.hasAcceptableInput()
        is_email_valid = self.email_edit.hasAcceptableInput() and self.validate_email(self.email_edit.text())
        is_sex_valid = self.sex_combo_box.currentIndex() != 0
        is_age_valid = self.age_combo.currentIndex() != 0
        is_password_valid = bool(self.password_edit.text())
        is_confirm_password_valid = bool(self.confirm_password_edit.text())
        do_passwords_match = self.password_edit.text() == self.confirm_password_edit.text()
        is_user_type_valid = self.user_type_combo_box.currentIndex() != 0
        is_fields_valid = (
            is_name_valid and is_surname_valid and is_email_valid and
            is_sex_valid and is_age_valid and is_password_valid and
            is_confirm_password_valid and do_passwords_match and
            is_user_type_valid
        )

        self.send_button.setEnabled(is_fields_valid)

    def validate_email(self, email):
        # Additional validation for email domain
        common_domains = [
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"
        ]
        domain = email.split('@')[-1]
        if domain not in common_domains:
            QMessageBox.warning(self, 'Invalid Email Domain', 'Please use a common email domain.')
            return False
        return True
    
    def openLogin(self):
        self.close()
        self.login_window = LoginWindow(self)
        self.login_window.show()
        
    def openNextWindow(self, user_type, user_email):
        if user_type == "Patient":
            calendar_window = CalendarWindow(self.main_window, user_email)  # Pass user_email to CalendarWindow
            calendar_window.exec_()
        elif user_type == "Doctor":
            if 'linkletter' in user_email.lower():
                doctor_window = LinkLetterClass(self.main_window)
            elif 'sturgis' in user_email.lower():
                # You need to implement SturgisClass similarly to LinkLetterClass
                doctor_window = SturgisClass(self.main_window)
            doctor_window.exec_()
            


# Login --> LoginWindow

class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        
        self.main_window = main_window #############

        self.setWindowTitle('Login')
        width = 400
        height = 200
        self.setMinimumSize(width, height)
        
        # Create widgets
        self.email_label = QLabel('Email:')
        self.email_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.back_button = QPushButton('Back')  # Add back button
        
        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

        # Create a validator to check the email format
        email_validator = QRegExpValidator(QtCore.QRegExp(".+@.+"))

        # Set the validator for the email edit field
        self.email_edit.setValidator(email_validator)

        # Connect button signal to slot
        self.login_button.clicked.connect(self.login_user)
        self.back_button.clicked.connect(self.go_back)  
        
    def go_back(self):
        self.close()
        self.main_window.show()

    def login_user(self):
        email = self.email_edit.text()
        password = self.password_edit.text()
        user_type, user_email = self.verify_credentials(email, password)
        if user_type:
            self.close()  # Close the login window
            self.openNextWindow(user_type, user_email)  # Pass user_email to openNextWindow
        else:
            # Show error message
            QMessageBox.warning(self, 'Error', 'Invalid email or password')

    def verify_credentials(self, email, password):
        # Code to verify credentials and retrieve user type from CSV file
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                stored_email, stored_password, user_type = row[0], row[1], row[-1]
                if stored_email == email and stored_password == password:
                    return user_type, email  # Return user_email along with user_type
        return None, None

    def openNextWindow(self, user_type, user_email):
        if user_type == "Patient":
            calendar_window = CalendarWindow(self.main_window, user_email)  # Pass user_email to CalendarWindow
            calendar_window.exec_()
        elif user_type == "Doctor":
            if 'linkletter' in user_email.lower():
                doctor_window = LinkLetterClass(self.main_window)
            elif 'sturgis' in user_email.lower():
                # You need to implement SturgisClass similarly to LinkLetterClass
                doctor_window = SturgisClass(self.main_window)
            doctor_window.exec_()






###############
# MAIN WINDOW #
###############
# This is a pre-made widget which provides a lot of standard window 
# features you’ll make use of in your apps, including toolbars, menus, 
# a statusbar, dockable widgets and more.
class MainWindow(QMainWindow):
     def __init__(self, name, surname, email, sex, age):
        """!
        @brief Init MainWindow.
        """
        # If you want to create a custom window, the best approach is 
        # to subclass QMainWindow and then include the setup for the 
        # window in this __init__ block.

        super(MainWindow, self).__init__()

        # title and geometry

        
        ###
        # title and geometry
        self.setWindowTitle("PulseCheck - "f' {name}' f' {surname}')
        width = 1200
        height = 600
        self.setMinimumSize(width, height)
        
        self.name = name
        self.surname = surname
        self.email = email
        self.sex = sex
        self.age = age

        #self.initUI()

    #####################
    # GRAPHIC INTERFACE #
    #####################
 
#############
#  RUN APP  #
#############
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([])
    # works too.
    app = QApplication(sys.argv)
    #data_entry_window = DataEntryWindow()
    #data_entry_window.show()
    initial_window = InitialWindow()
    initial_window.show()
    # Create a Qt widget, which will be our window.
    #w = MainWindow()
    #w.show() # IMPORTANT!!!!! Windows are hidden by default.
    # Start the event loop.
    sys.exit(app.exec_())

    # Your application won't reach here until you exit and the event
    # loop has stopped.
    
    
    ##

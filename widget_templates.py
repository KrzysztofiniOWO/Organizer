from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore


def create_image(path):
    """Function to make creating new images easier in our app"""

    #We import our image
    pixmap = QPixmap(path)

    #We set our image on logo and style it a bit
    img = QLabel()
    img.setPixmap(pixmap)
    img.setAlignment(QtCore.Qt.AlignCenter)
    img.setStyleSheet("margin-top: 30px;")

    return img


def create_button(text, connection, width, height):
    """Function to make creating new buttons easier in our app"""

    #We create button and make it interactive
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    #We connect our button to class it's supposed to work with
    button.clicked.connect(connection)
    button.setFixedWidth(width)
    button.setFixedHeight(height)

    #We make stylesheet for our button with padding
    button.setStyleSheet(
        "*{font-size: 35px;" +
        "color: '#233142';" +
        "padding: 25px 20px;" +
        "background: '#a44f82';" +
        "margin: 10px 10px;" +
        "border: 5px solid '#683b6b';" +
        "text-align: center;}" +
        "*:hover{background: '#f36d9a';}"
    )

    return button


def create_user_input(text, width, height):
    """Function to make creating user input fields easier in our app"""

    #We create input box and set text in it
    input_box = QLineEdit(text)

    #We set height and width for our input box
    input_box.setFixedHeight(height)
    input_box.setFixedWidth(width)

    # We make stylesheet for our input box
    input_box.setStyleSheet(
        "*{font-size: 35px;" +
        "color: '#121b27';" +
        "padding: 10px 10px;" +
        "margin: 10px 10px;" +
        "background: '#a44f82';" +
        "border: 5px solid '#683b6b';}"
    )

    return input_box


def create_event_label(text):
    """Function to make creating labels for events easier in our app"""

    #We create label and fill it with given text
    label = QLabel(text)

    #We set size of our label
    label.setFixedHeight(60)

    # We make stylesheet for our label
    label.setStyleSheet(
        "font-size: 18px;" +
        "background: '#a44f82';"
    )

    return label


def create_event_button(text, connection, width, height):
    """Function to make creating new event buttons easier in our app"""

    # We create button and make it interactive
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # We connect our button to class it's supposed to work with
    button.clicked.connect(connection)
    button.setFixedWidth(width)
    button.setFixedHeight(height)

    # We make stylesheet for our button with padding
    button.setStyleSheet(
        "*{font-size: 25px;" +
        "color: '#233142';" +
        "padding: 10px 15px;" +
        "background: '#a44f82';" +
        "margin: 10px 10px;" +
        "border: 5px solid '#683b6b';" +
        "text-align: center;}" +
        "*:hover{background: '#f36d9a';}"
    )

    return button


def create_event_group_box(name, date, description, edit_function, delete_function):
    """Function to make creating group boxes for events easier in our app"""

    # We create group box
    group_box = QGroupBox()

    group_box.setFixedWidth(700)
    group_box.setFixedHeight(100)

    #We set values for an event
    text_label = create_event_label(f"{name} | {date} | {description}")
    settings_button = create_event_button("Edit", edit_function, 100, 80)
    delete_button = create_event_button("Del", delete_function, 100, 80)

    #We create grid and add elements to it
    vbox = QGridLayout()
    vbox.addWidget(text_label, 0, 0)
    vbox.addWidget(settings_button, 0, 1)
    vbox.addWidget(delete_button, 0, 2)

    group_box.setLayout(vbox)

    group_box.setStyleSheet("QGroupBox { background: '#a44f82';" +
                            "border: 5px solid '#683b6b';}")

    return group_box


def create_message_box(text):
    """Function to make creating message boxes for events easier in our app"""

    #We create message box
    message_box = QMessageBox()

    #We set our text
    message_box.setText(text)

    return message_box








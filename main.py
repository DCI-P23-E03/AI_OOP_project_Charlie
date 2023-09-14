from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, 
                             QTextEdit, QWidget, QLineEdit, QScrollArea)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class BusinessIdeaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'IdeaAlchemy: Craft Your Success'
        self.description = (
            "Innovative idea generator based on your skills, interests, and resources — your key to optimal business proposals! "
            "Say goodbye to endless searches for the perfect business concept — now everything is easy and swift.\\n\\n"
            "The program analyzes your abilities, passions, and available opportunities to craft unique ideas that are tailored perfectly for you. "
            "Tomorrow's successful startup begins today — simply input your parameters and let our generator breathe life into your entrepreneurial future!\\n\\n"
            "Don't miss the chance to transform your knowledge and interests into a profitable business. "
            "Entrust yourself to our idea generator and discover your unique path to success!"
        )
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main Layout for the central widget
        main_layout = QVBoxLayout(self.central_widget)

        # Project title label with increased font size and centered alignment
        self.title_label = QLabel(self.title)
        title_font = QFont()
        title_font.setPointSize(30)  # Increase font size
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Project description label with decreased font size
        self.description_label = QLabel(self.description)
        description_font = QFont()
        description_font.setPointSize(14)  # Decrease font size
        self.description_label.setFont(description_font)
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.description_label)

        # Text "Ready to become a millionaire?" with increased font size
        millionaire_label = QLabel("Ready to become a millionaire?")
        millionaire_font = QFont()
        millionaire_font.setPointSize(20)  # Increase font size
        millionaire_label.setFont(millionaire_font)
        millionaire_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(millionaire_label)

        # Button "yes!" with increased font size and styling
        self.yes_button = QPushButton("yes!")
        yes_font = QFont()
        yes_font.setPointSize(18)  # Increase font size
        self.yes_button.setFont(yes_font)
        self.yes_button.setStyleSheet("background-color: #f0f0f0; border: 2px solid #888; border-radius: 10px; padding: 10px;")
        self.yes_button.clicked.connect(self.show_questions)
        main_layout.addWidget(self.yes_button)

        # Button "yes yes yes! i was waiting for this chance whole of my life" with increased font size and styling
        self.yes_yes_yes_button = QPushButton("yes yes yes!\ni was waiting for this chance whole of my life")
        yes_yes_yes_font = QFont()
        yes_yes_yes_font.setPointSize(18)  # Increase font size
        self.yes_yes_yes_button.setFont(yes_yes_yes_font)
        self.yes_yes_yes_button.setStyleSheet("background-color: #f0f0f0; border: 2px solid #888; border-radius: 10px; padding: 10px;")
        self.yes_yes_yes_button.clicked.connect(self.show_questions)
        main_layout.addWidget(self.yes_yes_yes_button)

        # Text Edit to display generated idea
        self.idea_display = QTextEdit()
        main_layout.addWidget(self.idea_display)

    def show_questions(self):
        # Switch to the questions page
        self.questions_page = QuestionsPage()
        self.setCentralWidget(self.questions_page)

class QuestionsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Title label
        title_label = QLabel("Answer the following questions:")
        title_font = QFont()
        title_font.setPointSize(20)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # Questions and input fields
        self.questions = [
            "What are your primary skills and competencies?",
            "In which industries or sectors do you have experience or education?",
            "What hobbies or interests do you have?",
            "What assets or resources are available to you? (e.g., equipment, space, starting capital, etc.)",
            "What business format do you prefer? (e.g., online, offline, franchise, startup, etc.)",
            "Are there specific markets or audiences you would like to target?",
            "What level of risk are you willing to take? (e.g., high, medium, low)",
            "What is your long-term plan or vision for the business?",
            "Are there any specific market problems or needs you would like to address?",
            "What would you like to achieve with your business over the next 5 years?"
        ]
        self.inputs = []
        
        for question in self.questions:
            label = QLabel(question)
            layout.addWidget(label)
            line_edit = QLineEdit()
            self.inputs.append(line_edit)
            layout.addWidget(line_edit)

  # Generate button
        self.generate_button = QPushButton("Generate", self)
        self.generate_button.clicked.connect(self.open_new_page)
        layout.addWidget(self.generate_button)

    
    def open_new_page(self):
        new_page_widget = QWidget()
        layout = QVBoxLayout(new_page_widget)
        result_label = QLabel("Having analyzed your data \nbased on the entered skills, interests, and assets, \nwe have compiled a list of the top 5 best business ideas. \nChoose the one you like:")
        result_font = QFont()
        result_font.setPointSize(20)
        result_label.setFont(result_font)
        result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(result_label)
        # Adding 5 buttons numbered from 1 to 5
        for i in range(1, 6):
            btn = QPushButton("Business Idea {}".format(i), new_page_widget)
            layout.addWidget(btn)

        self.window().setCentralWidget(new_page_widget)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = BusinessIdeaApp()
    ex.show()
    sys.exit(app.exec())







# from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, 
#                              QTextEdit, QWidget, QLineEdit, QScrollArea)
# from PyQt6.QtGui import QFont
# from PyQt6.QtCore import Qt
# import sys

# class BusinessIdeaApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.title = 'IdeaAlchemy: Craft Your Success'
#         self.description = (
#             "Innovative idea generator based on your skills, interests, and resources — your key to optimal business proposals! "
#             "Say goodbye to endless searches for the perfect business concept — now everything is easy and swift.\\n\\n"
#             "The program analyzes your abilities, passions, and available opportunities to craft unique ideas that are tailored perfectly for you. "
#             "Tomorrow's successful startup begins today — simply input your parameters and let our generator breathe life into your entrepreneurial future!\\n\\n"
#             "Don't miss the chance to transform your knowledge and interests into a profitable business. "
#             "Entrust yourself to our idea generator and discover your unique path to success!"
#         )
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle(self.title)
        
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)

#         # Main Layout for the central widget
#         main_layout = QVBoxLayout(self.central_widget)

#         # Project title label with increased font size and centered alignment
#         self.title_label = QLabel(self.title)
#         title_font = QFont()
#         title_font.setPointSize(30)  # Increase font size
#         self.title_label.setFont(title_font)
#         self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         main_layout.addWidget(self.title_label)

#         # Project description label with decreased font size
#         self.description_label = QLabel(self.description)
#         description_font = QFont()
#         description_font.setPointSize(14)  # Decrease font size
#         self.description_label.setFont(description_font)
#         self.description_label.setWordWrap(True)
#         self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         main_layout.addWidget(self.description_label)

#         # Text "Ready to become a millionaire?" with increased font size
#         millionaire_label = QLabel("Ready to become a millionaire?")
#         millionaire_font = QFont()
#         millionaire_font.setPointSize(20)  # Increase font size
#         millionaire_label.setFont(millionaire_font)
#         millionaire_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         main_layout.addWidget(millionaire_label)

#         # Button "yes!" with increased font size and styling
#         self.yes_button = QPushButton("yes!")
#         yes_font = QFont()
#         yes_font.setPointSize(18)  # Increase font size
#         self.yes_button.setFont(yes_font)
#         self.yes_button.setStyleSheet("background-color: #f0f0f0; border: 2px solid #888; border-radius: 10px; padding: 10px;")
#         self.yes_button.clicked.connect(self.show_questions)
#         main_layout.addWidget(self.yes_button)

#         # Button "yes yes yes! i was waiting for this chance whole of my life" with increased font size and styling
#         self.yes_yes_yes_button = QPushButton("yes yes yes!\ni was waiting for this chance whole of my life")
#         yes_yes_yes_font = QFont()
#         yes_yes_yes_font.setPointSize(18)  # Increase font size
#         self.yes_yes_yes_button.setFont(yes_yes_yes_font)
#         self.yes_yes_yes_button.setStyleSheet("background-color: #f0f0f0; border: 2px solid #888; border-radius: 10px; padding: 10px;")
#         self.yes_yes_yes_button.clicked.connect(self.show_questions)
#         main_layout.addWidget(self.yes_yes_yes_button)

#         # Text Edit to display generated idea
#         self.idea_display = QTextEdit()
#         main_layout.addWidget(self.idea_display)

#     def show_questions(self):
#         # Switch to the questions page
#         self.questions_page = QuestionsPage()
#         self.setCentralWidget(self.questions_page)

# class QuestionsPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout(self)
        
#         # Title label
#         title_label = QLabel("Answer the following questions:")
#         title_font = QFont()
#         title_font.setPointSize(20)
#         title_label.setFont(title_font)
#         layout.addWidget(title_label)
        
#         # Questions and input fields
#         self.questions = [
#             "What are your primary skills and competencies?",
#             "In which industries or sectors do you have experience or education?",
#             "What hobbies or interests do you have?",
#             "What assets or resources are available to you? (e.g., equipment, space, starting capital, etc.)",
#             "What business format do you prefer? (e.g., online, offline, franchise, startup, etc.)",
#             "Are there specific markets or audiences you would like to target?",
#             "What level of risk are you willing to take? (e.g., high, medium, low)",
#             "What is your long-term plan or vision for the business?",
#             "Are there any specific market problems or needs you would like to address?",
#             "What would you like to achieve with your business over the next 5 years?"
#         ]
#         self.inputs = []
        
#         for question in self.questions:
#             label = QLabel(question)
#             layout.addWidget(label)
#             line_edit = QLineEdit()
#             self.inputs.append(line_edit)
#             layout.addWidget(line_edit)

#   # Generate button
#         self.generate_button = QPushButton("Generate", self)
#         self.generate_button.clicked.connect(self.open_new_page)
#         layout.addWidget(self.generate_button)

#     def open_new_page(self):
#         new_page_widget = QWidget()
#         self.window().setCentralWidget(new_page_widget)

        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = BusinessIdeaApp()
#     ex.show()
#     sys.exit(app.exec())




# MakeResult

## Overview

**MakeResult App** is a sophisticated academic result transcript generation application developed using the KivyMD framework. Designed to streamline the process of creating detailed student transcripts, the app provides a user-friendly interface to input essential exam information, student details, and subject marks. It then generates comprehensive transcripts in both HTML and PDF formats, ensuring an efficient and organized approach to result reporting.

## Key Features

- **Multi-Screen Structure:** Utilizes Kivy's ScreenManager to offer a seamless navigation experience across different sections of the application.

- **Effortless Input:** Enables effortless input of institution details, exam name, class, section, and subject marks through an intuitive interface.

- **GPA Calculation:** Automatically calculates the Grade Point Average (GPA) for each student based on their subject marks.

- **Position Determination:** Accurately determines the position of each student in the class, considering both their total marks and GPA. This comprehensive ranking system provides a fair assessment of students' overall performance.

- **Transcript Generation:** Generates both HTML and PDF transcripts for students, providing flexibility in report distribution.

- **Scalable:** Supports up to 200 students and 14 subjects, making it suitable for a wide range of educational institutions.

## Screenshots

### Entering Exam Information and Student Details (Page 1):

This screenshot showcases the user interface where the user can enter exam information, student names, gained marks, and total marks for each subject. It also demonstrates the automatic GPA calculation based on the entered marks.

![entering_inputs](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/75e0b9c2-995e-4b54-80f8-97819e22c4d1)

### Result Editing Page Template (Pages 2-11):

These screenshots provide an overview of the template used for generating transcript pages. Each page displays the student's name, subject-wise marks, GPA, and any additional relevant information.

![pages](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/5dc0a016-4e27-4478-984f-e003d1041e9f)

### Result Summary and Analysis (Page 12):

This screenshot displays the summary and analysis page where the user enters the total number of students and selects whether to view results based on GPA or total marks. The page provides information on the number of passed, failed, and absent students, as well as pass, fail, and absent rates.

![Screenshot (33)](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/b7f619b1-e4c3-414f-8a9f-1b752e33b622)

### Result by GPA Position:

These screenshots illustrate the pages displaying the students' results organized by their GPA positions. This view allows users to easily identify the top-performing students based on their GPA scores.


![by_gpa_position](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/130878fe-a40b-4191-8f20-addaa64098a0)

![by_gpa_submit](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/118d6f4b-49a8-4e96-9eb9-a04aac65b402)

### Result by Total Marks Position:

Similarly, these screenshots show the pages presenting the results based on the students' positions determined by total marks. This view offers insights into students' performance based on their achieved marks.

![by_marks_position](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/eb33bc38-eaa8-4435-a0f5-87bcaca82f42)

![by_marks_submit](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/63d50154-dcd2-4107-809e-1e2f24a9dbf2)

### Class Result Sheet PDF:

[Result Sheet 1.pdf](https://github.com/IsratTasnimEsha/MakeResult/files/12388375/Result.Sheet.1.pdf)

![Screenshot (36)](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/5180b3cb-f3b0-43cb-870c-550df39a6426)

### Individual Student Result Sheet PDF:

[Roll 4.pdf](https://github.com/IsratTasnimEsha/MakeResult/files/12388380/Roll.4.pdf)

![Screenshot (35)](https://github.com/IsratTasnimEsha/MakeResult/assets/88322977/df327b2d-dfb4-44d0-8f37-915d2ab55e6d)

## Installation

### Prerequisites

- Python 3.x
- Git

### Clone the Repository

To get started, clone the MakeResult App repository to your local machine:

git clone https://github.com/yourusername/MakeResult-App.git

cd MakeResult-App

### Install Dependencies
Navigate to the app's directory and install the required dependencies using pip: pip install -r requirements.txt

## Usage

### Run the App:

Launch the MakeResult App using the following command: python main.py


## Contributing
If you would like to contribute to the MakeResult App, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Ensure your code adheres to the existing coding style and conventions.
- Submit a pull request with a clear description of your changes.

## Author

Israt Tasnim Esha

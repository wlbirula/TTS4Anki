#! /usr/bin/env python3

'''
Program that creates MP3 files for ANKI flashcards
using Google Text-To-Speech engine.
Author: Wojtek L. Birula
'''

import os
import datetime
from appJar import gui
from gtts import gTTS

version = "0.5"
now = datetime.datetime.now()
timestamp = (now.strftime("%Y%m%d-%H%M%S"))


def mainproc(question_language, answer_language, input_filename, prefix):
    sourcefilename = input_filename
    targetfilename = 'anki_import_file_' + timestamp + ".txt"

    with open(targetfilename, 'w', encoding="utf-8") as targetf:
        with open(sourcefilename, 'r', encoding="utf-8") as sourcef:
            lines = sourcef.readlines()
            row_number = 0
            for input_csv_row in lines:
                row_number = row_number + 1
                chomped_row = input_csv_row.rstrip()
                q_and_a = chomped_row.split(';')

                tts_question = gTTS(
                    text=q_and_a[0],
                    lang=question_language,
                    slow=False)
                question_mp3_file = str(
                    prefix + '{:04d}'.format(row_number)) + "_" + question_language + ".mp3"
                print(q_and_a[0])
                tts_question.save(question_mp3_file)

                tts_answer = gTTS(
                    text=q_and_a[1],
                    lang=answer_language,
                    slow=False)
                answer_mp3_file = str(
                    prefix + '{:04d}'.format(row_number)) + "_" + answer_language + ".mp3"
                print(q_and_a[1])
                tts_answer.save(answer_mp3_file)

                targetf.write(
                    q_and_a[0] +
                    '[sound:' +
                    question_mp3_file +
                    '];' +
                    q_and_a[1] +
                    '[sound:' +
                    answer_mp3_file +
                    ']\n')
    return(row_number)


def press(button):
    if button == "Process":
        input_filename = os.path.normpath(app.getEntry("Input_File"))
        question_language = app.getEntry("question_lang")
        answer_language = app.getEntry("answer_lang")
        prefix = app.getEntry("prefix")
        if len(prefix) == 0:
            prefix = timestamp + "_"
        else:
            prefix = prefix + "_"
        pairs = mainproc(
            question_language,
            answer_language,
            input_filename,
            prefix)
        info = str(2 * pairs) + \
            " sound files are ready to import. Happy learning!"
        app.infoBox("Success!", info, parent=None)
        app.stop()
    else:
        app.stop()


app = gui("Text-To-Speech for ANKI v. " + version, useTtk=True)
app.setTtkTheme("default")
app.setSize(450, 200)
app.addLabel("Question language (2 letter code):")
app.addEntry("question_lang")
app.addLabel("Answer language (2 letter code):")
app.addEntry("answer_lang")
app.addLabel("Prefix for all MP3 filenames (optional):")
app.addEntry("prefix")
app.addLabel("Input CSV file:")
app.addFileEntry("Input_File")
app.addButtons(["Process", "Quit"], press)
app.go()

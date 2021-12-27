# TTS4Anki - Text-To-Speech for Anki flashcards

This is a tiny Python script that creates sound files for Anki flashcards using Google Text-To-Speech engine. The pronunciation in the files is not perfect, but it makes your learning easier.

# How to use
0. Create a text file with questions and answers. 
Each line should contain a question and an answer separated by a semicolon. 
It may simply contain the same word or phrase in your native and the foreign language.
```
book;das Buch
house;das Haus
```
2. Unzip and run the program.
    + Enter the two-letter language codes for the question and for answers (e.g. 'en' for English, 'de' for German, 'es' for Spanish).
    + You can also enter a prefix that will be attached to the name of each MP3 file you create. If this field is blank, the program will automatically append the date and time you started the program. The prefix might be useful to find the files you have created.
    + Select an input file.
    + Press the "Process" button.
3. If everything is OK, select and copy the created MP3 files.
    + open the Run command (Windows key + R), type **%APPDATA%**, and press Enter. 
    + find the subfolder **Anki2** and then - in the folder with the name of your Anki profile (probably ***User 1***) - **collection.media**. Paste the MP3 files there.
4. Open Anki and import the generated text file (its name is **Anki_import_file_DATE-TIME.txt**)

Happy learning!

# Todo
- [ ] Error handling

# Technologies:
The script uses two Python modules:

+ gTTS - https://pypi.org/project/gTTS/

+ appJar - http://appjar.info/

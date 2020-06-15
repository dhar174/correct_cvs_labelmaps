# correct_cvs_labelmaps
This is a personal script I've written to convert labelmap data for ML datasets into my own format for training Tensorflow models.

The script has several functions.
   1. Replace ';' delimiters with '''
   2. Translate fieldnames (values are the same, names are different. Changed to my preferred variable names)
   3. Collate CSV labelmap files into one labelmap file.

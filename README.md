# ODS-SQL
Python application to convert ODS spreadsheets into SQL script

I was learning some Python when I had the idea for this program. I've made that just to keep becoming more familiar with Python. 
It's not really usefull when you realize it can be found online by typing "ods to sql" into Google. However, if you want to run this on your Linux desktop, fallow these steps:

1 - Make shure you have Python 3 installed on your OS.

2 - Install pyexcel API: https://github.com/pyexcel/pyexcel

3 - Download this repository and paste it in /opt. It must be like this: /opt/ODS-SQL/Core/files...

4 - Ctrl + Alt + t to open terminal

5 - $ python3 /opt/ODS-SQL/Core/

Each sheet from the ods file must be a table, and the first line must contain the columns.
The data must begin in cell A1. 

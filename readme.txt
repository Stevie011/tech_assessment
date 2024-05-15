I used a very straightforward Django setup as per the documentation/many tutorials available online

I created a model with the required fields, created a forms.py file and used the builtin ModelForm to generate the new form.

I then added the form and the most recent UserDetails object to the page context and the html.

Used import_export to handle files.  Followed tutorial here https://www.youtube.com/watch?v=gcaAEHEg1C4, thanks.

Matplotlib for the files (https://www.youtube.com/watch?v=jrT6NiM46jk).



*Took me a second to realise the number in the file are randomly generated in a range. 

-Swapped matplotlib for plotly, simpler integration of interactive charts


TO DO:

add verification for uploaded file type
resources- some created but not used 
figure out plot path properly

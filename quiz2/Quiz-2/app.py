
from flask import Flask, request, render_template
import requests
import re
app = Flask(__name__)


@app.route('/question6', methods=['GET', 'POST'])
def question6():
    return render_template("question6.html")
@app.route('/question6_1', methods=['GET','POST'])
def question6_1():
    n=request.form['n']
    #words=n.split('.|?|"|!| ')
    total_words=n.split(" ")
    total_sentences=n.split(".")
    print(total_words)
    print(total_sentences)
    c=["a","i","e","o","u"]

    count_overall=0
    for a in total_words:
        count=0
        for b in c:
                if b in a:
                    count+=1
        count_overall=count_overall+count
    deduction=0
    for a in total_words:
        if a[len(a)-1] in 'e':
            deduction=deduction+1

    total_number_words=len(total_words)
    total_number_sentences=len(total_sentences)
    count_overall1=count_overall-deduction
    total_number_syllables=count_overall1
    print(count)
    print(count_overall1)
    Readability = 206.835 - (1.015 * total_number_words/total_number_sentences) - (84.6 * total_number_syllables/total_number_words)
    if Readability>90 and Readability<100:
        value="5 th grade"
    elif Readability>80 and Readability<90:
        value="6th grade"
    elif Readability>70 and Readability<80:
        value="7th grade"
    elif Readability>60 and Readability<70:
        value="8th  an 9th grade"
    elif Readability>50 and Readability<60:
        value="10th to 12th Grade"
    elif Readability>30 and Readability<50:
        value="College"
    elif Readability>10 and Readability<30:
        value="College graduate"
    elif Readability>0 and Readability<10:
        value="Professional"   
    return render_template("question6_1.html",re=Readability,value=value,ts=total_sentences)



if __name__ == '__main__':
    app.run()

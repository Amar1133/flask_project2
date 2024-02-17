from flask import Flask,render_template


FAI=Flask(__name__)
@FAI.route('/createproperty')
def createproperty():
    return render_template('createproperty.html',name='amar')

@FAI.route('/property')
def property():
    return render_template('property.html')



if __name__=='__main__':
    FAI.run(debug=True)
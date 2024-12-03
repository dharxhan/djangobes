from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    sNum = [1, 2, 3, 4, 5]
    eNames = ['Mohan', "Raju", "Krishna", "Krish", "Kruthika"]
    eSalary = [60000, 70000, 50000, 40000, 800000]
    eDisg = ['SE', 'SSE', 'SE', 'SE', 'SSE']
    eOrg = ['Intel', 'Dell', 'Siemens', 'Accenture', 'Bosch']

    mywebsite = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Login Page </title>
<style>
body {
  font-family: Calibri, Helvetica, sans-serif;
  background-color: pink;
}
button {
       background-color: #4CAF50;
       width: 100%;
        color: orange;
        padding: 15px;
        margin: 10px 0px;
        border: none;
        cursor: pointer;
         }
 form {
        border: 3px solid #f1f1f1;
    }
 input[type=text], input[type=password] {
        width: 100%;
        margin: 8px 0;
        padding: 12px 20px;
        display: inline-block;
        border: 2px solid green;
        box-sizing: border-box;
    }
 button:hover {
        opacity: 0.7;
    }
  .cancelbtn {
        width: auto;
        padding: 10px 18px;
        margin: 10px 5px;
    }

 .container {
        padding: 25px;
        background-color: lightblue;
    }
</style>
</head>
<body>

     <table border="1px" cellspacing="1px" cellpadding="5px" rules="all">
        <tr>
            <th>Snum</th>
            <th>eNames</th>
            <th>eSalary</th>
            <th>eDisg</th>
            <th>eOrg</th>
        </tr>
        <tbody>'''
    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[0]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[0])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[0])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[0])
    mywebsite = mywebsite + '''
            <td>%s</td></tr>''' % (eSalary[0])

    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[1]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[1])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[1])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[1])
    mywebsite = mywebsite + '''
            <td>%s</td></tr>''' % (eSalary[1])

    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[2]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[2])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[2])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[2])
    mywebsite = mywebsite + '''
            <td>%s</td></tr> <br>''' % (eSalary[2])

    
    for index in range(len(sNum)):
        mywebsite=mywebsite+'''<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>       
            '''%(str(sNum[index]), eNames[index], eDisg[index], eOrg[index], eSalary[index])

    mywebsite = mywebsite + '''</tbody>

    </tbody>
    </table>
</body>
</html>'''
    return HttpResponse(mywebsite)
def ctable(request):
    sNum = [1, 2, 3, 4, 5]
    eNames = ['Mohan', "Raju", "Krishna", "Krish", "Kruthika"]
    eSalary = [60000, 70000, 50000, 40000, 800000]
    eDisg = ['SE', 'SSE', 'SE', 'SE', 'SSE']
    eOrg = ['Intel', 'Dell', 'Siemens', 'Accenture', 'Bosch']

    mywebsite = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Login Page </title>
<style>
body {
  font-family: Calibri, Helvetica, sans-serif;
  background-color: pink;
}
button {
       background-color: #4CAF50;
       width: 100%;
        color: orange;
        padding: 15px;
        margin: 10px 0px;
        border: none;
        cursor: pointer;
         }
 form {
        border: 3px solid #f1f1f1;
    }
 input[type=text], input[type=password] {
        width: 100%;
        margin: 8px 0;
        padding: 12px 20px;
        display: inline-block;
        border: 2px solid green;
        box-sizing: border-box;
    }
 button:hover {
        opacity: 0.7;
    }
  .cancelbtn {
        width: auto;
        padding: 10px 18px;
        margin: 10px 5px;
    }

 .container {
        padding: 25px;
        background-color: lightblue;
    }
</style>
</head>
<body>

     <table border="1px" cellspacing="1px" cellpadding="5px" rules="all">
        <tr>
            <th>Snum</th>
            <th>eNames</th>
            <th>eSalary</th>
            <th>eDisg</th>
            <th>eOrg</th>
        </tr>
        <tbody>'''
    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[0]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[0])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[0])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[0])
    mywebsite = mywebsite + '''
            <td>%s</td></tr>''' % (eSalary[0])

    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[1]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[1])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[1])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[1])
    mywebsite = mywebsite + '''
            <td>%s</td></tr>''' % (eSalary[1])

    mywebsite = mywebsite + '''<tr>
            <td>%s</td>''' % (str(sNum[2]))
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eNames[2])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eDisg[2])
    mywebsite = mywebsite + '''
            <td>%s</td>''' % (eOrg[2])
    mywebsite = mywebsite + '''
            <td>%s</td></tr> <br>''' % (eSalary[2])

    
    for index in range(len(sNum)):
        mywebsite=mywebsite+"<tr>"
        mywebsite=mywebsite+'<td>'+str(sNum[index])+'</td>'
        mywebsite=mywebsite+'<td>'+(eNames[index])+'</td>'
        mywebsite=mywebsite+'<td>'+(eDisg[index])+'</td>'
        mywebsite=mywebsite+'<td>'+(eOrg[index])+'</td>'
        mywebsite=mywebsite+'<td>'+str(eSalary[index])+'</td></tr>'

    mywebsite = mywebsite + '''</tbody>

    </tbody>
    </table>
</body>
</html>'''
    return HttpResponse(mywebsite)


def table2(request):
    sNum = [1, 2, 3, 4, 5]
    eNames = ['Mohan', "Raju", "Krishna", "Krish", "Kruthika"]
    eSalary = [60000, 70000, 50000, 40000, 800000]
    eDisg = ['SE', 'SSE', 'SE', 'SE', 'SSE']
    eOrg = ['Intel', 'Dell', 'Siemens', 'Accenture', 'Bosch']

    mywebsite = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Login Page </title>
<style>
body {
  font-family: Calibri, Helvetica, sans-serif;
  background-color: pink;
}
button {
       background-color: #4CAF50;
       width: 100%;
        color: orange;
        padding: 15px;
        margin: 10px 0px;
        border: none;
        cursor: pointer;
         }
 form {
        border: 3px solid #f1f1f1;
    }
 input[type=text], input[type=password] {
        width: 100%;
        margin: 8px 0;
        padding: 12px 20px;
        display: inline-block;
        border: 2px solid green;
        box-sizing: border-box;
    }
 button:hover {
        opacity: 0.7;
    }
  .cancelbtn {
        width: auto;
        padding: 10px 18px;
        margin: 10px 5px;
    }

 .container {
        padding: 25px;
        background-color: lightblue;
    }
</style>
</head>
<body>

     <table border="1px" cellspacing="1px" cellpadding="5px" rules="all">
        <tr>
            <th>Snum</th>
            <th>eNames</th>
            <th>eSalary</th>
            <th>eDisg</th>
            <th>eOrg</th>
        </tr>
        <tbody>'''
    for sno, name, desig,  org, sal in zip(sNum, eNames, eDisg, eOrg, eSalary):
        mywebsite=mywebsite+"<tr>"
        mywebsite=mywebsite+'<td>'+str(sno)+'</td>'
        mywebsite=mywebsite+'<td>'+name+'</td>'
        mywebsite=mywebsite+'<td>'+desig+'</td>'
        mywebsite=mywebsite+'<td>'+org+'</td>'
        mywebsite=mywebsite+'<td>'+str(sal)+'</td>'


    mywebsite = mywebsite + '''</tbody>

    </tbody>
    </table>
</body>
</html>'''
    return HttpResponse(mywebsite)

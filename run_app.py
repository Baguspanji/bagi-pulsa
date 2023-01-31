from aplikasi import create_app

app = create_app()
application = app

if __name__ == '__main__':
    
    app.run(host='103.163.138.24', debug=True)

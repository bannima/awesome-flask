###Introduction
This project is a demo practice for Flask Web Development. https://book.douban.com/subject/26274202/

###deploy
##requirements:
All dependency python packages are listed in requirements/dev.txt and you should use the following command for requried python packages.

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement/dev.txt

##development
The manage.py has packaged the development by using this command:

python3 manage.py reset 

##runserver
For starting the website, we should first prepare the SQL dataset and then run the flask server.

python3 manage.py deploy
nohup python3 manage.py runserver --host 0.0.0.0 --port 80 >> report.log 2>&1 &



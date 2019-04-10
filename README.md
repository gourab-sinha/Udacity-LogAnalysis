# Log Analysis
This project is a part of the Udacity Full Stack Web Development Nano Degree Program.
# Project Summary
In this project one should create and use SQL queries which will fetch the information from the database "news" which is part of a website. The purpose of this project is to apply and test command over sql queries and make sure he/she fetch the correct information from the database. The code uses queries to fetch the information and uses two views to answer third query.

# Software Requirements
1. Python - 3.7.3
2. Vagrant - 2.2.4
3. Virtualbox - 6.0.4
4. Git - 2.21.0.windows.1

# How to run the project
 1. Download(Optional):
 1.1 [Git](https://git-scm.com/download/win)
 1.2 [Python3](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe)
 1.3 [VirtualBox](https://download.virtualbox.org/virtualbox/6.0.4/VirtualBox-6.0.4-128413-Win.exe)
 1.4 [Vagrant](https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.msi)
 1.5 Configured [Vagrantfile](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip)*
 1.6 [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)*
 2. Installation(If not installed):
    2.1 Git
    2.2 Python3
    2.3 VirtualBox
    2.4 Vagrant
 3. Open command prompt or gitbash terminal
 4. Create new directory or you can use existing one. For creating directory use mkdir 'DirectoryName' on gitbash terminal/cmd.
 5. Goto the directory where you want to keep your files and paste downloaded files in steps Vagrantfile and newsdata.sql inside the folder.
 6. Open VirtualBox
 7. 'vagrant up' on gitbash/cmd. 
 8. 'vagrant ssh' on gitbash/cmd once step 7th successfully completed.
 9. Run 'cd /vagrant' on gitbash/cmd to goto shared directory between host and guest machine.
 10. Run 'psql -d news -f newsdata.sql' to load data into database. 
 11. To connect to news database run 'psql -d news'.
 12. Type 'python3 log-analysis.py' to run the python code.
 
 # Create Views
 1. Create view requestlog as select date(time) as time,count(*) requests from log group by date(time);
 2. Create view failedlog as select date(time) as time,count(*) requestfailed from log where status like '%404%' group by date(time);
 
 # Troubleshooting
 If you are unable to access shared folder then close connections and run 'vagrant reload'.
 
 # Note
 \* are required files. 

To set up the project on your system, you can follow the steps mentioned below:
- Fork the repository to your GitHub account.
- Clone your fork to your system and ```cd``` into the ```online_leave_management_iitp``` folder.
```
$ git clone https://github.com/<your-username>/online_leave_management_iitp.git
$ cd online_leave_management_iitp
```
After following the above steps, you should be inside the folder where ```manage.py``` is present.
- Set up the remote to the main repository.
```
$ git remote add upstream https://github.com/arundhati24/online_leave_management_iitp.git
```
**Note:** If your are looking forward to contribute to this project as part of [NJACK Winter Of Code](https://github.com/NJACKWinterOfCode), then set up the ```upstream``` remote as follows:
```
$ git remote add upstream https://github.com/NJACKWinterOfCode/online_leave_management_iitp.git
```
- Assuming, you already have ```Python3``` and ```pip3`` installed on your system, we will now set up the virtual environment. To set up the virtual environment, follow the steps below:
    - Install virtual environment using pip3.
    ```
    $ pip3 install virtualenv
    ```
    - Make sure you are in the directory where ```manage.py``` is present. Create a virtual environment for your project.
    ```
    $ virtualenv venv
    ```
    - Now, activate the virtual environment.
    ```
    $ source venv/bin/activate
    ```
    - Finally, use the following command to install the requirements for the project (specified in the requirements.txt file):
    ```
    $ pip3 install -r requirements.txt
    ```
    To list all the installed pip packages use the command below:
    ```
    $ pip3 list
    ```
    - Now, you can run the project using the following command:
    ```
    $ python manage.py runserver
    ```
Congratulations! You have successfully set up the project on your system. 😃 
      

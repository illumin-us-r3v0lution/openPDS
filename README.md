Human Dynamics openPDS
======================================

    >apt-get install python-pip
    
    >apt-get install python-virtualenv
    
    >apt-get install mongodb mongodb-server
    
    >apt-get install git
    
    >service mongodb start

    >virtualenv pdsvirtenv
    
    >cd pdsvirtenv
    
    >git clone git@github.com:HumanDynamics/openPDS.git
    
    >source bin/activate

    >cd openPDS/conf
    
    >pip install -r requirements.txt

    >cd ../
    
    >python manage.py runserver 0.0.0.0:8002 (for access to local VM)

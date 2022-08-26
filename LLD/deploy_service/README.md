Have designed a high level  solution where lets say we fire an API to call /api/deploy 
by passing a Request Object.

The API gets hit and subsequent components are involved, which saves the model to a Destination Path in NFS Mount.



Testing Steps:-

1) Create a Virtual environment using python3 -m venv test-env
2) Actiavte using source/test-env/activate
3) pip install flask
4) Run the application with python3 deploy.py
5) Once application is started, hit the API using CURL by executing test_deploy_api.sh



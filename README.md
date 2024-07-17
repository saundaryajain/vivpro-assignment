Installation Prerequisites
Python 3.8 or above
virtualenv package (install via pip install virtualenv)

git clone https://github.com/saundaryajain/vivpro-assignment.git
cd vivpro-assignment

1. Create a virtual environment

2. virtualenv venv

3. Activate the venv
    source venv/bin/activate

4. pip install -r requirements.txt

5. To run the application: python app.py

    1. API to save records in table format

        curl --location --request GET 'http://127.0.0.1:5000/save-records' \
        --form 'playlist_file=@"playlist_vivpro.json"'

    2. API to fetch all records

        curl --location --request GET 'http://127.0.0.1:5000/fetch-records?page=1&per_page=5'

    3. API to fetch data using title

        curl --location 'http://127.0.0.1:5000/fetch-by-title/<title>'

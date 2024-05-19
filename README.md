# Illuquest
This is an request forum application that allows users to log in, send requests for illustrations, view all requests, reply to requests with illustrations, search users, view other users' profile pages and toggle their availability status to receive requests.
<br>

## Group members
| UWA ID   | Name                 | Github Username |
|----------|----------------------|-----------------|
| 23118632 | Selina Tan           | st252   |
| 23621217 | Kiki Zhang           | kik-ki  |
| 23170244 | Daniel Odijk         | Viper-cell |
| 23201336 | Chunchig Buyanjargal | N/A |

<br>

## How to launch the application

1. **Clone the repository:**

    ```bash
    git clone https://github.com/st252/webdev-proj.git
    cd webdev-proj
    ```

2. **Initialize a Python virtual environment and activate it:**

    ```bash
    python3 -m venv tmp-env
    source tmp-env/bin/activate
    ```

3. **Install the required packages and libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set the secret key:**
    ```bash
    export GROUP_PROJECT_SECRET_KEY='your-secret-key!'
    ```

5. **Implement database (Optional):**
    ```bash
    flask db upgrade 24be6862d252
    ```
   
7. **Open a new terminal and populate database with test data (Optional):**
    ```bash
    flask shell
    import app.test_data
    ```

8.  **Run the application:**
    ```bash
    flask run
    ```

Open up a web browser and navigate to `http://localhost:5000`.

*Note: Images such as cow.png and penguin.png are free for users to use in the 'img' folder.


<br>

## How to run tests for the application

1. **Clone the repository:**

    ```bash
    git clone https://github.com/st252/webdev-proj.git
    cd webdev-proj
    ```

2. **Run the unit tests:**

   ```bash
    python -m unittest tests.unit
    ```

3. **Run the selenium tests:**

    ```bash
    python -m unittest tests.selenium  
    ```

# webdev-proj
<br>

## About /Website Name/
This is an request forum application that allows users to log in, send illustration requests, view all public requests, reply to requests with illustration, view users' and individual profile pages.
<br>

## Group members
| UWA ID   | Name                 | Github Username |
|----------|----------------------|-----------------|
| 23118632 | Selina Tan           | st252   |
| 23621217 | Kiki Zhang           | kik-ki  |
| 23170244 | Daniel Odijk         |   |
| 23201336 | Chunchig Buyanjargal |   |

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

3. **Install the required packages and libraries**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set the secret key:**
    ```bash
    export GROUP_PROJECT_SECRET_KEY='your-secret-key!'
    ```

5.  **Run the application:**

    ```bash
    flask run
    ```

    Open up a web browser and navigate to `http://localhost:5000`.

<br>

## How to run tests for the application

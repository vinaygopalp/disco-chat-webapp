# Disco Chat WebApp

## Overview

Disco Chat is a real-time web application built using Django and Channels, which supports encrypted messaging using AES encryption. Users can join chat rooms and send messages securely.

## Features

- Real-time chat functionality
- AES encrypted messaging
- User authentication
- Responsive design

## Technologies Used

- Django
- Channels
- JavaScript (CryptoJS)
- HTML/CSS
- SQLite (default) or any other preferred database

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 4.2+


### Installation Steps
1. **Clone the Repository**

    
    git clone https://github.com/vinaygopalp/disco-chat-webapp.git
    cd disco-chat-webapp
   

2. **Create a Virtual Environment**

     bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
     

3. **Install Dependencies**

     bash
    pip install -r requirements.txt
     

4. **Set Environment Variables**

    Ensure the key is a valid 32-byte base64-encoded string.

5. **Run Migrations**

     bash
    python manage.py migrate
     

6. **Create a Superuser**

     bash
    python manage.py createsuperuser
     

7. **Run the Development Server**

     bash
    python manage.py runserver
     

8. **Access the Application**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### Create a Chat Room

1. Log in with your superuser account.
2. Create a chat room from the dashboard.

### Sending and Receiving Messages

1. Join a chat room.
2. Send messages through the input field. Messages will be encrypted before being sent.
3. View messages in the chat log, which will be decrypted upon receipt.

## Code Overview

### `views.py`

Handles the main logic for chat rooms, including:

- Loading the encryption key from environment variables
- Encrypting and decrypting messages using AES encryption
- Fetching and displaying messages

### `users.html`

Handles the frontend for displaying chat messages and sending new messages. Includes JavaScript for encrypting and decrypting messages using CryptoJS.

### WebSocket Setup

Uses Django Channels for real-time communication between clients and the server.

## Contributing

1. Fork the repository.
2. Create a new branch with your feature or bugfix.
3. Commit and push your changes.
4. Create a pull request to the main branch.



## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Channels Documentation](https://channels.readthedocs.io/)
- [CryptoJS Documentation](https://cryptojs.gitbook.io/docs/)

---

Feel free to adjust this as necessary to fit the specifics and any additional details of your project.
# College Event Management System

A Flask-based web application that helps manage college events and student registrations.

## Features

- View college events
- Add new events
- Store event descriptions, dates, venues, and organizers
- Register students for events
- View registered students for each event
- Delete events
- Store event and registration data using SQLite
- Data remains available after restarting the application

## Technologies Used

- Python
- Flask
- HTML
- CSS
- SQLite
- Git
- GitHub

## Project Structure

```text
college-event-management
│
├── app.py
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── events.html
│   ├── add_event.html
│   └── registrations.html
├── static/
│   └── style.css
└── screenshots/
    ├── home.png
    ├── events.png
    ├── registration.png
    └── registrations.png

events.db is a local database file and is excluded from Git tracking.

## How to Run
Clone the repository.
Open the project folder in VS Code.
Install Flask:
pip install flask
Run the application:
python app.py
Open the local address shown in the terminal, usually:
http://127.0.0.1:5000
Application Features
Home Page

Provides an introduction to the system and access to the events section.

Event Management

Users can view existing events and add new college events with details such as:

Event name
Description
Date
Venue
Organizer
Student Registration

Students can register for an event by providing:

Name
Email
Branch
Registration Management

The system displays all students registered for a particular event.

Event Deletion

Events can be removed from the system when required.

Data Persistence

Event and registration information is stored in a local SQLite database.

The data remains available after closing and restarting the application.

## Screenshots
Home Page

Events

Registration

Registrations

## Future Improvements
Student login and authentication
Admin dashboard
Event editing
Event search and filtering
Email notifications
Event capacity limits
```

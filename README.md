# bc_python_flask_form
BeCode Python - Flask Form Module

## Project

### Length

- 1 day to learn about flask
- 4 days to develop the project

### Skills

- Backend: Python Programming (initiation to logical structures)
- Validation and Sanitazation of a form
- Implementing POST and GET requests
- Implementing templates with Jinja

### Situation

The company "Hackers Poulette" is selling DIY kits and accessories for Raspberry Pi's, they want to implement a form for technical support.

Your mission is to develop a python script, showing a contact form and handling its use (sanitazation, validation, submit and feedback)

## Rules

### Performance criteria

- If there is an error in the user input, return the form with valid fields still filled.
- Show the field errors near the field in question.
- The form should sanitize and have server side validation.
- If the sanitazation and validation are ok, a "Thank you for your message" page should show with a run-down of all the information the user input.
- Implement antispam and honeypots
- **Required fields**:
    - Full name
    - Email
    - Country (list)
    - Message
    - Gender (radio box)
    - Subject (Repair, Order, Other)
- All fields are required except "Subject", which will default to "Other" value if not entered


### Goals

- Presentation: architechture client/server
- Sanitazation: neutralize all malicious code (script tags)
- Validation: required fields + valid email
- Confirmation: feedback when message sent
- NO JS OR CSS


### End goals

At the end of the project, the following skills should be acquired:

- Explain the difference betwenn a POST and GET request
- Avoid XSS attacks
- Avoid SSTI attacks
- Use a micro framework
- Deploy an app


## Running the project

```flask run```

Navigate to the url the terminal gives you (localhost:5000), you can see an example message already displayed.

Navigate to "Create" and create a message

## Ressources

[Install Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)

[The tutorial I used](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application)

[Flask](https://flask.palletsprojects.com/en/2.3.x/)

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
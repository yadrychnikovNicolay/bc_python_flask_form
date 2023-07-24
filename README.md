# bc_python_flask_form
BeCode Python - Flask Form Module

## Rules

### Performance criteria

- If there is an error in the user input, return the form with valid fields still filled.
- Show the field errors near the field in question.
- The form should sanitize and have server side validation.
- If the sanitazation and validation are ok, a "Thank you for your message" page should show with a run-down of all the information the user input.
- Implement antispam and honeypots
- Required fields:
    - Full name
    - Email
    - Country (list)
    - Message
    - Gender (radio box)
    - Subject (Repair, Order, Other)
- All fields are requiered except "Subject", which will default to "Other" value if not entered


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
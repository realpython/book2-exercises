Feature: flaskr provides user login and logout

  Scenario: successful login
    Given flaskr is setup
      When we login with "admin" and "admin"
      Then we should see the alert "You were logged in"

  Scenario: incorrect username
     Given flaskr is setup
      When we login with "notright" and "admin"
      Then we should see the alert "Invalid username"

  Scenario: incorrect password
     Given flaskr is setup
      When we login with "admin" and "notright"
      Then we should see the alert "Invalid password"

  Scenario: successful logout
     Given flaskr is setup
     and we login with "admin" and "admin"
      When we logout
      Then we should see the alert "You were logged out"
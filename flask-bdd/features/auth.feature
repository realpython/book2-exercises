Feature: flaskr is secure in that users must login and logout to access certain features

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

  Scenario: successful post
    Given flaskr is setup
    and we login with "admin" and "admin"
      When we add a new entry with "test" and "test" as the title and text
      Then we should see the alert "New entry was successfully posted"
      Then we should see the post with "test" and "test" as the title and text

  Scenario: unsuccessful post
    Given flaskr is setup
    Given we are not logged in
      When we add a new entry with "test" and "test" as the title and text
      Then we should see the alert "Unauthorized"
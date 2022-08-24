
Feature: Login form
    Scenario: Access the login form
        Given an anonymous user
        When I visit login page
        Then I should see Django administration
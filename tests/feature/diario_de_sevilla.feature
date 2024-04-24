Feature: Diario De Sevilla
  As a user, I want to verify that the news site is working correctly.

Scenario: Go Local News Page
  Given I have created an instance of DiarioDeSevilla with a browser driver
  When I call go_local_news_page("Sevilla")
  Then I should be taken to the local news page
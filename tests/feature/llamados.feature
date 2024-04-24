Feature: Llamados 
    As a user, I want to use Llamados to summarize and clean texts

Scenario: Summarize text
    Given I have a text
    When I send the text to Llamados for summarization
    Then the response should be a summary of the original text
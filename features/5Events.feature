Feature: Events

Scenario: Set time
  Given website "http://time.omnivox.eu/"
  When login ass owner
  When click on "Events" tab
  When set events, start "07:00", end "17:00"
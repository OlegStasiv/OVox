Feature: Pop-up

Scenario: Verify Add worker, customer, manager popups
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Managers" in Menu
  When click on AddManager button
  Then modal window appears
  When close popup
  Then modal window disappears
  When click on "Customers" in Menu
  When click on AddManager button
  Then modal window appears
  When close popup
  Then modal window disappears
  When click on "Workers" in Menu
  When click on AddManager button
  Then modal window appears
  When close popup
  Then modal window disappears
  
Scenario: Show protocol pop-up
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Workers" in Menu
  When click on any worker
  When click on Show Protocol button
  Then modal window appears
  When close popup
  Then modal window disappears

Scenario: Get Report pop-up
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Workers" in Menu
  When click on "Reports" tab
  When click on any worker
  When click on Get Report button
  Then modal window appears
  When close popup
  Then modal window disappears
  When click on any worker by means of multiaction
  Then modal window appears
  When close popup
  Then modal window disappears

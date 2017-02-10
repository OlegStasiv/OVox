Feature: Managers

Scenario: Create managers
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  When delete all managers except owner
  When create "20" manager

Scenario: Verify pagination
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  Then pagination is present
  When click on pagination "50"
  Then managers list will be contain "21" users
  When click on pagination "10"
  Then managers list will be contain "10" users

Scenario: Edit managers
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  When click on any manager
  When change F-Name "Edit fname", L-Name "Edit lname", Phone "00000000000", Email "edit@test.com"
  When click on Save button
  Then user profile was changed successfully

Scenario: Delete managers
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  When delete all managers except owner

Scenario: Sorting

  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  When delete all managers except owner
  When create few managers
    | first | last | phone | email |
    | Arnold     | Bobo        | 3333333333 | atest@test.com  |
    | Ronald     | Dithem      | 222222222  | hermst@test.com |
    | Wallen     | Xzibit      | 111111111  | tetiit@test.com |

  Then verify that sort works correctly for "Name" column
  Then verify that sort works correctly for "Phone" column
  Then verify that sort works correctly for "E-mail" column
  Then verify that sort works correctly for "Assigned" column

Scenario: Search

  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on Manager in Menu
  When delete all managers except owner
  When create few managers
    | first | last | phone | email |
    | Arnold     | Bobo        | 3333333333 | atest@test.com  |
    | Ronald     | Dithem      | 222222222  | hermst@test.com |
    | Wallen     | Xzibit      | 111111111  | tetiit@test.com |
  When try search "Ronald"
  Then list contain only "Ronald Dithem" and not contain "Arnold Bobo"

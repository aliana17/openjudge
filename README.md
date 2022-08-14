# openjudge
An offline platform to host contest

- [ ] A login page to user
- [ ] If a user is an admin
  - [ ] it should be display a page where he can add and remove questions
  - [ ] it should also provide option to add test cases for a question.
  - [ ] Should display the leaderboard representing which user is on top
  - [ ] should also visualize the user with its submission time
- [ ] if user is a participant
  - [ ] a page is displayed which will ask user for email address and name. 
  - [ ] After user has entered email address an htmx request is made to server API which will ask user to validate email id. If email id has already given the contest, 
        a red message is displayed to user that he has already given the contest. 
  - [ ] After email address verification a workspace api is called and a set of questions along with code editor is visible to user
  - [ ] On compile only output is visible to user
  - [ ] on submit button the code is checked against set of test cases. Use pytest 
  - [ ] Return the count of test cases passed. 

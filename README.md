# Point Guard: A Novel Password Manager

**Author #1 Dominic Flowers** (C22186640)  
**Author #2 Christopher Hunter** (C10195042)  
**Author #3 Isaiah Velez** (C80323220)

## Abstract

Concisely summarize the main points of the project report.

**Keywords:** password management, cybersecurity, user security

## Motivation

Have you ever wondered why millions of people still use '123456' as their password despite knowing the risks? According to NordPass, '123456' is used by over four and a half million people, making it the most common password of 2023. This trend extends to variations like '12345678' and '123456789,' highlighting the struggle users face in creating and managing secure passwords (Jacob, "Most Overused Passwords in the World — Make Sure Yours Isn't on the List.").

Passwords are notoriously difficult to remember, leading users to either reuse them across multiple accounts or opt for simplistic variations that are easily guessable. However, this convenience comes at a significant cost, with data breaches averaging a staggering $4.45 million in damages (IBM Data Breach Report).

Enter PointGuard, a revolutionary password manager designed to bridge the gap between security and convenience. Our military-oriented approach, focused on zero-trust architecture, ensures that users can generate and store strong, unique passwords without the hassle of remembering them. By safeguarding over four and a half million users from easily guessable passwords, PointGuard not only enhances security but also saves businesses millions of dollars in potential breach damages.

## Related Work

The field of password security is constantly evolving in response to advances in password cracking techniques. And riddled throughout the science of passwords are misconception. One common belief has been that complex passwords, with unique characters and symbols, are more secure. However, recent cybersecurity studies have challenged this idea, suggesting that longer passwords may be just as secure, if not more so ("Password Complexity Rules," Ars Technica, 2013).

PointGuard sets itself apart from traditional password managers by not only securely storing passwords but also focusing on educating and engaging users. Our web application actively sends informative articles on password security to our elite clientele and uses gamification techniques to demonstrate the vulnerability of common passwords.

### Password Cracking Techniques

To understand how PointGuard enhances security, it's important to grasp the techniques hackers use to crack passwords. One such method is brute force attacks, where hackers try every possible combination of characters to guess a password. This can be an exhaustive process, especially for longer and more complex passwords.

Another technique is hash cracking, where hackers obtain a database of hashed passwords (encrypted versions of passwords) and attempt to decrypt them to reveal the original passwords. While this approach can be effective, it requires significant computational resources and time.

Dictionary attacks involve using precompiled lists of commonly used passwords to try to gain access to accounts. These lists include variations of simple passwords like "password123" or common words like "qwerty."

Password spraying is another tactic where hackers try a few common passwords against many accounts, hoping that at least some of them will work. This method can be more efficient than brute force attacks, especially when targeting multiple accounts simultaneously.

Hackers also take advantage of password reuse, where users use the same password across different accounts. They leverage previously leaked passwords from data breaches and try them on other platforms, exploiting the tendency of users to reuse passwords.

### Other Password Managers

While PointGuard faces competition from other password managers like LastPass and 1Password, it distinguishes itself through its comprehensive features and user-centric approach. For example, unlike some competitors that offer advanced features only with paid subscriptions, PointGuard provides a complete solution without such restrictions. Additionally, while other managers may focus on interface design and customer support, PointGuard prioritizes user education and engagement to enhance overall cybersecurity awareness.

## Interface Requirements

In secure design, there's often a balance between making a system secure and ensuring it's user-friendly. This balance is known as the Perennial Security Conflict, and many IT professionals advocate for usable security to overcome this challenge. Our design philosophy acknowledges this conflict by personifying each side and prioritizing zero trust in all our designs. Zero trust doesn't mean no trust at all; instead, it means minimizing trust as much as possible.

### Primary Actors

#### User

Users are at the forefront of interacting with PointGuard, and they can be categorized into different roles based on their needs and actions within the system.

1. **Trusted User:** I want the most privileges so that I can quickly access my content. This user type has gone through the application's multi-factor authentication process and is granted the highest level of privileges to efficiently access and manage their data.
2. **The Adversary:** I want the app to be poorly designed so that I can exploit vulnerabilities for a profit. While not an actual user of the system, the adversary represents potential security threats. Emphasizing the adversary's perspective helps ensure that security vulnerabilities are addressed during the design phase.
3. **Consumer:** I want to store my passwords and retrieve them so that I can keep my passwords safe without incurring too much cognitive load. This user type desires the convenience of securely storing and accessing passwords without overwhelming cognitive demands. They represent the balance between security and usability.
4. **Newbie:** I want to check out this app so that I can explore my password manager options. Newbies are users who are new to PointGuard and are interested in exploring its features and functionalities. Motivating newbies to become regular consumers is a key goal.

#### Administrator

Administrators play a crucial role in ensuring the stability, maintenance, and security of the PointGuard system. They are divided into distinct teams to handle different aspects effectively.

1. **Network Engineers:** I want to ensure that the physical network systems are working correctly. This team focuses on the underlying physical infrastructure of the network, ensuring its reliability and functionality.
2. **Cloud Sustainment:** I want to manage the cloud-based network aspects efficiently. This team oversees the cloud overlay of the network, ensuring seamless operations and connectivity in the cloud environment.
3. **UI Designer:** I want to focus on enhancing the usability and user experience of the application. The UI designer team prioritizes creating an intuitive and user-friendly interface for PointGuard, optimizing user interactions.
4. **Cyber Security:** I want to act as advisors to other teams to ensure that security remains a primary focus. This team collaborates with other teams to provide guidance and recommendations on implementing robust security measures across all aspects of PointGuard.

#### Web Extension

The web extension is a crucial component of PointGuard, automating password management tasks for users during web browsing. As the Web Extension, I want to monitor web usage and automatically input passwords for users to streamline their experience. The web extension's objective is to simplify password management by monitoring web activities, detecting login pages, and automatically filling in credentials when necessary.

### Critical Use Cases

PointGuard revolves around three main actors: User, Administrator, and Web Extension, with six key app functions: login, view, add, update, generate passwords, and admin functions. The use case diagram (Figure 1) illustrates these relationships and functions.

![Use Case Diagram Showing the Relationship Between Actors and Functions](UseCaseDiagram_v2.drawio%20(3).png)

Out of the 6 main functions, there are 3 pivotal functions to understanding what makes PointGuard, the best password manager on the market. Below, we will explore how to Add Passwords, Generate Password from the Users perspective and Update Password from the web extension.

#### Use Case 1: Add Password

**Primary Actor:** User

**Basic Flow:**

1. User navigates to the "Add Entry" section.
2. User inputs the website URL, login username, and password.
3. User optionally categorizes the entry or adds it to a folder.
4. User saves the entry.
5. The application encrypts and stores the password entry in the vault.

**Entry Conditions:**

- The user is logged into the Password Manager application.
- The user has verified their identity through any required security measures (e.g., MFA).

**Exit Conditions:**

- A new password entry is successfully created and stored in the vault.
- The user is notified of the successful addition.

**Nonfunctional Requirements and Constraints:**

- **Security:** Use AES-256 encryption for storing password entries. Ensure all data transmission is secured with TLS.
- **Usability:** Provide a simple and intuitive interface for adding new entries. Auto-fill the website's favicon to help users identify entries visually.

#### Use Case 2: Update Password

**Primary Actor:** Web Extension

**Basic Flow:**

1. User navigates to a login page of a registered website, where the Web Extension detects login fields and queries the Password Manager for stored credentials.
2. The Password Manager decrypts and sends back the credentials to the Web Extension, which auto-fills the login fields.
3. If the user updates or creates a new account, the Web Extension prompts the user to save these new credentials.
4. The user confirms, and the Web Extension sends the new credentials to the Password Manager for encryption and storage.
5. The user is notified of the successful auto-fill or credential update by the Web Extension.

**Entry Conditions:**

- The user has the Web Extension installed and enabled in their web browser.
- The user is logged into the Password Manager application with valid session authentication (e.g., MFA).
- The website being accessed is recognized by the Password Manager application, and credentials are stored.

**Exit Conditions:**

- Login credentials are successfully auto-filled into the login page, or new/updated credentials are stored.
- The user is notified of any successful auto-fill or credential update by the Web Extension.

**Nonfunctional Requirements and Constraints:**

- **Security:** Communication between the Web Extension and Password Manager application must be encrypted. Credentials should only be decrypted transiently for auto-filling purposes and not stored locally by the Web Extension.
- **Usability:** The Web Extension should be lightweight and not impact web page loading times. User prompts for saving new or updated credentials should be clear and minimally intrusive.

#### Use Case 3: Generate Password

**Primary Actor:** User

**Basic Flow:**

1. User clicks on the "Generate Password" button.
2. The application presents options for password complexity, including length and character types (symbols, numbers, uppercase, lowercase).
3. User selects desired complexity settings and generates the password.
4. User can accept the generated password or generate a new one if unsatisfied.
5. Once accepted, the password is automatically filled in the password field for the entry.

**Entry Conditions:**

- The user is creating a new password entry or updating an existing one.
- The user selects the option to generate a strong password.

**Exit Conditions:**

- A strong, complex password is generated, accepted by the user, and stored in the entry.
- The user is informed about the successful password generation.

**Nonfunctional Requirements and Constraints:**

- **Security:** Ensure generated passwords are cryptographically secure and meet selected complexity criteria.
- **Usability:** The password generation feature should be easily accessible within the entry creation and updating flows. Provide clear options for customizing the generated password's complexity.

## Interface Design

### Visual Design

**General Appearance:** PointGuard's visual design principles are centered around modernity and sleekness. These principles guide every aspect of our design decisions to ensure a cohesive and user-friendly interface.

**Color Scheme:** Our chosen color scheme reflects the modern and sleek aesthetic we aim for. The colors are carefully selected to enhance usability and visual appeal. Here are the main colors used in PointGuard's interface:

| Color                                                      | Hex Code  |
|------------------------------------------------------------|-----------|
| ![Color 1](https://via.placeholder.com/15/006D77?text=+)  | `#006D77` |
| ![Color 2](https://via.placeholder.com/15/83C5BE?text=+)  | `#83C5BE` |
| ![Color 3](https://via.placeholder.com/15/EDF6F9?text=+)  | `#EDF6F9` |
| ![Color 4](https://via.placeholder.com/15/FFDDD2?text=+)  | `#FFDDD2` |
| ![Color 5](https://via.placeholder.com/15/E29578?text=+)  | `#E29578` |

The choice of blue as the primary color aligns well with the trustworthiness theme, as blue is often associated with trust and reliability (https://www.colorpsychology.org/blue/). Complementing it with orange, which is inviting and energetic, adds a pleasant contrast and enhances the overall user experience (https://www.colorpsychology.org/orange/). This color combination can indeed help in conveying a sense of trust to users.

**Flowchart Diagram:**

![Flowchart of the different screens with PointGuard](Flowcart%20P03%20SecureInterfaceDesign%20(1).pdf)

**Flow and Design:** Initially, users are greeted by the welcome screen. After clicking welcome, the user is presented with the login screen. Here, the user can type in their username and password to log in or click the signup button. After logging in, the user can interact with the home screen. Here, the user has three options: 'generate password' screen, 'retrieve password' screen, and 'crack me' screen. There is another flow for the app using the web extension. For this special case, the user is currently on a webpage and clicks the web extension. This activates the web extension to ask for the password from the database and autofill it into the web page's forum.

**Homescreen:** The visual design is simple and clean, with a bamboo background and three buttons. The buttons are "Generate Password", "Access Password", and "Crack Me!". The user can click on any of the buttons to perform the corresponding user actions. The "Generate Password" button will generate a new password. The "Access Password" button will allow the user to access a previously generated password. The "Crack Me!" button will attempt to crack a password that a user has entered.

The design provides good feedforward in the form of signifiers and constraints. The buttons are clearly labeled, and the user can easily understand what each button does. The design also provides good feedback in the form of visual cues. When the user clicks on a button, the button changes color to indicate that it has been pressed. The user is also given feedback in the form of text that appears on the screen. For example, when the user clicks on the "Generate Password" button, the screen will display the message "Password generated successfully" message.

Overall, the visual design is simple, clean, and easy to use. The design provides good feedforward and feedback, which makes it easy for the user to understand how to use the application.

**Generate Password Screen:** Once the user accesses the 'generate password' screen, the user is greeted with a simple and usable screen. From top to bottom, the user is showcased to a blue banner with black text saying, "Generate Password". Below that is the automatically generated password that will be displayed to the user. To the right of that is a small button with an arrow to store the password. Additionally, the user should be able to click on it and it automatically stores the password in the copy-and-paste vault. Below that the user has three toggle buttons to manage password complexity. By default, they will already be preselected to ensure the strongest password. Then below that, the user will have a slider to pick a range of 0 to 18 characters long. Here, 0 will be automatically selected and the user will have to actively change the password length. As shown in our flow chart, the toggle buttons demonstrate unity by being level with each other and being the same size. This visually tells the user that they are all equal in value. Moreover, the buttons will provide feedback to the user when they are clicked by displaying or removing a checkmark. Moreover, the circle with have a carrot symbol (>) to signify to the user to click and drag to the right to increase password length.

To access this page in our web application, below the sequence diagram will illustrate the process.

![Sequence Diagram for Generate Password](genPasswordSequenceDiagram.png)

To elaborate, the user will have to log in on the welcome screen. From there, the user will access the home screen. After selecting the 'generate password' button, the user will go to the appropriate screen. After selecting the password length slider, the generated password will run the generated password and display it on the screen. After being satisfied with the password, the user will click the 'store' button. Here, the generated password screen will be posted to the database and the database will send a confirmation. After this, the user can exit and return to the home screen.

As shown in the state machine diagram, the user is very limited in their access to different roles.

![State Machine Diagram for Generate Password](genPasswordStateDiagram.png)

While on the login screen, any user is put into active mode. After successfully logging in, the user is elevated to user mode. Then, while the application generates the password and stores it in the database, the user is temporarily in password mode to access these more private functions. Afterward, the user is returned to user\_mode.

As shown in the State diagram and the Required Password sequence diagram below they are different then the one used for generating the password.

![State Diagram for Password requirements and State machine](ReqPasswordSequence&State.pdf)

**Retrieve Password Screen:** Following the user activating the web extension the program will always be checking if there is a prompt to enter a password on a page. If the user comes to

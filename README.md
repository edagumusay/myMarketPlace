# <img width="14" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/04f97134-f293-47cf-b122-bc9721cc3eb7"> myMarketPlace
myMarketPlace is an online marketplace designed to simplify the way we buy and sell.<br><br>

# The Aim Of The <img width="14" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/04f97134-f293-47cf-b122-bc9721cc3eb7"> myMarketPlace
To start with, every user can create their own account via “Sign up” page. Users can see the Recent items posted or create a “New item”. New Item page allows users to do following:
- Choose a Category
- Write the Name of the new item
- Write a description
- Determine the price
- Choose an image file

Finally, “Submit”.
After all, buyers will be able to see added items in the Recent items section or they can “Search for...” their desired item through the browser.

Users can browse their desired items also by category through the browser. Buyers can contact the seller and initiate a chat.<br><br>

# Dataflow
<img width="350" alt="data flow" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/ed33fd51-80cd-4fdd-9562-15a7f17227ab"><br><br>

# UI (User Interface)

Home page (http://127.0.0.1:8001/?page=2)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/9c9e7193-dd44-46f4-ac54-b03d7f973f68"><br><br>

Sign up page (http://127.0.0.1:8001/signup/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/da713cd4-4ce1-4c56-ab3e-722cfd93947a"><br><br>

Log in page (http://127.0.0.1:8001/login/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/d22f2a28-d338-43b9-8021-a09fab3008e4"><br><br>

Adding a new item (http://127.0.0.1:8001/items/new/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/ef70e4f2-832b-407f-bb1c-afa65e3e0a4e"><br><br>

Inbox page (http://127.0.0.1:8001/inbox/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/657452f2-59b9-4434-bfde-b3ec5f27f162"><br><br>

Conversation (http://127.0.0.1:8001/inbox/9/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/7e417862-f871-4079-ba0b-8b8961eba3aa"><br><br>

myPage (http://127.0.0.1:8001/dashboard/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/e59a50ac-3d15-4ba9-8343-b8fc100a3c0d"><br><br>

An item’s page (http://127.0.0.1:8001/items/13/)

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/fa259621-8c5c-4079-a87a-d21843f51f2b"><br><br><br>

# Code Structure

- **Models**

Every item is bound to a Category which has a name field. Every item itself has a name, description, price, image, is_sold, created_by and created_at fields.

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/b6640676-ca1f-4d89-91fc-4bf3fd50a15e"><br>

Every message is bound to a Conversation which has an item and members (users) field. Every message itself has a content, created_by and created_at fields.

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/62c2491a-8274-4869-b861-94d080bb3cc1"><br><br><br>


- **Urls**

Basically, every functionality has its path and relevant method defined.

Because I developed this website in a local environment, I added static media url path for the media files.

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/7cb31268-25b7-4e94-8a73-e1547be0d2a8"><br>

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/f146b138-951f-4833-ad68-ba0534e47c31"><br>

Functionalities like viewing, editing, deleting an item require a unique identifier (primary key pk) in its paths.

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/e75f5620-eae9-426a-92a0-9f496a05c8f5"><br>

<img width="470" alt="image" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/7bf1f1f7-ebd3-466a-991c-91df41042aee">

I also defined the name for these paths, so I could use them easily in html elements (mainly buttons).<br><br><br>

- Views

<img width="470" alt="Screen Shot 2023-10-28 at 10 02 57 PM" src="https://github.com/edagumusay/myMarketPlace/assets/81931479/ea4d6878-48c4-4ada-90e8-1531016232e2">

Each of these files you see extends core/base.html as I wanted to avoid too much repetition.<br><br><br>

- Tests

I have implemented 17 automated unit tests which test several edge cases for different apps inside the project (e.g., new item form being invalid in case of string price).

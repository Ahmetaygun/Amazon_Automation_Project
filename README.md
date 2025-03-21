**# 🧪 Amazon.com.tr Automation Project

This project is developed as part of the Bootcamp Automation Challenge. It automates a user journey on [Amazon.com.tr](https://www.amazon.com.tr/) using **Python**, **Selenium WebDriver**, and follows the **Page Object Model (POM)** design pattern.

## 📅 Deadline
**March 19, 2025 – 19:00 (GMT+3)**

---

## ✅ Project Requirements

- Use any programming language + test automation framework (**Java** or **Python** preferred)
- BDD frameworks such as **Cucumber, Codeception, Quantum** are **not allowed**
- Must fully implement **Page Object Model (POM)** principles

---

## 🔍 Test Steps

1. Go to https://www.amazon.com.tr/
2. Verify the homepage is displayed
3. Search for **"samsung"**
4. Verify search results are shown
5. Click on the **2nd page** of search results and verify
6. Click on the **3rd product** on the page
7. Verify product page is opened
8. Add product to cart
9. Verify product is added to cart
10. Go to the cart page
11. Verify product in cart
12. Delete product from cart and verify
13. Return to homepage and verify

---

## 🧱 Project Structure

```bash
amazon-automation/
│
├── pages/                      # Page Object classes
│   ├── base_page.py            # Base page with common actions
│   ├── home_page.py
│   ├── search_results_page.py
│   ├── product_page.py
│   ├── cart_page.py
│
├── tests/
│   └── test_amazon.py          # Main test scenario 
│
├── utils/
│   └── driver_factory.py       # Driver setup & teardown
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project info

⚙️ Installation
Clone the repository:
git clone https://github.com/yourusername/amazon-automation.git
cd amazon-automation

Run the test:
pytest tests/test_amazon.py

🧪 Technologies Used
Python 3.11
Selenium WebDriver
PyTest
Page Object Model (POM)

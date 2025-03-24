1. Extract the file.
2. Open the file in your IDE (eg. VS Studio).
3. Run pip install requirements.txt to install all the required libraries
4. Run the line python get_exhibitors_names.py
5. You will get a csv named all_exhibitors_scrapes.csv with a list of all company names from the 3 exhibitions.
6. Use Enriched-companies.csv which we got from Clay Table and run the line Python scoring.py
7. You will get scored_companies.csv as output with a score for each company.
8. Run Python generate_personalized_messages.py to generate messages using openai.
9. You will get scored_companies_1.csv with the outreach message to the decision maker of the company. 
10. To run the dashboard locally, run the line streamlit run streamlit_dashboard.py or view the link in the report.
11. There is a Python script named send_email_mock.py, its a placeholder code which serves as a mock automation tool that simulates the process of locating contact information—specifically, email addresses—generating personalized outreach messages, and sending those emails to the respective contacts. Given the appropriate API keys and credentials, this mock script can be adapted into a fully functional email automation solution.
from flask import Flask, render_template

app = Flask(__name__)

# Education Data
EDUCATION = [
    {"level": "Fourth Year", "institution": "Dr. D. Y. Patil School of Science and Technology, Tathawade-Pune", "university": "Dr. D. Y. Patil Vidyapeeth, Pune", "year": "2025-2026", "grade": "Appearing", "highlight": "Focusing on Data Structures, Algorithms & AI/ML."},
    {"level": "Third Year", "institution": "Dr. D. Y. Patil School of Science and Technology, Tathawade-Pune", "university": "Dr. D. Y. Patil Vidyapeeth, Pune", "year": "2024-2025", "grade": "8.32 (Aggregate)", "highlight": "Focusing on Data Structures, Algorithms & AI/ML."},
    {"level": "Second Year", "institution": "Dr. D. Y. Patil School of Science and Technology, Tathawade-Pune", "university": "Dr. D. Y. Patil Vidyapeeth, Pune", "year": "2023-2024", "grade": "8.65 (Aggregate)", "highlight": "Volunteer – Student Council."},
    {"level": "First Year", "institution": "Dr. D. Y. Patil School of Science and Technology, Tathawade-Pune", "university": "Dr. D. Y. Patil Vidyapeeth, Pune", "year": "2022-2023", "grade": "7.39 (Aggregate)", "highlight": "Active member of Coding Club."}
]

# Schooling Data
SCHOOLING = [
    {"level": "12th (HSC)", "sub": "Science (PCM with Computer Science)", "institution": "Moolji Jaitha College, Jalgaon", "university": "State Board-Maharashtra", "year": "2021-2022", "grade": "60.50%", "highlight": "Participated in college-level sports tournament."},
    {"level": "10th (SSC)", "sub": "General Education", "institution": "Orion English Medium School, Jalgaon", "university": "State Board-Maharashtra", "year": "2019-2020", "grade": "67.00%", "highlight": "First Prize – School Flower Decoration Competition."}
]

# Projects Data
PROJECTS = [
    {"title": "ATS Resume Scanner", "desc": "A Python-based tool utilizing NLP to analyze resumes against job descriptions.", "tech": ["Python", "NLP", "Flask"], "link": "https://github.com/Chinmay-3737/ast-pro"},
    {"title": "CoffeeShop", "desc": "A modern coffee shop ordering and management platform with real-time order tracking, inventory management platform.", "tech": ["Node.js", "MongoDB", "Tailwind CSS"], "link": "https://github.com/Chinmay-3737/coffee"},
    {"title": "Vyronex Motors", "desc": "Luxury custom car workshop digital experience with 3D branding.", "tech": ["Three.js", "Web Design", "GSAP"], "link": "https://vyronex-motors-kzee.vercel.app/"},
    {"title": "Diwali Sales Analysis", "desc": "Performed sales analysis on Diwali sales data using Python.", "tech": ["Python", "Data Analysis"], "link": "https://github.com/Chinmay-3737/Diwali_Sales_Analysis"},
    {"title": "Customer Churn Data", "desc": "Performed exploratory data analysis on customer churn dataset using Python.", "tech": ["Python", "Data Analysis"], "link": "#"},
    {"title": "Sales Performance Dashboard", "desc": "Built an interactive Power BI dashboard to visualize sales trends, top products, and customer insights for data-driven decisions.", "tech": ["PowerBI", "Data Visualization", "DashboardDesign"], "link": "#"},
    {"title": "Super Store Dashboard", "desc": "Designed an Interactive Power BI Dashboard.", "tech": ["Business Analysis", "Excel", "PowerBI"], "link": "#"},
    {"title": "Uber Dashboard", "desc": "Designed an Interactive Power BI Dashboard analyzing ride-sharing data.", "tech": ["Dashboard Design", "Excel", "PowerBI", "DashboardDesign"], "link": "#"},
    {"title": "Spotify Dashboard", "desc": "Designed an Interactive Power BI Dashboard analyzing music streaming data.", "tech": ["PowerBI", "Data Visualization", "DashboardDesign"], "link": "#"},
    {"title": "Portfolio Website", "desc": "A personal portfolio website to showcase projects and skills.", "tech": ["React", "CSS", "Framer Motion", "Responsive Design"], "link": "https://chinmay.corvaya.in/"},
]

# Add this near your other data lists in app.py
CONTACT_INFO = {
    "email": "chinmaychaudhari312@gmail.com",
    "linkedin": "https://www.linkedin.com/in/chaudhari-chinmay/",
    "github": "https://github.com/Chinmay-3737",
    "location": "Pune, India"
}
@app.route('/')
def home():
    # Adding contact=CONTACT_INFO fixes the UndefinedError
    return render_template('index.html', 
                           projects=PROJECTS, 
                           education=EDUCATION,
                            schooling=SCHOOLING, 
                           contact=CONTACT_INFO)

if __name__ == '__main__':
    app.run(debug=True)
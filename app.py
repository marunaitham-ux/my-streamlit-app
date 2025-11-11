from flask import Flask, render_template_string

app = Flask(__name__)

# Simple HTML template with placeholders for photos
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Government Tribal Welfare Residential Degree College for Women, Boath, Adilabad</title>
</head>
<body>
    <h1>Welcome to Government Tribal Welfare Residential Degree College for Women, Boath, Adilabad</h1>
    <p>This is a sample website for the college.</p>
    
    <h2>College Photos</h2>
    <img src="/static/photo1.jpg" alt="College Photo 1" width="300">
    <img src="/static/photo2.jpg" alt="College Photo 2" width="300">
    <!-- Add more <img> tags for additional photos, e.g., <img src="/static/photo3.jpg" ...> -->
    
    <p>For more information, visit the official site or contact the college.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)

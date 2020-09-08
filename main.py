from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

references = {
    'bluefuse': {
        'name': 'Andy Ewings',
        'phone': '01225758181',
        'email': 'andy.e@bluefusesystems.com',
        'title': 'Owner',
        'company': 'Bluefuse Systems'
    },
    'uob': {
        'name': 'Dr Fabio Nemetz',
        'phone': '',
        'email': 'f.nemetz@bath.ac.uk',
        'title': 'Director of Studies',
        'company': 'University of Bath'
    },
    'henley': {
        'name': 'David Binney',
        'phone': '',
        'email': 'david@hisl.co.uk',
        'title': 'Lead Consultant',
        'company': 'Henley IS'
    },
}

projects = [
    {
        'photo': '/static/images/projects/bluefuse.png',
        'link': '/work/bluefuse',
    },
    {
        'photo': '/static/images/projects/bath.jpg',
        'link': '/work/university',
    },
    {
        'photo': '/static/images/projects/website.png',
        'link': '/work/website',
    },
]

navigationMenu = {
    'home': '/',
    'about': '/about',
    'skills': '/about/skills',
    'hobbies': '/about/sport',
    'travel': '/about/travel',
    'food': '/about/food',
    'work': '/work',
    'bluefuse': '/work/bluefuse',
    'university': '/work/university',
    'contact': '/contact',
    'linkedIn': 'https://uk.linkedin.com/in/thomas-wooliston-1a3123149',
}

notes = {
    'title': 'Relevant Notes',
    'allText': [
        {
            'brokenText': 'Graduated in July 2020',
        },
        {
            'brokenText': 'Interested in working close with design in a project-based environment',
        },
        {
            'brokenText': 'Passion in understanding the best way to design interactive systems',
        },
        {
            'brokenText': 'Experience as a front and back-end developer',
        },
        {
            'brokenText': 'Currently located in London but flexible',
        },
    ],
}

career = {
    'title': 'Career Objectives',
    'allText': [
        {
            'brokenText': """
            I am particularly interested in roles where I would be working close with design in a project-based
            environment. My passion for design comes from being exposed to various interfaces. From a young age,
            I have found a lot of designs overly complicated and am motivated to make the user experience as
            attractive and accessible as possible.
            """,
        }
    ],
}

education = {
    'title': 'Education',
    'allText': [
        {
            'photo': '/static/images/education/bath.jpg',
            'brokenText': 'University of Bath',
            'link': '/about/bath',
            'website': 'https://www.bath.ac.uk/',
        },
        {
            'photo': '/static/images/education/landmark.jpg',
            'brokenText': 'Landmark Forum',
            'link': '/about/landmark',
            'website': 'https://www.landmarkworldwide.com/',
        },
        {
            'photo': '/static/images/education/graveney.jpg',
            'brokenText': 'Graveney Sixth Form',
            'link': '/about/graveney',
            'website': 'https://www.graveney.org/',
        },
        {
            'photo': '/static/images/education/lfcg.png',
            'brokenText': 'Lycée Français Charles de Gaulle',
            'link': '/about/lfcg',
            'website': 'https://www.lyceefrancais.org.uk/',
        },
    ],
}

qualifications = [
    'Registered IT Technician for Software Development with BCS - 2020',
    'Landmark Leadership Advanced Course - 2016',
    'Duke of Edinburgh Silver Award - 2016',
    'Landmark Forum (Leadership Development) - 2015',
    'National Citizenship Service Certificate - 2014',
]

skills = {
    'coding': ['JavaScript and TypeScript', 'HTML and CSS/SCSS', 'Python', 'PHP', 'SQL', 'C', 'WebGl', 'MATLAB'],
    'software': ['Visual Studio, Intelij, Eclipse, PyCharm (developer tools on browsers)',
                 'Github, Github Desktop',
                 'Microsoft SQL Server Management Studio',
                 'KiTTY and PuTTy',
                 'Jupyter',
                 'Slack',
                 'Microsoft Office Applications'],
    'languages': ['Bilingual in English and French', 'Spanish to a B1 level']
}

interests = {
    'sport':
    {
        'basketball': [
            'Participle in University scrimmages as well as in London',
            'Work as part of a team to overcome the challenges presented by the opposing team',
            'Quarantine has slowed things down in relation to basketball games but hope to start it up again soon',
        ],
        'swimming': [
            'Commitment to swimming once a week for many years',
            'Keep working on my technique on my own',
            'With the closure of gyms and pools, I have not been able to continue with swimming',
        ],
        'running': [
            'As a consequence of COVID-19, I have taken up running',
            'I have a history of having good endurance due to swimming regularly',
            'This activity has been my alternative to the two previous sports',
        ],
    },
    'travelIntro': [
                'Enjoy traveling every year with my friends',
                'Organise the holidays’ accommodation and flights',
                'Have an active group and plan to go on hikes to reach tourist sites',
            ],
    'travel': [
        {
            'text': [
                'Berlin 2020',
            ],
            'photos': [
                '/static/images/interests/Travel/berlin2020/1.jpg',
                '/static/images/interests/Travel/berlin2020/2.jpg',
                '/static/images/interests/Travel/berlin2020/3.jpg',
                '/static/images/interests/Travel/berlin2020/4.jpg',
                '/static/images/interests/Travel/berlin2020/5.jpg',
                '/static/images/interests/Travel/berlin2020/6.jpg',
                '/static/images/interests/Travel/berlin2020/7.jpg',
                '/static/images/interests/Travel/berlin2020/8.jpg',
            ]
        },
        {
            'text': [
                'Estonia 2020',
            ],
            'photos': [
                '/static/images/interests/Travel/estonia2020/1.JPG',
                '/static/images/interests/Travel/estonia2020/2.jpg',
                '/static/images/interests/Travel/estonia2020/3.jpg',
                '/static/images/interests/Travel/estonia2020/4.jpg',
                '/static/images/interests/Travel/estonia2020/5.jpg',
                '/static/images/interests/Travel/estonia2020/6.jpg',
                '/static/images/interests/Travel/estonia2020/7.jpg',
                '/static/images/interests/Travel/estonia2020/8.jpg',
            ]
        },
        {
            'text': [
                'The Hague 2020',
            ],
            'photos': [
                '/static/images/interests/Travel/hague2020/1.jpg',
                '/static/images/interests/Travel/hague2020/2.jpg',
            ]
        },
        {
            'text': [
                'Jordan 2019',
            ],
            'photos': [
                '/static/images/interests/Travel/jordan2019/1.jpg',
                '/static/images/interests/Travel/jordan2019/2.jpg',
                '/static/images/interests/Travel/jordan2019/3.jpg',
                '/static/images/interests/Travel/jordan2019/4.jpg',
                '/static/images/interests/Travel/jordan2019/5.jpg',
                '/static/images/interests/Travel/jordan2019/6.jpg',
                '/static/images/interests/Travel/jordan2019/7.jpg',
                '/static/images/interests/Travel/jordan2019/8.jpg',
                '/static/images/interests/Travel/jordan2019/9.jpg',
                '/static/images/interests/Travel/jordan2019/10.jpg',
                '/static/images/interests/Travel/jordan2019/11.jpg',
                '/static/images/interests/Travel/jordan2019/12.jpg',
                '/static/images/interests/Travel/jordan2019/13.jpg',
                '/static/images/interests/Travel/jordan2019/14.jpg',
                '/static/images/interests/Travel/jordan2019/15.jpg',
                '/static/images/interests/Travel/jordan2019/16.jpg',
                '/static/images/interests/Travel/jordan2019/17.jpg',
                '/static/images/interests/Travel/jordan2019/18.jpg',
                '/static/images/interests/Travel/jordan2019/19.jpg',
            ]
        },
        {
            'text': [
                'Porto 2020',
            ],
            'photos': [
                '/static/images/interests/Travel/porto2019/1.jpeg',
                '/static/images/interests/Travel/porto2019/2.jpeg',
                '/static/images/interests/Travel/porto2019/3.jpg',
                '/static/images/interests/Travel/porto2019/4.jpg',
                '/static/images/interests/Travel/porto2019/5.jpg',
            ]
        },
        {
            'text': [
                'Kitzbuhel 2018',
            ],
            'photos': [
                '/static/images/interests/Travel/Kitzbuhel/1.jpg',
                '/static/images/interests/Travel/Kitzbuhel/2.jpg',
                '/static/images/interests/Travel/Kitzbuhel/3.jpg',
                '/static/images/interests/Travel/Kitzbuhel/4.jpg',
                '/static/images/interests/Travel/Kitzbuhel/5.jpg',
                '/static/images/interests/Travel/Kitzbuhel/6.jpg',
            ]
        },
        {
            'text': [
                'Interrail Across Spain 2017',
            ],
            'photos': [
                '/static/images/interests/Travel/spain2017/1.jpg',
                '/static/images/interests/Travel/spain2017/2.jpg',
                '/static/images/interests/Travel/spain2017/3.jpg',
                '/static/images/interests/Travel/spain2017/4.jpg',
                '/static/images/interests/Travel/spain2017/5.jpg',
                '/static/images/interests/Travel/spain2017/6.jpg',
                '/static/images/interests/Travel/spain2017/7.jpg',
                '/static/images/interests/Travel/spain2017/8.jpg',
                '/static/images/interests/Travel/spain2017/9.jpg',
                '/static/images/interests/Travel/spain2017/10.jpg',
            ]
        },
    ],
    'food': [
        {
            'text': [
                'Practising cooking intricate dishes',
                'Enjoying meals that require precise execution of a recipe',
                'Trying to recreate recipes from memory',
                'Using techniques and flavour combinations that I have learnt to then use in future cooking',
            ],
            'photos': [
                '/static/images/interests/Food/1.jpg',
                '/static/images/interests/Food/2.jpg',
                '/static/images/interests/Food/3.jpg',
                '/static/images/interests/Food/4.jpg',
                '/static/images/interests/Food/5.jpg',
                '/static/images/interests/Food/6.jpg',
                '/static/images/interests/Food/7.jpg',
                '/static/images/interests/Food/8.jpg',
                '/static/images/interests/Food/9.jpg',
                '/static/images/interests/Food/10.jpg',
            ]
        },
    ],
}

landmark = {
    'companies': [
        '/static/images/Landmark/apple.jpg',
        '/static/images/Landmark/lululemon.png',
        '/static/images/Landmark/merc.png',
        '/static/images/Landmark/nasa.png',
        '/static/images/Landmark/reebok.jpg'
    ],
    'what': ["""
           Landmark is a company providing courses aiming to bring a profound impact in personal and professional
           aspects of someone's life.
           """,
             """
           As explained by Landmark, it helps achieve:
           \" the freedom to be at ease and the power to be effective in the areas that
           matter most to you: the quality of your relationships, the confidence with which you live your life, your
           personal productivity, your experience of the difference you make, your enjoyment of life.\"
           """,
             """
           The courses focus on inter-personal relationships and understanding how people think and react. Hence, being
           able to express yourself with a degree of awareness in regards to how other people could interpret the
           interaction and ultimately helping remove unnecessary tension and increase effectiveness communication.
           """,
             ],
    'why': ["""
           Learning about how people think and react has permitted a greater understanding of myself and as a result
           I have a clearer mind and am able to be more productive without overthinking aspects of my own personal life.
           """,
            """
           Understanding how something said could be interpreted differently to what was originally intended has enabled
           me to have a greater sensitivity to how someone's feedback or comment could be misunderstood or lead to 
           unintentional inter-personal conflicts.
           """,
            """
           Engaging with this course has empowered me to resolve conflicts over ignoring issues.
           """,
            """
            Self-introspection and awareness of situations causing irritability have resulted in me being more patient.
            """,
            ],
}
bath = {
    'dissertation': {
        'text': [
            'Built an app to allow users to give away food that they are no longer planning to eat themselves',
            'Implemented persuasive technique to encourage the user to complete the desired behaviour',
            'Investigated HCI techniques, in academic papers, to develop an interface with a greater user '
            'experience',
            'Conducted my own research to determine the usability and persuasiveness of the system',
            'Challenged myself by learning a new language from scratch for this project',
            'Working on a solo project allowed gain more practice focusing on specific details in the system',
        ]
    },
    'standout': {
        'text': [
            {
                'name': 'Safety-Critical Computer Systems - 2:1',
                'about': 'Looking at the current state of safe systems development and '
                         'understanding of risk in systems. The content of this module '
                         'that stood out the most for me was how important the usability '
                         'of the system must upheld to ensure safe functionality. The '
                         'users of safety-critical systems must be able to react and '
                         'operate a system as accurately as possible and therefore needs '
                         'the best UX possible. ',
            },
            {
                'name': 'Human-computer interaction - 70%',
                'about': 'HCI was one of the modules I most enjoyed during my time at university. Following my '
                         'interest in design, the subject helped explicitly outline the structure that improves the '
                         'user experience which I strive to apply as much as I can throughout all of my projects.',
            },
            {
                'name': 'Computing as a science and engineering discipline - 68%',
                'about': 'This module was the first group project (of 6 people) that I completed at while studying at '
                         'Bath. While only being in first year, our group was able to produce work utilising or '
                         'diverse skill set which complimented each others contribution. My main focus during this '
                         'module was to produce the design and justification of the design which I volunteered as '
                         'being the part I most enjoyed working on. However, each member continued to help each other '
                         'by contributing to everyone\'s own section. This module was a great introduction into '
                         'teamwork and its positive and negative aspects and how the negative can be overcome with '
                         'clear communication, patience and respect.',
            },
            {
                'name': 'Integrated group-based project - 71%',
                'about': 'Following the work from \'Computing as a science and engineering discipline\', this module '
                         'provided further experience with teamwork (again with 6 people). This work occurred in '
                         'second year while studying at bath. With more experience with the computer '
                         'science discipline, the group was better able to help each other and was more flexible when '
                         'choosing roles to fill. Therefore, the group members were better able to identify issues '
                         'within the team and resolve them more efficiently and effectively.',
            },
            {
                'name': 'Theory of human computer interaction - 66%',
                'about': 'This module was used to gain an advanced level of understanding of current research issues '
                         'in human computer interaction. This module guided my rational thinking into understanding '
                         'how and why people behave and interact with a system in a certain manner; which was helpful '
                         'in further developing my research and discussion in my dissertation project.',
            },
        ]
    },
    'management': {
        'text': [
            'Entrepreneurship - marketing an app we built (team of 5)',
            'Digital business innovation - presenting a possible area of improvement to a business',
            'Business strategy - purely theory work',
        ]
    },
    'mention': {
        'text': [
            'Networking - theory',
            'Fundamentals of visual computing - building 3D objects and manipulating them in a space',
            'Databases - with PHP and SQL',
            'Artificial intelligence - small projects such as a sudoku solver',
            'Discrete and Analytical mathematics for computation - logic theory',
        ]
    },
}


profile = {
    'name': 'Thomas Wooliston',
    'email': 'thomaswooliston@gmail.com',
    'references': references,
    'links': navigationMenu,
    'projects': projects,
    'about': {
        'photo': '/static/images/face/thomas.PNG',
        'notes': notes,
        'career': career,
        'education': education,
        'qualifications': qualifications,
        'skills': skills,
        'everything': interests,
    },
    'landmark': landmark,
    'bath': bath,
}


@app.route('/')
def index():
    return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template("about.html", profile=profile)


@app.route('/about/skills')
def skills():
    return render_template("skills.html", profile=profile)


@app.route('/about/sport')
def sport():
    return render_template("sport.html", profile=profile)


@app.route('/about/travel')
def travel():
    return render_template("travel.html", profile=profile)


@app.route('/about/food')
def food():
    return render_template("food.html", profile=profile)


@app.route('/work')
def work():
    return render_template("thomas.html", profile=profile)


@app.route('/work/bluefuse')
def bluefuse():
    return render_template("bluefuse.html", profile=profile)


@app.route('/work/university')
def university():
    return render_template("university.html", profile=profile)


@app.route('/work/website')
def website():
    return render_template("website.html", profile=profile)


@app.route('/contact')
def contact():
    return render_template("contact.html", profile=profile)


@app.route('/about/bath')
def bath():
    return render_template("bath.html", profile=profile)


@app.route('/about/landmark')
def landmark():
    return render_template("landmark.html", profile=profile)


@app.route('/about/graveney')
def graveney():
    return render_template("graveney.html", profile=profile)


@app.route('/about/lfcg')
def lfcg():
    return render_template("lfcg.html", profile=profile)


if __name__ == "__main__":
    app.run()

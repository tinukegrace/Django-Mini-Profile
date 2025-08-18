from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   
    context = {
        'name': 'Ogun Tinuke Grace',
        'welcome_text': 'Welcome to my digital portfolio',
        'skills': [
            {
                'icon': '💻',
                'title': 'Programming',
                'description': 'Python, HTML/CSS, Django'
            },
            {
                'icon': '📊',
                'title': 'Data Analysis',
                'description': 'Excel, SQL, Data Visualization'
            },
            {
                'icon': '🗣️',
                'title': 'Communication',
                'description': ' Technical Writing'
            }
        ],
        'aspirations': {
            'title': 'My Aspirations',
            'content': 'I aspire to become a full-stack developer who creates meaningful digital experiences that solve real-world problems. My goal is to work with innovative teams that push the boundaries of technology while making a positive impact on society. I\'m passionate about continuous learning and staying at the forefront of emerging technologies.'
        }
    }
    return render(request, 'home.html', context)

def about(request):
    """
    About page view
    """
    context = {
        'name': 'Ogun Tinuke Grace',
        'about_sections': [
            {
                'title':'My Story',
                'content': 'I\'m a passionate individual with a love for technology and creativity. My journey began with curiosity about how things work, which led me to explore programming and digital design. I believe in the power of technology to transform lives and create positive change in the world.'
            },
            {
                'title': 'Education & Background',
                'content': 'Currently pursuing my degree in Computer Science with a focus on Data Science/Machine Learning. I\'ve completed various online courses and certifications in web development, data science, and user experience design. I\'m always eager to learn new technologies and stay updated with industry trends.'
            },
            {
                'title': 'What Drives Me',
                'content': 'I\'m motivated by challenges that require creative problem-solving and innovative thinking. I enjoy collaborating with diverse teams and believe that the best solutions come from combining different perspectives. Whether it\'s building a new application or solving a complex algorithm, I approach every task with enthusiasm and dedication.'
            },
            {
                'title': 'Current Focus',
                'content': 'Currently, I\'m focusing on mastering full-stack development, particularly modern Python frameworks and cloud technologies. I\'m also exploring machine learning and artificial intelligence to understand how these technologies can be integrated into web applications to create smarter, more intuitive user experiences.'
            },
    
        ]
    }
    return render(request, 'about.html', context)


def contact(request):
    """
    Contact page view
    """
    context = {
        'name': 'Ogun Tinuke Grace',
        'email': 'tinuke.grace@example.com',
        'whatsapp': '+234 XXX XXX XXXX',
        'intro_text': 'I\'d love to hear from you! Feel free to reach out through any of the following channels.',
        'contact_methods': [
            {
                'icon': '📧',
                'title': 'Email',
                'value': 'tinuke.grace@gmail.com',
                'description': 'Best for professional inquiries'
            },
            {
                'icon': '📱',
                'title': 'WhatsApp',
                'value': '+234 XXX XXX XXXX',
                'description': 'Quick messages and calls'
            }
        ],
        'social_links': [
            {'name': 'LinkedIn', 'icon': '💼', 'url': '#'},
            {'name': 'GitHub', 'icon': '🐱', 'url': '#'},
            {'name': 'Twitter', 'icon': '🐦', 'url': '#'},
            {'name': 'Instagram', 'icon': '📷', 'url': '#'},
            {'name': 'Facebook', 'icon': '📘', 'url': '#'},
        ],
        'collaboration': {
            'title': 'Let\'s Collaborate!',
            'content': 'Whether you have a project in mind, want to discuss opportunities, or just want to connect, I\'m always open to meaningful conversations. Don\'t hesitate to reach out!'
        }
    }
    return render(request, 'contact.html', context)
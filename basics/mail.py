from django.core.mail import EmailMessage
from django.template.loader import render_to_string

video_url = "https://www.youtube.com/watch?v=0wkdRPI0ZCY"
context = {"video_url": video_url}
html_content = render_to_string("email_template.html", context)

email = EmailMessage(
    'Subject',
    html_content,
    'from@example.com',
    ['to@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)

email.content_subtype = "html"
email.send()

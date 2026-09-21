from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LOGO='logos/reclora/Reclora%20logo.png'

def rel(path,target):
    return Path(__import__('os').path.relpath(ROOT/target,path.parent)).as_posix()

for path in ROOT.rglob('*.html'):
    if '.git' in path.parts or 'account-test' in path.parts:
        continue
    text=path.read_text(encoding='utf-8',errors='ignore')
    prefix=rel(path,'reclora-theme.css')
    logo=rel(path,'logos/reclora/Reclora logo.png').replace(' ','%20')
    account=rel(path,'account-test/index.html')
    if 'reclora-theme.css' not in text and '</head>' in text:
        text=text.replace('</head>',f'<link rel="stylesheet" href="{prefix}"></head>',1)
    text=text.replace('recroom.network','RecLora').replace('Rec Room','RecLora')
    text=text.replace('#FF6727','#0b7f86').replace('#FF5C00','#0b7f86')
    text=re.sub(r'content=["\']/logo\.png',f'content="{logo}',text)
    text=re.sub(r'(href=["\'])/logo\.png',r'\1'+logo,text)
    if 'data-reclora-brand' not in text and '<body>' in text:
        brand=(f'<div data-reclora-brand class="reclora-brandbar"><a href="{rel(path,"index.html")}"><img src="{logo}" alt="RecLora logo"><span>RecLora</span></a><a class="reclora-account-link" href="{account}">Test accounts</a></div>')
        text=text.replace('<body>','<body>'+brand,1)
    path.write_text(text,encoding='utf-8')
print('Applied RecLora shared branding to mirrored HTML pages.')

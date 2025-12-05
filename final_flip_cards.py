#!/usr/bin/env python3
"""Complete flip card implementation - add CSS and update HTML"""

import re

# Detect encoding
def detect_and_read(filepath):
    """Read file trying multiple encodings"""
    for encoding in ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read(), encoding
        except:
            pass
    raise Exception("Could not read file with any encoding")

# Read the file
content, encoding = detect_and_read('index.html')
print(f"✅ Read file with encoding: {encoding}")

# STEP 1: Add flip card CSS before </style>
flip_css = '''
        /* Team Member Flip Card Animation */
        .team-member { perspective: 1000px; cursor: pointer; position: relative; min-height: 400px; }
        .team-member-inner { position: relative; width: 100%; height: 100%; transition: transform 0.6s; transform-style: preserve-3d; }
        .team-member:hover .team-member-inner { transform: rotateY(180deg); }
        .team-member-front, .team-member-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; padding: 2rem 1.5rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .team-member-front { background: white; }
        .team-member-back { background: linear-gradient(135deg, var(--color-primary), var(--color-secondary)); color: white; transform: rotateY(180deg); overflow-y: auto; }
        .team-member-back h4 { font-weight: bold; margin-bottom: 0.5rem; }
        .team-member-back .role { font-size: 0.875rem; opacity: 0.9; margin-bottom: 0.75rem; }
        .team-member-back p { font-size: 0.875rem; line-height: 1.4; margin-bottom: 0.5rem; }
        .team-member-back .quote { font-size: 0.75rem; font-style: italic; opacity: 0.85; margin-top: 0.5rem; }
'''

# Add CSS if not already there
if 'team-member-front' not in content:
    content = content.replace('    </style>', flip_css + '\n    </style>')
    print("✅ Added flip card CSS")
else:
    print("⚠️ CSS already present")

# STEP 2: Update team member cards using regex with extensive context
# This pattern finds article tags and replaces the entire card
old_erick = re.compile(
    r'<article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">\s*'
    r'<div class="flex items-start gap-6">\s*'
    r'<img src="filez/eric-and-krista\.jfif"[^>]*>',
    re.DOTALL
)

# Match and update each team card
replacements = {
    # Erick & Krista
    'erick': {
        'pattern': r'<article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">\s*<div class="flex items-start gap-6">\s*<img src="filez/eric-and-krista\.jfif"[^>]*>\s*<div>\s*<h4 class="text-xl font-bold">Erick and Krista Baraza</h4>.*?</article>',
        'name': 'Erick & Krista'
    },
}

# Try a simpler approach: find and replace by image src
# Find "eric-and-krista.jfif" and work backwards to find article opening
if 'eric-and-krista.jfif' in content:
    idx = content.find('eric-and-krista.jfif')
    # Go back to find <article
    article_start = content.rfind('<article', 0, idx)
    # Go forward to find </article>
    article_end = content.find('</article>', idx) + len('</article>')
    
    old_card = content[article_start:article_end]
    print(f"Found Erick card, length: {len(old_card)}")
    
    # Create new card
    new_card = '''<article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/eric-and-krista.jfif" alt="Erick and Krista Baraza" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text=Erick+%26+Krista'">
                                    <h4 class="text-lg font-bold">Erick & Krista</h4>
                                    <p class="text-sm text-gray-600">Founders & Missionaries</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Erick & Krista Baraza</h4>
                                    <div class="role text-sm mb-2">Founders & Missionaries</div>
                                    <p class="text-sm mb-2">Passionate missionaries and founders of Angaza Tumaini, bringing hope and transformation to Kibera through the Gospel.</p>
                                    <div class="quote text-xs">"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</div>
                                </div>
                            </div>
                        </article>'''
    
    content = content[:article_start] + new_card + content[article_end:]
    print("✅ Updated Erick & Krista card")

# Similarly for other team members
team_members = [
    {
        'img': 'filez/hypeman.jpg',
        'name': 'Evans Wandera',
        'role': 'Programs Coordinator',
        'front_name': 'Evans Wandera',
        'back_name': 'Evans Wandera',
        'bio': 'Passionate about serving his community, ensuring every child receives care, mentorship, and academic support with Christ-centered love.',
        'quote': '"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6'
    },
    {
        'img': 'filez/Jackline.jpg',
        'name': 'Jackline Mueni (Jay)',
        'role': 'Administrator & Programs Manager',
        'front_name': 'Jackline (Jay)',
        'back_name': 'Jackline Mueni (Jay)',
        'bio': 'Dedicated to empowering children and families through organizational excellence and deep love for God.',
        'quote': '"Commit to the Lord whatever you do, and He will establish your plans." – Proverbs 16:3'
    },
    {
        'img': 'filez/Felix.jpeg',
        'name': 'Felix Mito (Teacher Feloh)',
        'role': 'Tutor / Teacher',
        'front_name': 'Felix (Teacher Feloh)',
        'back_name': 'Felix Mito (Teacher Feloh)',
        'bio': 'Passionate educator combining patience, creativity, and Christ-centered approach to build strong academic and spiritual foundations.',
        'quote': '"Let the wise hear and increase in learning, and the one who understands obtain guidance." – Proverbs 1:5'
    },
    {
        'img': 'filez/Naureen.jpeg',
        'name': 'Naureen Mugeni (Chief Chef)',
        'role': 'Cook',
        'front_name': 'Naureen (Chief Chef)',
        'back_name': 'Naureen Mugeni (Chief Chef)',
        'bio': 'Serves with heart to ensure every child receives nutritious meals and experiences love and warmth through her dedicated work.',
        'quote': '"So, whether you eat or drink or whatever you do, do it all for the glory of God." – 1 Corinthians 10:31'
    },
    {
        'img': 'filez/Ben.jpeg',
        'name': 'Benard Owira (Benah)',
        'role': 'Support Staff',
        'front_name': 'Benard (Benah)',
        'back_name': 'Benard Owira (Benah)',
        'bio': 'Serves with humble dedication and pride, keeping the center clean, safe, and welcoming through servant-leadership.',
        'quote': '"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23'
    }
]

for member in team_members:
    if member['img'] in content:
        idx = content.find(member['img'])
        article_start = content.rfind('<article', 0, idx)
        article_end = content.find('</article>', idx) + len('</article>')
        old_card = content[article_start:article_end]
        
        new_card = f'''<article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="{member['img']}" alt="{member['name']}" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text={member['name'].replace(' ', '+')}'">
                                    <h4 class="text-lg font-bold">{member['front_name']}</h4>
                                    <p class="text-sm text-gray-600">{member['role']}</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">{member['back_name']}</h4>
                                    <div class="role text-sm mb-2">{member['role']}</div>
                                    <p class="text-sm mb-2">{member['bio']}</p>
                                    <div class="quote text-xs">{member['quote']}</div>
                                </div>
                            </div>
                        </article>'''
        
        content = content[:article_start] + new_card + content[article_end:]
        print(f"✅ Updated {member['name']}")

# Write back
with open('index.html', 'w', encoding=encoding) as f:
    f.write(content)

print("\n✅ All updates complete!")

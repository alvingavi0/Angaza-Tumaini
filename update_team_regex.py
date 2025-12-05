#!/usr/bin/env python3
"""Update team member cards to use flip card animation - regex version"""

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern 1: 2-column grid (Erick/Krista & Evans)
pattern_2col = r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">.*?</article>\s*<article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">.*?</article>\s*</div>'

replacement_2col = '''<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <article class="team-member rounded-xl shadow-md scroll-reveal">
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
                        </article>

                        <article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/hypeman.jpg" alt="Evans Wandera" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text=Evans'">
                                    <h4 class="text-lg font-bold">Evans Wandera</h4>
                                    <p class="text-sm text-gray-600">Programs Coordinator</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Evans Wandera</h4>
                                    <div class="role text-sm mb-2">Programs Coordinator</div>
                                    <p class="text-sm mb-2">Passionate about serving his community, ensuring every child receives care, mentorship, and academic support with Christ-centered love.</p>
                                    <div class="quote text-xs">"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6</div>
                                </div>
                            </div>
                        </article>
                    </div>'''

# Try to replace - use DOTALL flag to match across newlines
try:
    new_content = re.sub(pattern_2col, replacement_2col, content, flags=re.DOTALL)
    if new_content != content:
        print("✅ 2-column grid updated")
    else:
        print("⚠️ 2-column grid pattern not found")
    content = new_content
except Exception as e:
    print(f"❌ Error updating 2-column grid: {e}")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Done!")

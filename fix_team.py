#!/usr/bin/env python3
"""Fix team member cards - complete replacement"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of the mixed Erick/Krista card and replace the old content part
# Looking for: </h4> followed by the old div/p tags up to closing article

old_part = '<div class="text-sm text-gray-500 mb-3">Founders & Missionaries</div>\n                                    <p class="text-gray-700">Erick and Krista Baraza are passionate missionaries and the founders of Angaza Tumaini Mission Center, located in the heart of Kibera slums in Nairobi, Kenya. Married for over five years, they share a deep love for God and a calling to bring hope and transformation to their community through the Gospel of our Lord and Savior, Jesus Christ. Having been born and raised in Kibera, Erick understands the daily challenges children and families face. This personal experience birthed a vision in his heart – to create a place where children can find safety, joy, and hope. At Angaza Tumaini, kids have a space to play, study, receive a hot meal, and most importantly, encounter the love of Christ. Together, Erick and Krista are committed to shining the light of Christ in one of the most underserved areas of Nairobi – raising a new generation of young people grounded in God\'s word, equipped with education, and filled with hope for the future. Their mission is to bring the light and love of Jesus Christ to the children and families of Kibera by providing a safe space for learning, nourishment, discipleship, and spiritual growth.</p>\n                                    <div class="mt-3 text-sm italic text-gray-500">"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</div>'

new_part = '<p class="text-sm text-gray-600">Founders & Missionaries</p>\n                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>\n                                </div>\n                                <div class="team-member-back rounded-xl">\n                                    <h4 class="text-lg font-bold mb-1">Erick & Krista Baraza</h4>\n                                    <div class="role text-sm mb-2">Founders & Missionaries</div>\n                                    <p class="text-sm mb-2">Passionate missionaries and founders of Angaza Tumaini, bringing hope and transformation to Kibera through the Gospel.</p>\n                                    <div class="quote text-xs">"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</div>'

if old_part in content:
    content = content.replace(old_part, new_part)
    print("✅ Fixed Erick/Krista card")
else:
    print("⚠️ Old text pattern not found, trying alternative...")
    # Try with escaped quotes
    old_part2 = '<div class="text-sm text-gray-500 mb-3">Founders & Missionaries</div>'
    if old_part2 in content:
        print("Found old pattern with different quote style")

with open('index.html', 'w') as f:
    f.write(content)

print("Done!")

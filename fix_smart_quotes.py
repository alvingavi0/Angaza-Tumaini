#!/usr/bin/env python3
"""Fix team member cards with correct quote characters"""

# Read with latin-1 encoding
with open('index.html', 'r', encoding='latin-1') as f:
    content = f.read()

print(f"File size: {len(content)} chars")

# The smart quote character is chr(147) in Latin-1
smart_open_quote = chr(147)  # "
smart_close_quote = chr(148)  # "

# Replace Evans card with smart quotes
evans_old = f'''<article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <div class="flex items-start gap-6">
                                <img src="filez/hypeman.jpg" alt="Evans Wandera" class="w-28 h-28 rounded-full object-cover flex-shrink-0" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Evans'">
                                <div>
                                    <h4 class="text-xl font-bold">Evans Wandera</h4>
                                    <div class="text-sm text-gray-500 mb-3">Programs Coordinator</div>
                                    <p class="text-gray-700">Evans Wandera serves as the Programs Coordinator. Born and raised in Nairobi, Evans has always been passionate about serving his community, especially children and young people living in challenging circumstances. With a strong background in education and ministry, Evans brings both practical experience and a heart for discipleship to his role. He oversees the daily programs at Angaza Tumaini, ensuring that every child receives care, mentorship, academic support, and most importantly, encounters the love of Christ. Evans believes deeply that every child has God-given potential. Through his leadership, he creates programs that nurture faith, build character, and inspire hope. His dedication and compassion continue to make a lasting impact on the lives of the children and families served by the ministry.</p>
                                    <div class="mt-3 text-sm italic text-gray-500">{smart_open_quote}Train up a child in the way he should go, and when he is old, he will not depart from it.{smart_close_quote} – Proverbs 22:6</div>
                                </div>
                            </div>
                        </article>'''

evans_new = '''<article class="team-member rounded-xl shadow-md scroll-reveal">
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
                                    <div class="quote text-xs">{smart_open_quote}Train up a child in the way he should go, and when he is old, he will not depart from it.{smart_close_quote} – Proverbs 22:6</div>
                                </div>
                            </div>
                        </article>'''

if evans_old in content:
    content = content.replace(evans_old, evans_new)
    print("✅ Updated Evans card")
else:
    print("⚠️ Evans card not found - checking for variations...")
    if 'Evans Wandera serves as the Programs Coordinator' in content:
        print("  Found Evans content, but article structure differs")

# Fix Erick/Krista (currently hybrid)
erick_old = f'''<div class="text-sm text-gray-500 mb-3">Founders & Missionaries</div>
                                    <p class="text-gray-700">Erick and Krista Baraza are passionate missionaries and the founders of Angaza Tumaini Mission Center, located in the heart of Kibera slums in Nairobi, Kenya. Married for over five years, they share a deep love for God and a calling to bring hope and transformation to their community through the Gospel of our Lord and Savior, Jesus Christ. Having been born and raised in Kibera, Erick understands the daily challenges children and families face. This personal experience birthed a vision in his heart – to create a place where children can find safety, joy, and hope. At Angaza Tumaini, kids have a space to play, study, receive a hot meal, and most importantly, encounter the love of Christ. Together, Erick and Krista are committed to shining the light of Christ in one of the most underserved areas of Nairobi – raising a new generation of young people grounded in God's word, equipped with education, and filled with hope for the future. Their mission is to bring the light and love of Jesus Christ to the children and families of Kibera by providing a safe space for learning, nourishment, discipleship, and spiritual growth.</p>
                                    <div class="mt-3 text-sm italic text-gray-500">{smart_open_quote}Let your light shine before others, that they may see your good deeds and glorify your Father in heaven.{smart_close_quote} – Matthew 5:16</div>
                                </div>
                            </div>
                        </article>'''

erick_new = f'''<p class="text-sm text-gray-600">Founders & Missionaries</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Erick & Krista Baraza</h4>
                                    <div class="role text-sm mb-2">Founders & Missionaries</div>
                                    <p class="text-sm mb-2">Passionate missionaries and founders of Angaza Tumaini, bringing hope and transformation to Kibera through the Gospel.</p>
                                    <div class="quote text-xs">{smart_open_quote}Let your light shine before others, that they may see your good deeds and glorify your Father in heaven.{smart_close_quote} – Matthew 5:16</div>
                                </div>
                            </div>
                        </article>'''

if erick_old in content:
    content = content.replace(erick_old, erick_new)
    print("✅ Fixed Erick/Krista card")
else:
    print("⚠️ Erick/Krista pattern not found")
    if 'Let your light shine' in content:
        print("  Found Erick/Krista quote, but pattern structure differs")

# Write back
with open('index.html', 'w', encoding='latin-1') as f:
    f.write(content)

print("✅ Done!")

#!/usr/bin/env python3
"""Update team member cards to use flip card animation"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 2-column grid replacement (Erick/Krista & Evans)
old_2col = """                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                                <div class="flex items-start gap-6">
                                    <img src="filez/eric-and-krista.jfif" alt="Erick and Krista Baraza" class="w-28 h-28 rounded-full object-cover flex-shrink-0" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Erick+%26+Krista'">
                                <div>
                                    <h4 class="text-xl font-bold">Erick and Krista Baraza</h4>
                                    <div class="text-sm text-gray-500 mb-3">Founders & Missionaries</div>
                                    <p class="text-gray-700">Erick and Krista Baraza are passionate missionaries and the founders of Angaza Tumaini Mission Center, located in the heart of Kibera slums in Nairobi, Kenya. Married for over five years, they share a deep love for God and a calling to bring hope and transformation to their community through the Gospel of our Lord and Savior, Jesus Christ. Having been born and raised in Kibera, Erick understands the daily challenges children and families face. This personal experience birthed a vision in his heart – to create a place where children can find safety, joy, and hope. At Angaza Tumaini, kids have a space to play, study, receive a hot meal, and most importantly, encounter the love of Christ. Together, Erick and Krista are committed to shining the light of Christ in one of the most underserved areas of Nairobi – raising a new generation of young people grounded in God's word, equipped with education, and filled with hope for the future. Their mission is to bring the light and love of Jesus Christ to the children and families of Kibera by providing a safe space for learning, nourishment, discipleship, and spiritual growth.</p>
                                    <div class="mt-3 text-sm italic text-gray-500">"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</div>
                                </div>
                            </div>
                        </article>

                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <div class="flex items-start gap-6">
                                <img src="filez/hypeman.jpg" alt="Evans Wandera" class="w-28 h-28 rounded-full object-cover flex-shrink-0" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Evans'">
                                <div>
                                    <h4 class="text-xl font-bold">Evans Wandera</h4>
                                    <div class="text-sm text-gray-500 mb-3">Programs Coordinator</div>
                                    <p class="text-gray-700">Evans Wandera serves as the Programs Coordinator. Born and raised in Nairobi, Evans has always been passionate about serving his community, especially children and young people living in challenging circumstances. With a strong background in education and ministry, Evans brings both practical experience and a heart for discipleship to his role. He oversees the daily programs at Angaza Tumaini, ensuring that every child receives care, mentorship, academic support, and most importantly, encounters the love of Christ. Evans believes deeply that every child has God-given potential. Through his leadership, he creates programs that nurture faith, build character, and inspire hope. His dedication and compassion continue to make a lasting impact on the lives of the children and families served by the ministry.</p>
                                    <div class="mt-3 text-sm italic text-gray-500">"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6</div>
                                </div>
                            </div>
                        </article>
                    </div>"""

new_2col = """                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
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
                    </div>"""

# Define the 3-column grid replacement (Jackline, Felix, Naureen)
old_3col = """                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <img src="filez/Jackline.jpg" alt="Jackline Mueni" class="w-28 h-28 rounded-full object-cover mx-auto mb-4" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Jackline'">
                            <h4 class="text-xl font-bold text-center">Jackline Mueni (Jay)</h4>
                            <div class="text-sm text-gray-500 text-center mb-3">Administrator & Programs Manager</div>
                            <p class="text-gray-700">Jackline Mueni serves as the Administrator and Programs manager. With a heart for service and a passion for empowering children and families, Jackline plays a key role in ensuring the smooth running of the mission's programs and operations. Born and raised in Nairobi, Jackline has dedicated her life to ministry and community development. She combines her organizational skills with a deep love for God to create an environment where children can thrive spiritually, academically, and emotionally.</p>
                            <div class="mt-3 text-sm italic text-gray-500">"Commit to the Lord whatever you do, and He will establish your plans." – Proverbs 16:3</div>
                        </article>

                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <img src="filez/Felix.jpeg" alt="Felix Mito" class="w-28 h-28 rounded-full object-cover mx-auto mb-4" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Felix'">
                            <h4 class="text-xl font-bold text-center">Felix Mito (Teacher Feloh)</h4>
                            <div class="text-sm text-gray-500 text-center mb-3">Tutor / Teacher</div>
                            <p class="text-gray-700">Felix Mito serves as a dedicated tutor. With a heart for teaching and a passion for guiding children in both academic and faith, Felix plays a vital role in nurturing the minds and spirits of our young people in the community of Kibera. Born and raised in Nairobi, Felix has always believed in the transformative power of education. He combines patience, creativity, and a Christ-centered approach to help children build strong academic foundations while encouraging them to grow spiritually and morally.</p>
                            <div class="mt-3 text-sm italic text-gray-500">"Let the wise hear and increase in learning, and the one who understands obtain guidance." – Proverbs 1:5</div>
                        </article>

                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <img src="filez/Naureen.jpeg" alt="Naureen Mugeni" class="w-28 h-28 rounded-full object-cover mx-auto mb-4" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Naureen'">
                            <h4 class="text-xl font-bold text-center">Naureen Mugeni (Chief Chef)</h4>
                            <div class="text-sm text-gray-500 text-center mb-3">Cook</div>
                            <p class="text-gray-700">Naureen Mugeni serves as the Cook. With a heart for service and care, Naureen ensures that every child at the center receives nutritious and wholesome meals, supporting their growth, health, and overall well-being. Born and raised in Nairobi, Naureen understands the importance of providing not only physical nourishment but also a sense of love and warmth through her work.</p>
                            <div class="mt-3 text-sm italic text-gray-500">"So, whether you eat or drink or whatever you do, do it all for the glory of God." – 1 Corinthians 10:31</div>
                        </article>
                    </div>"""

new_3col = """                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/Jackline.jpg" alt="Jackline Mueni" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text=Jackline'">
                                    <h4 class="text-lg font-bold">Jackline (Jay)</h4>
                                    <p class="text-sm text-gray-600">Administrator & Programs Manager</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Jackline Mueni (Jay)</h4>
                                    <div class="role text-sm mb-2">Administrator & Programs Manager</div>
                                    <p class="text-sm mb-2">Dedicated to empowering children and families through organizational excellence and deep love for God.</p>
                                    <div class="quote text-xs">"Commit to the Lord whatever you do, and He will establish your plans." – Proverbs 16:3</div>
                                </div>
                            </div>
                        </article>

                        <article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/Felix.jpeg" alt="Felix Mito" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text=Felix'">
                                    <h4 class="text-lg font-bold">Felix (Teacher Feloh)</h4>
                                    <p class="text-sm text-gray-600">Tutor / Teacher</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Felix Mito (Teacher Feloh)</h4>
                                    <div class="role text-sm mb-2">Tutor / Teacher</div>
                                    <p class="text-sm mb-2">Passionate educator combining patience, creativity, and Christ-centered approach to build strong academic and spiritual foundations.</p>
                                    <div class="quote text-xs">"Let the wise hear and increase in learning, and the one who understands obtain guidance." – Proverbs 1:5</div>
                                </div>
                            </div>
                        </article>

                        <article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/Naureen.jpeg" alt="Naureen Mugeni" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Naureen'">
                                    <h4 class="text-lg font-bold">Naureen (Chief Chef)</h4>
                                    <p class="text-sm text-gray-600">Cook</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Naureen Mugeni (Chief Chef)</h4>
                                    <div class="role text-sm mb-2">Cook</div>
                                    <p class="text-sm mb-2">Serves with heart to ensure every child receives nutritious meals and experiences love and warmth through her dedicated work.</p>
                                    <div class="quote text-xs">"So, whether you eat or drink or whatever you do, do it all for the glory of God." – 1 Corinthians 10:31</div>
                                </div>
                            </div>
                        </article>
                    </div>"""

# Define the Benard replacement
old_benard = """                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <article class="team-member bg-white p-6 rounded-xl shadow-md scroll-reveal">
                            <img src="filez/Ben.jpeg" alt="Benard Owira" class="w-28 h-28 rounded-full object-cover mx-auto mb-4" onerror="this.onerror=null;this.src='https://placehold.co/112x112?text=Benard'">
                            <h4 class="text-xl font-bold text-center">Benard Owira (Benah)</h4>
                            <div class="text-sm text-gray-500 text-center mb-3">Support Staff</div>
                            <p class="text-gray-700">Benard Owira serves faithfully as part of the Support staff. His dedication and humble service help ensure that the center runs smoothly and remains clean, safe, and welcoming. Born and raised in Nairobi, Benard takes great pride in his work, viewing it as a way to serve God and support the mission's vision of bringing light and hope to the community. Through his daily work, Benard reflects the heart of servant-leadership – serving not for recognition, but out of love for God and others.</p>
                            <div class="mt-3 text-sm italic text-gray-500">"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23</div>
                        </article>
                    </div>"""

new_benard = """                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <article class="team-member rounded-xl shadow-md scroll-reveal">
                            <div class="team-member-inner">
                                <div class="team-member-front rounded-xl">
                                    <img src="filez/Ben.jpeg" alt="Benard Owira" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src='https://placehold.co/160x160?text=Benard'">
                                    <h4 class="text-lg font-bold">Benard (Benah)</h4>
                                    <p class="text-sm text-gray-600">Support Staff</p>
                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>
                                </div>
                                <div class="team-member-back rounded-xl">
                                    <h4 class="text-lg font-bold mb-1">Benard Owira (Benah)</h4>
                                    <div class="role text-sm mb-2">Support Staff</div>
                                    <p class="text-sm mb-2">Serves with humble dedication and pride, keeping the center clean, safe, and welcoming through servant-leadership.</p>
                                    <div class="quote text-xs">"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23</div>
                                </div>
                            </div>
                        </article>
                    </div>"""

# Apply replacements
content = content.replace(old_2col, new_2col)
content = content.replace(old_3col, new_3col)
content = content.replace(old_benard, new_benard)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Team member cards updated successfully!")
print("   - 2-column grid: Erick/Krista & Evans")
print("   - 3-column grid: Jackline, Felix, Naureen")
print("   - Benard: Updated to flip cards")
